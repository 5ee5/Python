score = 0
questions = 5

print(f"Welcome to the quiz consisting of {questions} questions")
while True:
    playing = input("Do you want to play? (yes/no): ")

    if playing.lower() == "yes":
        print("Okay! Let's play!")
        break
    elif playing.lower() == "no":
        print("Okay! Maybe next time.")
        quit()
    else:
        print("Please answer with 'yes' or 'no'.")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does OS stand for? ")
if answer.lower() == "operating system":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

percentage = (score / questions) * 100

print(f"You got {score} out of {questions} questions correct.")
print(f"You scored {percentage:.2f}% on the quiz.")
