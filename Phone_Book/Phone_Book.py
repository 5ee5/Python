import json

with open('contacts.json', 'r', encoding="utf-8") as file:
    contacts_dictionary = json.load(file)

while True:
    response = input("Enter choice: 1-Add, 2-Print, 3-Delete, 0-Exit: ")

    if response == '1':
        print('Adding new contact')
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        number = input("Enter number: ")

        contact = {
            "name": name,
            "surname": surname,
            "phone": number
        }
        contacts_dictionary["contacts"].append(contact)

    elif response == '2':
        print('Printing contacts')
        for contact in contacts_dictionary["contacts"]:
            print(contact)

    elif response == '3':
        print('Deleting contact')
        name_to_delete = input("Enter the name of the contact to delete: ")

        original_length = len(contacts_dictionary["contacts"])
        contacts_dictionary["contacts"] = [
            contact for contact in contacts_dictionary["contacts"] if contact["name"] != name_to_delete
        ]

        # Check if anything was deleted
        if len(contacts_dictionary["contacts"]) < original_length:
            print(f"Deleted contact: {name_to_delete}")
        else:
            print(f"No contact found with name: {name_to_delete}")
    elif response == '0':
        filename = "contacts.json"

        with open(filename, "w") as json_file:
            json.dump(contacts_dictionary, json_file, indent=4)
        
        print('Exiting')
        break
    else:
        print('No such choice!')
