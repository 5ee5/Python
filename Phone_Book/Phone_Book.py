contacts_list = []

while True:
    response = input("Make a choice (1. Add, 2. List all, 3. Delete, 0. Exit): ")
    
    if response == "1":
        name = input("Enter a name: ")
        phone_number = input("Enter a phone number for the contact: ")
        contacts_list.append([name, phone_number])
        print(f"Current contact list: {contacts_list}")
        
    elif response == "2":
        if contacts_list:
            print("Contacts:")
            for index, contact in enumerate(contacts_list):
                print(f"{index + 1}. {contact[0]}  {contact[1]}")
        else:
            print("No contacts found.")
        
    elif response == "3":
        contact_to_remove = input("Enter the name of the contact you want to remove: ")
        found = False
        for contact in contacts_list:
            if contact[0] == contact_to_remove:
                contacts_list.remove(contact)
                found = True
                print(f"{contact_to_remove} was removed from the contacts.")
                break
        if not found:
            print("Contact not found.")
        
    elif response == "0":
        print("BYE BYE!")
        break
    else:
        print("Enter a valid number.")