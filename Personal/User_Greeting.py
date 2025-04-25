from datetime import datetime

# Get the current date
now = datetime.now()

name = input("What's your name: ")
birth_year = int(input("What year were you born in: "))
birth_month = int(input("What month were you born in (1-12): "))
birth_day = int(input("What day were you born on (1-31): "))

# Create a birth date object
birth_date = datetime(birth_year, birth_month, birth_day)

# Calculate the age
age = now.year - birth_date.year

# Adjust the age if the birthday hasn't occurred yet this year
if (now.month, now.day) < (birth_date.month, birth_date.day):
    age -= 1

print(f"Hello {name}! You are {age} years old and you were born on {birth_date.strftime('%Y-%m-%d')}!")
