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

def EditForValidDBText(text):
    text = text.strip().lower()
    return text

def FindUser(user_data):
    dbData = GetUsersData()
    if user in dbData:
        if user["first_name"] == user_data["first_name"] and user["second_name"] == user_data["second_name"]:
            return True
    return False


def GetAllUserData(user_data):
    dbData = GetUsersData()
    if user in dbData:
        if user["first_name"] == user_data["first_name"] and user["second_name"] == user_data["second_name"]:
            return user
    return None