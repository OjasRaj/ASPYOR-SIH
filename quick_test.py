from copilot.agent import RetailCopilot


def main():

    copilot = RetailCopilot()

    print("\nRetail Intelligence Copilot")
    print("Type 'exit' to stop.\n")

    while True:

        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            break

        if not user_input:
            continue

        try:
            answer = copilot.ask(user_input)

            print("\nCopilot:")
            print(answer)
            print()

        except Exception as error:
            print("\nError:")
            print(error)
            print()


if __name__ == "__main__":
    main()