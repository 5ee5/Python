import random

start = float(input("Enter the start point: "))
end = float(input("Enter the end point: "))

choice = input("Do you want a whole number or a floating-point number? (enter 'whole' or 'float'): ").strip().lower()


if choice == 'whole':
    random_number = random.randint(int(start), int(end))
elif choice == 'float':
    random_number = random.uniform(start, end)
else:
    print("Invalid choice! Please enter 'whole' or 'float'.")
    random_number = None

if random_number is not None:
    print(f"Random number between {start} and {end}: {random_number}")
