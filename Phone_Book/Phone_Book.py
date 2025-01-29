import json

# contacts = [['Anna', '987654321'], ['Oskars', '123456789'], ['Jenifere', '654987321']]

with open('contacts.json', 'r', encoding="utf-8") as file:
    contacts_dictionary = json.load(file)

while True:
    response = input("Enter choice: 1-Add, 2-Print, 3-Delete, 0-Exit: ")

    if response == '1':
        print('Adding new contact')
        name = input("Enter name: ")
        number = input("Enter number: ")

        contact = {
            "name": name,
            "phone": number
        }
        contacts_dictionary["contacts"].append(contact)

    elif response == '2':
        print('Printing contacts')
        for contact in contacts_dictionary["contacts"]:
            print(contact)

    elif response == '3':
        print('Deleting contact')
    
    elif response == '0':
        filename = "contacts.json" #svarīgi, jo tas ir faila nosaukums

        with open(filename, "w") as json_file:
            json.dump(contacts_dictionary, json_file, indent=4)
        
        print('Exiting')
        break
    else:
        print('No such choice!')
