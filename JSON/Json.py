import json

# Open and read the JSON file
with open('/home/e5/Code/Python/JSON/data.json', 'r') as file:
    data = json.load(file)

# Print the data
print(data)