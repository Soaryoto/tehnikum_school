import json
import datetime
import config

__construct_database = {
    "events" : [
#        {
#            "name" : "",
#            "parametrs" : ""
#        }
    ],
    "users_data" : [
#        {
#            "name" : "",
#            "presence" : "",
#            "absence" : "",
#            "last_actions" : ""
#        }
    ]
}

ACTIONS = ["work", "rest"]


def __getNameDatabase():
    date = datetime.datetime.now()
    return date.strftime("%d_%m_%Y") + ".json"

def __setDataInDatabase():
    with open("database/" + __getNameDatabase(), "w") as databese_file:
        json.dump(__construct_database, databese_file)

def getData():
    return __construct_database

def setAttendanceUser(user_name, action):
    date = datetime.datetime.now()

    serial_number = -1

    for i in range(len(__construct_database["users_data"])):
        if __construct_database["users_data"][i]["name"] == user_name:
            serial_number = i
            break

    if serial_number < 0:
        serial_number = len(__construct_database["users_data"])
        __construct_database["users_data"].append({
            "name" : user_name,
            "presence" : [ 0, 0, 0 ],
            "absence" : [ 0, 0, 0 ],
            "last_actions" : [ date.hour, date.minute, date.second ] })

    key = ""
    if action == ACTIONS[0]:
        #add presence
        key = "presence"
    else:
        #add absence
        key = "absence"

    hour = __construct_database["users_data"][serial_number][key][0]
    minute = __construct_database["users_data"][serial_number][key][1]
    seconds = __construct_database["users_data"][serial_number][key][2]
    last_actions_date = __construct_database["users_data"][serial_number]["last_actions"]

    seconds += date.second - last_actions_date[2]
    if seconds > 60:
        seconds -= 60
        minute += 1
    elif seconds < 0:
        seconds += 60
        minute -= 1
        
    minute += date.minute - last_actions_date[1]
    if minute > 60:
        minute -= 60
        hour += 1
    elif minute < 0:
        minute += 60
        hour -= 1

    hour += date.hour - last_actions_date[0]


    __construct_database["users_data"][serial_number][key] = [ hour, minute, seconds]
    __construct_database["users_data"][serial_number]["last_actions"] = [ date.hour, date.minute, date.second ]
    
