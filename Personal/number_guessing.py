import random

number_target = random.randint(1, 100)

number_of_guesses = 0
number_lower = 1
number_upper = 100
guesses = []

while True:    
    number_guess = random.randint(number_lower, number_upper)
    guesses.append(number_guess)
    number_of_guesses += 1

    if number_guess == number_target:
        if number_of_guesses <= 3:
            print(f"Wow, you are a super player, you won from {number_guess} guesses!")
        elif number_of_guesses <= 10:
            print(f"Nice, you have won after {number_of_guesses} guesses!")
        else:
            print(f"Well, you could have done better than {number_of_guesses} guesses...")
        break
    elif number_guess < number_target:
        print("Guess higher")
        number_lower = number_guess + 1
    elif number_guess > number_target:
        print("Guess lower")
        number_upper = number_guess - 1

print(guesses)