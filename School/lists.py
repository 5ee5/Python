names = ["Anna", "Oscar", "Jennifer", "Janis"]

#for name in names:
#    print(f"Hey hey {name}!")

ages = [16, 15, 21, 18]
University = [False, False, True, True]

personal_data = [
    ["Anna", 16, False, "anna@mail.com"],
    ["Oskars", 15, False, "oscar@bestmail.com"],
    ["Jennifer", 21, True, "jennifer@smitch.com"],
    ["Janis", 18, True, "janis.krumins@gmail.com"]
]

name = input('Enter your name: ')
age = int(input('Enter your age: '))
university = input('Are you in university? (yes/no): ').lower() == 'yes'
email = input('Enter your email: ')

new_data = [name, age, university, email]
personal_data.append(new_data)