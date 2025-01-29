
contacts = [['Anna', '987654321'], ['Oskars', '123456789'], ['Jenifere', '654987321']]
contacts_dictionary = {}
while True:
    response = input("Izvēlies darbību 1-pievienot, 2-izvadīt, 3-izdēst, 0-iziet: ")

    if response == '1':
        print('Pievienosim jaunu kontaktus')
        name = input("Ievadi vārdu: ")
        number = input("Ievadi numuru: ")
        contacts.append([name, number])
    elif response == '2':
        print('Izvadīsim visus kontaktus')
        for contact in contacts:
            print(f"{contact[0]} {contact[1]}")

    elif response == '3':
        print('Deleting contact')
    elif response == '0':
        print('Exiting')
        break
    else:
        print('Šadas izvēles nav!')
