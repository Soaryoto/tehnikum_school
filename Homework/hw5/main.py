from functions import *


def Start():
    # Начальные данные
    # AddUser("Адыл", "25", "m", "uz")
    # AddUser("Вова", "40", "m", "kz")
    # AddUser("Максим", "22", "m", "en")
    # AddUser("Яна", "35", "f", "ru")

    # Для красоты добавляем админа
    print("Впишите ваши данные через пробел (Имя возраст пол язык(ru)): ")
    com_text = input()
    temp_arr = com_text.split(" ")
    AddUser(temp_arr[0], temp_arr[1], temp_arr[2], temp_arr[3], "admin")

    NUN = temp_arr[0]
    LOCAL = temp_arr[3]

    print(UserDatabase)

    while True:
        com_text = input()
        temp_arr = com_text.split(" ")

        if len(temp_arr) > 0 and temp_arr[0][:1] == "!": # Проверка функция ли это

            if func_command.index(temp_arr[0]) in [7, 8, 9]: # Функция вывода всех функций
                print(func_command)

            elif func_command.index(temp_arr[0]) == 6: # Функция вывода всех пользователей
                print(UserDatabase)

            elif func_command.index(temp_arr[0]) == 0: # Функция добавления пользователя
                if len(temp_arr) == 2:
                    AddUser(temp_arr[1])
                elif len(temp_arr) == 3:
                    AddUser(temp_arr[1], temp_arr[2])
                elif len(temp_arr) == 4:
                    AddUser(temp_arr[1], temp_arr[2], temp_arr[3])
                elif len(temp_arr) == 5:
                    AddUser(temp_arr[1], temp_arr[2], temp_arr[3], temp_arr[4])
                else:
                    print(glob_texts[LOCAL]["error_many_params"])

            elif func_command.index(temp_arr[0]) == 1: # Функция вывода пользователя по его index
                if temp_arr[1].isdigit():
                    print(GetUserForId(int(temp_arr[1])))
                else:
                    print(glob_texts[LOCAL]["error_index"])

            elif func_command.index(temp_arr[0]) == 2: # Функция вывода пользователя по его name
                if len(temp_arr) == 1:
                    print(glob_texts[LOCAL]["error_few_params"])
                else:
                    print(GetUserForName(temp_arr[1]))

            elif func_command.index(temp_arr[0]) == 3: # Функция удаления пользователя по его index
                if temp_arr[1].isdigit():
                    print(glob_texts[LOCAL]["confirm_delete"])
                    print(GetUserForId(int(temp_arr[1])))
                    u_input = input()
                    if u_input.lower() in user_ansver[LOCAL]["yes"]:
                        DeleteUserForId(int(temp_arr[1]))
                    else:
                        print(glob_texts[LOCAL]["function_end"])
                else:
                    print(glob_texts[LOCAL]["error_index"])

            elif func_command.index(temp_arr[0]) == 4: # Функция удаления пользователя по его name
                print(glob_texts[LOCAL]["confirm_delete"])
                print(GetUserForName(temp_arr[1]))
                u_input = input()
                if u_input.lower() in user_ansver[LOCAL]["yes"]:
                    DeleteUserForName(temp_arr[1])
                else:
                    print(glob_texts[LOCAL]["function_end"])

            elif func_command.index(temp_arr[0]) == 5: # Функция обновления пользователя по его index
                if temp_arr[1].isdigit():
                    if len(temp_arr) < 3:
                        print(glob_texts[LOCAL]["error_few_params"])
                    elif len(temp_arr) > (2 + len(UserDatabaseParams)):
                        print(glob_texts[LOCAL]["error_many_params"])
                    else:
                        UserApdateForId(int(temp_arr[1]), temp_arr[2:])
                else:
                    print(glob_texts[LOCAL]["error_index"])

            else:
                print(glob_texts[LOCAL]["error_command"] + "(it is not function)")
        else:
            print(glob_texts[LOCAL]["error_command"] + "(not in ! or null)")

Start()