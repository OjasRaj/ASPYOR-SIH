import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.3-70b-versatile"
)


if not GROQ_API_KEY:
    raise RuntimeError(
        "GROQ_API_KEY is not set. "
        "Add it to your .env file."
    )


client = Groq(api_key=GROQ_API_KEY)


def chat(
    messages: list[dict],
    tools: list[dict] | None = None,
    tool_choice: str = "auto"
):
    """
    Send a conversation to the Groq model.

    Parameters
    ----------
    messages:
        Conversation history.

    tools:
        Tools that the model is allowed to call.

    tool_choice:
        Controls whether the model may call tools automatically.
    """

    kwargs = {
        "model": GROQ_MODEL,
        "messages": messages,
        "temperature": 0.2,
    }

    if tools:
        kwargs["tools"] = tools
        kwargs["tool_choice"] = tool_choice

    return client.chat.completions.create(**kwargs)