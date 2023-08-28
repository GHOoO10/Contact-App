class Contact:
    #This function: Receives name, phone, and email.
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    #This function: Returns contact details as string
    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"

class ContactManager:
    #Receive empty list of contacts
    def __init__(self):
        self.contacts = []
        
    #This function: It receives an object from Contact and adds it to the contact list
    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    #This function: Take Contact name and delete it from the list.
    def remove_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print("Contact removed successfully.")
                return
        print("Contact not found.")

    #This function: It takes name as parameter and searches the list for the contact.
    # If the contact is found, it is returned, otherwise, None is returned.
    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    #This function: Displays all contacts in the list.
    # If no contacts found, it prints "No contacts found".
    def display_contacts(self):
        if len(self.contacts) == 0:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)

contact_manager = ContactManager()

while True:
    print("Contact Manager:")
    print("1- Add contact")
    print("2- Remove contact")
    print("3- Search contact")
    print("4- Display contacts")
    print("5- Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contact = Contact(name, phone, email)
        contact_manager.add_contact(contact)

    elif choice == "2":
        name = input("Enter name of contact to remove: ")
        contact_manager.remove_contact(name)

    elif choice == "3":
        name = input("Enter name of contact to search: ")
        contact = contact_manager.search_contact(name)
        if contact:
            print(contact)
        else:
            print("Contact not found.")

    elif choice == "4":
        contact_manager.display_contacts()

    elif choice == "5":
        print("Exit Program")
        break

    else:
        print("Error choice. Please try again, choice from 1 to 5.")