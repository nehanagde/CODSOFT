contacts = []

def add_contact():
    print("\nAdd New Contact")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    print("\nContact List")
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    print("\nSearch Contact")
    keyword = input("Enter name or phone number to search: ")
    found = False

    for contact in contacts:
        if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True

    if not found:
        print("No matching contact found.")

def update_contact():
    print("\nUpdate Contact")
    name = input("Enter the name of the contact to update: ")

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Leave a field empty to keep the existing value.")
            new_phone = input("New phone number: ") or contact['phone']
            new_email = input("New email: ") or contact['email']
            new_address = input("New address: ") or contact['address']

            contact['phone'] = new_phone
            contact['email'] = new_email
            contact['address'] = new_address

            print("Contact updated successfully!")
            return

    print("Contact not found.")

def delete_contact():
    print("\nDelete Contact")
    name = input("Enter the name of the contact to delete: ")

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")

def menu():
    print("Welcome to Neha Nagde's Contact Manager!")
    while True:
        print("\n---------- MENU ----------")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("\nThank you!")
            break
        else:
            print("Invalid choice. Please select from 1 to 6.")

menu()
