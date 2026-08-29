import json
from typing import Any

from copilot.llm import chat
from copilot.prompts import SYSTEM_PROMPT
from copilot.tool_schemas import TOOL_SCHEMAS

from tools.registry import TOOL_REGISTRY


MAX_TOOL_ROUNDS = 5


class RetailCopilot:
    """
    Main conversational Copilot.

    Responsibilities:
    - Maintain conversation history
    - Ask the LLM to answer the user's question
    - Execute requested tools
    - Return tool results to the LLM
    - Produce the final natural-language response
    """

    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

    def ask(self, user_message: str) -> str:
        """
        Process a user question and return the final answer.
        """

        self.messages.append({
            "role": "user",
            "content": user_message
        })

        for _ in range(MAX_TOOL_ROUNDS):

            response = chat(
                messages=self.messages,
                tools=TOOL_SCHEMAS,
                tool_choice="auto"
            )

            assistant_message = response.choices[0].message

            # --------------------------------------------
            # No tool required
            # --------------------------------------------

            if not assistant_message.tool_calls:

                answer = assistant_message.content

                self.messages.append({
                    "role": "assistant",
                    "content": answer
                })

                return answer

            # --------------------------------------------
            # Tool call requested
            # --------------------------------------------

            self.messages.append(
                assistant_message.model_dump(exclude_none=True)
            )

            for tool_call in assistant_message.tool_calls:

                tool_name = tool_call.function.name
                arguments_raw = tool_call.function.arguments

                try:
                    arguments = json.loads(arguments_raw)
                except json.JSONDecodeError:

                    tool_result = {
                        "status": "error",
                        "message": "Invalid tool arguments."
                    }

                else:
                    tool_result = self._execute_tool(
                        tool_name,
                        arguments
                    )

                self.messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(tool_result)
                })

        return (
            "I couldn't complete the analysis within the "
            "allowed processing steps."
        )

    @staticmethod
    def _execute_tool(
        tool_name: str,
        arguments: dict[str, Any]
    ) -> dict[str, Any]:

        tool = TOOL_REGISTRY.get(tool_name)

        if tool is None:
            return {
                "status": "error",
                "message": f"Unknown tool: {tool_name}"
            }

        try:
            return tool(**arguments)

        except Exception as error:
            return {
                "status": "error",
                "message": (
                    f"Tool execution failed: {str(error)}"
                )
            }