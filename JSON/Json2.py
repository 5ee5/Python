import json

# Open and read the JSON file
with open('/home/e5/Code/Python/JSON/students.json', 'r') as file:
    data = json.load(file)

# Print the data
for student in data['students']:
    print('Name:', student['name'], "age:", student['age'], "Grade:", student['grade'])

TotalAge = sum([student['age'] for student in data['students']])
AverageAge = TotalAge / len(data['students'])

print(f"Average age: {AverageAge:.2f}")