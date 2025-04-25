import random
words = ["python","java","kotlin","javascript","swift","ruby"]
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]
attempts = 8
print(word_display)

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display:
    print("\n" + " ".join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print("Wrong! That letter does not appear in the word.")
        attempts -= 1

if "_" not in word_display:
    print("You guessed the word!")
    print(" ".join(word_display))
    print("You survived!")
else:
    print(f"You ran out of attempts. the word was:{chosen_word}")
    print("You lost!")
