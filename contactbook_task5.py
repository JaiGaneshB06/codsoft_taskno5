contacts = []
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contact = {"name": name,"phone": phone,"email": email,"address": address}
    contacts.append(contact)
    print("Contact added successfully!")
def view_contacts():
    if len(contacts) == 0:
        print("No contacts found.")
    else:
        print("\n===== CONTACT LIST =====")
        for i in range(len(contacts)):
            print(f"{i+1}. {contacts[i]['name']} - {contacts[i]['phone']}")
def search_contact():
    search = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if search == contact["name"] or search == contact["phone"]:
            print("\nContact Found")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            found = True
    if not found:
        print("Contact not found.")
def update_contact():
    name = input("Enter contact name to update: ")
    found = False
    for contact in contacts:
        if contact["name"] == name:
            contact["phone"] = input("Enter new phone number: ")
            contact["email"] = input("Enter new email: ")
            contact["address"] = input("Enter new address: ")
            print("Contact updated successfully!")
            found = True
    if not found:
        print("Contact not found.")
def delete_contact():
    name = input("Enter contact name to delete: ")
    found = False
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            found = True
            break
    if not found:
        print("Contact not found.")
while True:
    print("\n===== CONTACT BOOK MENU =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice(1-6): ")
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
        print("Exiting Contact Book...")
        break
    else:
        print("Invalid choice! Please try again.")