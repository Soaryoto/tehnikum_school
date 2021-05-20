from constants import *
from database import *

NUN = "" # NOW_USER_NAME
LOCAL = ""

def AddUser(Name, Age = "", Sex = "", Local = "ru",  Role = "user"):
    UserDatabase["name"].append(Name)
    UserDatabase["age"].append(Age)
    UserDatabase["sex"].append(Sex)
    UserDatabase["locate"].append(Local)
    UserDatabase["role"].append(Role)


def GetUserForId(index):
    vocabulary = {}
    if index < len(UserDatabase['name']):
        for key in UserDatabaseParams:
            vocabulary.update({ key: UserDatabase[key][index]})
    return vocabulary

def GetUserForName(Name):
    list = []

    for i in range(0, len(UserDatabase["name"])):
        if UserDatabase["name"][i] == Name:
            vocabulary = {}
            for key in UserDatabaseParams:
                vocabulary.update({ key: UserDatabase[key][i]})
            list.append(vocabulary)

    return list

def DeleteUserForId(Index):
    for key in UserDatabaseParams:
        UserDatabase[key].pop(Index)

def DeleteUserForName(Name):
    for i in range(0, len(UserDatabase["name"])):
        if UserDatabase["name"][i] == Name:
            for key in UserDatabaseParams:
                UserDatabase[key].pop(i)


def UserApdateForId(Index, data):
    for i in range(0, len(data)):
        UserDatabase[UserDatabaseParams[i]][Index] = data[i]
