contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")

    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact {name} added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts in the contact book.")
    else:
        print("Contact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}")

def search_contact():
    name = input("Enter contact name to search: ")
    if name in contacts:
        print(f"Contact {name} found!")
        print(f"Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}, Address: {contacts[name]['address']}")
    else:
        print(f"Contact {name} not found.")

def update_contact():
    name = input("Enter contact name to update: ")
    if name in contacts:
        print("Enter new information (press enter to keep current value):")
        phone = input("Enter new phone number: ") or contacts[name]["phone"]
        email = input("Enter new email: ") or contacts[name]["email"]
        address = input("Enter new address: ") or contacts[name]["address"]

        contacts[name] = {"phone": phone, "email": email, "address": address}
        print(f"Contact {name} updated successfully!")
    else:
        print(f"Contact {name} not found.")

def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"Contact {name} not found.")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "_main_":
    main()