HELP = """
    Commands:
    - hello: Greeting.
    - add <name> <phone>:Add new contact.
    - phone <name>: Get contact.
    - change <name> <phone>: Change the phone number of a contact.
    - all: All contacts.
    - help: All commands.
    - close/exit: Close the assistant.
    """

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return f"Contact {name} not found."

def get_phone(args, contacts):
    name, *args = args
    phone = contacts.get(name)
    if phone:
        return phone
    return f"Contact {name} not found."

def get_all_contacts(contacts):
    if len(contacts) == 0:
        return "No contacts found."
    res = ""
    for k, v in contacts.items():
        res+=f"{k}: {v}\n"

    return res

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)
            match command:
                case "close" | "exit":
                    print("Good bye!")
                    break
                case "hello":
                    print("How can I help you?")
                case "add":
                    print(add_contact(args, contacts))
                case "change":
                    print(change_contact(args, contacts))
                case "phone":
                    print(get_phone(args, contacts))
                case "all":
                    print(get_all_contacts(contacts))
                case "help":
                    print(HELP)
                case _:
                    print("Invalid command.")
        except Exception as e:
            print(HELP)

if __name__ == "__main__":
    main()