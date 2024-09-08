# Basic contact management system

contacts = []

def display_menu():
    print("\n--- Contact Management System ---")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contacts.append(contact)
    print(f"\nContact '{name}' added successfully!")

def view_contacts():
    if contacts:
        print("\n--- Contact List ---")
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("\nNo contacts found!")

def update_contact():
    if contacts:
        view_contacts()
        choice = int(input("\nEnter the number of the contact you want to update: "))
        if 0 < choice <= len(contacts):
            contact = contacts[choice - 1]
            print(f"\nUpdating contact: {contact['name']}")
            contact['name'] = input(f"Enter new name (current: {contact['name']}): ") or contact['name']
            contact['phone'] = input(f"Enter new phone (current: {contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Enter new email (current: {contact['email']}): ") or contact['email']
            print("\nContact updated successfully!")
        else:
            print("\nInvalid choice!")
    else:
        print("\nNo contacts to update!")

def delete_contact():
    if contacts:
        view_contacts()
        choice = int(input("\nEnter the number of the contact you want to delete: "))
        if 0 < choice <= len(contacts):
            deleted_contact = contacts.pop(choice - 1)
            print(f"\nContact '{deleted_contact['name']}' deleted successfully!")
        else:
            print("\nInvalid choice!")
    else:
        print("\nNo contacts to delete!")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("\nExiting Contact Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
