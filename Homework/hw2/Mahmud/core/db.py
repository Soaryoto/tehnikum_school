import json

def SaveUsersData(data):
    with open('database/users.json', 'w') as file:
        json.dump(data, file)

def GetUsersData():
    data = []
    with open('database/users.json', 'r') as file:
        for line in file:
            data = json.loads(line)
    return data