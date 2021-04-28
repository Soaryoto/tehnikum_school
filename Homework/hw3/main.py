# Soaryoto
import time
import core.base as Base
import core.image as Images
import core.functions as Functions

# Постоянные переменки
user_data = Base.GetDefaultDataUser()
error = False

Base.FullScreen() # На весь экран
Base.CleareConsole() # Чистим консоль

# На время тестирования закомментировал
# Base.WindLoad()

# Вытягиваю инфу о пользователе
Base.PrintTextWithImage(Base.GetString("get_user_name_text"), "img2")

while True:
    if error:
        Base.PrintTextWithImage(Base.GetString("get_user_name_text_error"), "img9")

    u_t_input = Base.GetInputUsersText()
    if u_t_input == "" or u_t_input.isdigit():
        error = True
        continue
    user_data["first_name"] = u_t_input
    break

Base.PrintTextWithImage(Base.GetString("get_hello_user_with_name").format(user_data["first_name"]), "img2")
Base.SetViewBlockForInput()

time.sleep(3)

Base.PrintTextWithImage(Base.GetString("get_user_second_name_text").format(user_data["first_name"]), "img4")

while True:
    if error:
        Base.CleareConsole() # Чистим консоль
        Base.PrintTextWithImage(Base.GetString("get_user_second_name_text_error"), "img9")

    u_t_input = Base.GetInputUsersText()
    if u_t_input == "" or u_t_input.isdigit():
        error = True
        continue
    elif u_t_input.lower() in Base.GetInStringArr("arr_no"):
        Base.PrintTextWithImage(Base.GetString("answer_user_second_name_text_no"), "img1")
        Base.SetViewBlockForInput()
        time.sleep(3)
        break
    user_data["second_name"] = u_t_input
    break

# Если успею нужно будет добавить ещё разговоров для взятия инфы. Если девушка то и номерок не забыть


# Тут уже наконец дз делаю

# Easy 1
result = []
Base.PrintTextWithImage(Base.GetString("get_task_1_text"), "img6")
while True:
    u_t_input = Base.GetInputUsersText()
    if u_t_input.lower() in Base.GetInStringArr("arr_no"):
        u_t_input = "Шла Саша по шоссе и сосала сушку"
        Base.CleareConsole() # Чистим консоль
        Base.PrintTextWithImage(Base.GetString("get_task_1_text_no"), "img3")
        Base.SetViewBlockForInput()
        time.sleep(3)
    elif u_t_input == "" or u_t_input.isdigit():
        Base.CleareConsole() # Чистим консоль
        Base.PrintTextWithImage(Base.GetString("get_task_1_text_error"), "img9")
        continue
    result = Functions.EasyTask_1(u_t_input)
    break


Base.CleareConsole() # Чистим консоль
Base.PrintArrWithImage(result, Base.GetString("get_task_1_text_result"), "img6")
Base.SetViewBlockForInput()
time.sleep(5)
# /Easy 1

# Easy 2
Base.CleareConsole() # Чистим консоль
Base.PrintTextWithImage(Base.GetString("get_task_2_text"), "img8")
Base.SetViewBlockForInput()
time.sleep(5)

Base.CleareConsole() # Чистим консоль
Base.PrintTextWithImage(Base.GetString("get_task_2_text_first"), "img1")

temp_arr = []
end_add_numbers = False

while True:
    u_t_input = Base.GetInputUsersText()
    if u_t_input == "0":
        Base.CleareConsole() # Чистим консоль
        Base.PrintTextWithImage(Base.GetString("get_task_2_text_end_null"), "img1")
        Base.SetViewBlockForInput()
        end_add_numbers = True
        time.sleep(3)
        break
    elif u_t_input.isdigit() or (len(u_t_input.split(".")) == 2 and u_t_input.split(".")[0].isdigit() and u_t_input.split(".")[1].isdigit()):
        temp_arr.append(float(u_t_input))
        break
    else:
        Base.CleareConsole() # Чистим консоль
        Base.PrintTextWithImage(Base.GetString("get_task_2_text_error"), "img9")
        continue

Base.PrintTextWithImage(Base.GetString("get_task_2_text_next"), "img1")
while True and end_add_numbers == False:
    u_t_input = Base.GetInputUsersText()
    if u_t_input == "0":
        Base.CleareConsole() # Чистим консоль
        Base.PrintTextWithImage(Base.GetString("get_task_2_text_end").format(Functions.EasyTask_2(temp_arr)), "img1")
        Base.SetViewBlockForInput()
        time.sleep(3)
        break
    elif u_t_input.isdigit() or (len(u_t_input.split(".")) == 2 and u_t_input.split(".")[0].isdigit() and u_t_input.split(".")[1].isdigit()):
        temp_arr.append(float(u_t_input))
        Base.CleareConsole() # Чистим консоль
        Base.PrintTextWithImage(Base.GetString("get_task_2_text_result").format(Functions.EasyTask_2(temp_arr)), "img3")
        Base.SetViewBlockForInput()
        time.sleep(3)
        Base.CleareConsole() # Чистим консоль
        Base.PrintTextWithImage(Base.GetString("get_task_2_text_next"), "img1")
        continue
    else:
        Base.CleareConsole() # Чистим консоль
        Base.PrintTextWithImage(Base.GetString("get_task_2_text_error"), "img9")
        continue


# /Easy 2
