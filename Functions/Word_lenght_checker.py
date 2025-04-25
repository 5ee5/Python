def length(word):
    length = len(word)

    if length < 5:
        response = "short"
    elif length < 10:
        response = "average"
    else:
        response = "long"

    print(f"The length of '{word}' is {length}, which is {response}.")

# Get user input and call the function
user_word = input("Enter a word: ")
length(user_word)
