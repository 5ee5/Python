from datetime import datetime

def calculate_age(name: str, birthdate: str):
    birth_date = datetime.strptime(birthdate, "%Y-%m-%d").date()
    today = datetime.today().date()

    # Calculate full years
    years = today.year - birth_date.year
    months = today.month - birth_date.month

    # Adjust if the birth month hasn't occurred yet this year
    if months < 0:
        years -= 1
        months += 12  # Convert negative months to positive

    print(f"{name} is {years} years and {months} months old.")

# Get user input
name = input("Enter your name: ")
birth_date = input("Enter your birthdate (YYYY-MM-DD): ")

# Call the function
calculate_age(name, birth_date)

