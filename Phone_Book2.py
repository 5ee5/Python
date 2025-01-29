contacts_dictionary = {
        "contacts": [
            {
             "name": "Anna",
             "surname":"Doe",
             "number": "987654321"
            },
            {
             "name": "Oscar",
             "surname": "Doe",
             "number": "123456789"
            },
            {
             "name": "Jenny",
             "surname": "Doe",
             "number": "654987321"
            }
            ]
        }

while True:
    response = input("Choose: 1-Add, 2-Print, 3-Delete, 0-Exit: ")

    if response == '1':
        print('Adding new contact')
        name = input("Enter name: ")
        surname = input("Enter surname: ")
        number = input("Enter number: ")

        contacts_dictionary["contacts"].append({
            "name": name,
            "surname": surname,
            "number": number
        })

    elif response == '2':
        print('Printing all contacts')
        for contact in contacts:
            print(f"{contact[0]} {contact[1]}")

    elif response == '3':
        int(input('Enter the index of the contact you want to delete: '))
        print('Deleting contact')
        if index < len(contacts):
            contacts.pop(index)
        else:
            print('Index not found')

    elif response == '0':
        print('Exiting')
        break
    else:
        print('No such option!')
