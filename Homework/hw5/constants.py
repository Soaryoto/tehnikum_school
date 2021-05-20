func_command = [
    "!AddUser", # 0
    "!GetUserForId", # 1
    "!GetUserForName", # 2
    "!DeleteUserForId", # 3
    "!DeleteUserForName", # 4
    "!UserApdateForId", # 5
    "!PrintDataUser", # 6
    "!Help", "!help", "!HELP" # 7, 8, 9
]

glob_texts = {
    "ru" : {
        "function_end" : "Прекращаю выполнение функции",
        "confirm_delete" : "Вы точно хотите удалить ?",
        "error_command" : "Неверная команда",
        "error_index" : "Неправвелно ввели индекc",
        "error_many_params" : "Ошибка, передано большое кол-во параметров",
        "error_few_params" : "Ошибка, недостаточное кол-во параметров"
    }
}

user_ansver = {
    "ru" : {
        "yes" : ["да", "конечно"],
        "no" : ["нет"],
        "break" : ["пропустить"]
    }
}