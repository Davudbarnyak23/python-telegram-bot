import json

data = {
    'name': 'Mike',
    'city': 'K-P',
    'hobbies': ['reading', 'walking']
}

with open('json.txt', 'w') as file:
    json.dump(data, file)

with (open('json.txt', 'r') as file):
    data_file = json.dump(file)

print(data_file['name'])