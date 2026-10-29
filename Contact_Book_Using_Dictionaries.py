# Contact Book Using Dictionaries
contacts = {}
def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if not name or not phone:
        print("Name and phone number are required.")
        return

    if phone in contacts:
        print("A contact with this phone number already exists.")
        return

    contacts[phone] = {
        "name": name,
        "email": email
    }

    print("Contact added successfully!")
def search_contact():
    phone = input("Enter phone number to search: ").strip()

    if phone in contacts:
        print("Name:", contacts[phone]["name"])
        print("Phone:", phone)
        print("Email:", contacts[phone]["email"])
    else:
        print("Contact not found.")
def update_contact():
    phone = input("Enter phone number to update: ").strip()

    if phone not in contacts:
        print("Contact not found.")
        return

    name = input("Enter new name: ").strip()
    email = input("Enter new email: ").strip()

    if name:
        contacts[phone]["name"] = name

    if email:
        contacts[phone]["email"] = email

    print("Contact updated successfully!")
def delete_contact():
    phone = input("Enter phone number to delete: ").strip()

    if phone in contacts:
        del contacts[phone]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")
def view_contacts():
    if not contacts:
        print("No contacts saved.")
        return

    print("\n--- Saved Contacts ---")

    for phone, details in contacts.items():
        print("Name:", details["name"])
        print("Phone:", phone)
        print("Email:", details["email"])
        print("--------------------")
while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        view_contacts()
    elif choice == "6":
        print("Thank you for using Contact Book!")
        break
    else:
        print("Invalid choice. Please enter 1-6.")
