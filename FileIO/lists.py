list = []

while True:
    action = input('Enter new, remove vai stop: ').lower()

    if action == "new":
        word = input("Enter new word: ")
        list.append(word)
        print(list)
    elif action == "remove":
        word_to_remove = input('Enter the word you want to remove: ')
        if word_to_remove in list:
            list.remove(word_to_remove)
            print(f'{word_to_remove} removed from the list.')
        else:
            print(f'{word_to_remove} not found in the list.')
    elif action == "stop":
        print("Final list:", list)
        break
    else:
        print("Invalid command. Please enter 'new', 'remove', or 'stop'.")
