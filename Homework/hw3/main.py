# Soaryoto
import time
import core.base as Base
import core.image as Images
import core.functions as Functions
import random

# Постоянные переменки
user_data = Base.GetDefaultDataUser()
error = False

Base.FullScreen() # На весь экран
Base.CleareConsole() # Чистим консоль

# На время тестирования закомментировал
Base.WindLoad()

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
Base.PrintTextWithImage(Base.GetString("get_e_task_1_text"), "img6")
while True:
    u_t_input = Base.GetInputUsersText()
    if u_t_input.lower() in Base.GetInStringArr("arr_no"):
        u_t_input = "Шла Саша по шоссе и сосала сушку"
        Base.CleareConsole() # Чистим консоль
        Base.PrintTextWithImage(Base.GetString("get_e_task_1_text_no"), "img3")
        Base.SetViewBlockForInput()
        time.sleep(3)
    elif u_t_input == "" or u_t_input.isdigit():
        Base.CleareConsole() # Чистим консоль
        Base.PrintTextWithImage(Base.GetString("get_e_task_1_text_error"), "img9")
        continue
    result = Functions.EasyTask_1(u_t_input)
    break


Base.CleareConsole() # Чистим консоль
Base.PrintArrWithImage(result, Base.GetString("get_e_task_1_text_result"), "img6")
Base.SetViewBlockForInput()
time.sleep(5)
# /Easy 1

# Easy 2
Base.CleareConsole() # Чистим консоль
Base.PrintTextWithImage(Base.GetString("get_e_task_2_text"), "img8")
Base.SetViewBlockForInput()
time.sleep(5)

Base.CleareConsole() # Чистим консоль
Base.PrintTextWithImage(Base.GetString("get_e_task_2_text_first"), "img1")

temp_arr = []
end_add_numbers = False

while True:
    u_t_input = Base.GetInputUsersText()
    if u_t_input == "0":
        Base.CleareConsole() # Чистим консоль
        Base.PrintTextWithImage(Base.GetString("get_e_task_2_text_end_null"), "img1")
        Base.SetViewBlockForInput()
        end_add_numbers = True
        time.sleep(3)
        break
    elif u_t_input.isdigit() or (len(u_t_input.split(".")) == 2 and u_t_input.split(".")[0].isdigit() and u_t_input.split(".")[1].isdigit()):
        temp_arr.append(float(u_t_input))
        break
    else:
        Base.CleareConsole() # Чистим консоль
        Base.PrintTextWithImage(Base.GetString("get_e_task_2_text_error"), "img9")
        continue

Base.PrintTextWithImage(Base.GetString("get_e_task_2_text_next"), "img1")
while True and end_add_numbers == False:
    u_t_input = Base.GetInputUsersText()
    if u_t_input == "0":
        Base.CleareConsole() # Чистим консоль
        Base.PrintTextWithImage(Base.GetString("get_e_task_2_text_end").format(Functions.EasyTask_2(temp_arr)), "img8")
        Base.SetViewBlockForInput()
        time.sleep(3)
        break
    elif u_t_input.isdigit() or (len(u_t_input.split(".")) == 2 and u_t_input.split(".")[0].isdigit() and u_t_input.split(".")[1].isdigit()):
        temp_arr.append(float(u_t_input))
        Base.CleareConsole() # Чистим консоль
        Base.PrintTextWithImage(Base.GetString("get_e_task_2_text_result").format(Functions.EasyTask_2(temp_arr)), "img3")
        Base.SetViewBlockForInput()
        time.sleep(3)
        Base.CleareConsole() # Чистим консоль
        Base.PrintTextWithImage(Base.GetString("get_e_task_2_text_next"), "img1")
        continue
    else:
        Base.CleareConsole() # Чистим консоль
        Base.PrintTextWithImage(Base.GetString("get_e_task_2_text_error"), "img9")
        continue


# /Easy 2

# Easy 3

Base.CleareConsole() # Чистим консоль
Base.PrintTextWithImage(Base.GetString("get_h_task_1_text"), "img8")
while True:
    u_t_input = Base.GetInputUsersText()
    if u_t_input.isdigit():
        pass
    else:
        pass


# /Easy 3

# Hard 1

temp_variant = "-1"
Base.CleareConsole() # Чистим консоль
Base.PrintTextWithImage(Base.GetString("get_h_task_1_text"), "img8")
while True:
    u_t_input = Base.GetInputUsersText()

    if u_t_input == Base.GetString("get_h_task_1_variant_1"):
        temp_variant = "1"
        break
    elif u_t_input == Base.GetString("get_h_task_1_variant_2"):
        temp_variant = "2"
        break
    else:
        Base.CleareConsole() # Чистим консоль
        Base.PrintTextWithImage(Base.GetString("get_h_task_1_text_error"), "img9")
        continue

if temp_variant == "1":
    last_num = None
    hidden_number = random.randint(1, 101)
    
    temp_counter = 0

    Base.CleareConsole() # Чистим консоль
    Base.PrintTextWithImage(Base.GetString("get_h_task_1_text_variant_1"), "img1")
    while True:
        u_t_input = Base.GetInputUsersText()
        if u_t_input.lower() in Base.GetInStringArr("arr_no"):
            Base.CleareConsole() # Чистим консоль
            Base.PrintTextWithImage(Base.GetString("get_h_task_2_text_end_null"), "img7")
            Base.SetViewBlockForInput()
            time.sleep(3)
            break
        elif u_t_input.isdigit():
            temp_num = int(u_t_input)
            temp_counter += 1
            Base.CleareConsole()
            if hidden_number == temp_num:
                Base.PrintTextWithImage(Base.GetString("get_h_task_1_result_v1").format(hidden_numbe, temp_counter), "img5")
                Base.SetViewBlockForInput()
                time.sleep(5)
                break
            else:
                Base.PrintTextWithImage(Base.GetString("answer_h_task_1_{}".format(Functions.HardTask_1_v1(hidden_number, temp_num, last_num))), "img1")
                last_num = temp_num
                continue
        else:
            Base.CleareConsole() # Чистим консоль
            Base.PrintTextWithImage(Base.GetString("get_h_task_1_text_error_num"), "img9")
elif temp_variant == "2":
    Base.CleareConsole() # Чистим консоль
    Base.PrintTextWithImage(Base.GetString("get_h_task_1_text_variant_2"), "img3")
    Base.SetViewBlockForInput()
    time.sleep(8)
    
    temp_num_min = 0
    temp_num_max = 101
    temp_num = random.randint(temp_num_min, temp_num_max)
    last_num = None
    last_type = None
    
    Base.CleareConsole() # Чистим консоль
    Base.PrintTextWithImage(Base.GetString("ansver_h_task_1_result_v2").format(temp_num), "img3")

    temp_counter = 1
    temp_arr_result = Base.GetInStringArr("ansver_h_task_1_v2")
    while True:
        u_t_input = Base.GetInputUsersText()
        if u_t_input.lower() in Base.GetInStringArr("arr_yes"):
            Base.CleareConsole() # Чистим консоль
            Base.PrintTextWithImage(Base.GetString("get_h_task_1_result_v2").format(temp_num, temp_counter), "img9")
            Base.SetViewBlockForInput()
            time.sleep(5)
            break
        elif u_t_input.lower() in Base.GetInStringArr("arr_no"):
            Base.CleareConsole() # Чистим консоль
            Base.PrintTextWithImage(Base.GetString("get_h_task_2_text_end_null"), "img7")
            Base.SetViewBlockForInput()
            time.sleep(3)
            break
        elif u_t_input in temp_arr_result:
            if last_num != None and u_t_input != last_type:
                temp_arr = Functions.HardTask_1_v2(temp_arr_result, [u_t_input, last_type], [temp_num, last_num], [temp_num_min, temp_num_max])
                temp_num_min = temp_arr[0]
                temp_num_max = temp_arr[1]

            last_type = u_t_input
            last_num = temp_num
            temp_num = random.randint(temp_num_min, temp_num_max)
            temp_counter += 1

            Base.CleareConsole() # Чистим консоль
            Base.PrintTextWithImage(Base.GetString("ansver_h_task_1_result_v2").format(temp_num), "img3")
            continue
        else:
            Base.CleareConsole() # Чистим консоль
            Base.PrintTextWithImage(Base.GetString("get_h_task_1_text_error_proximity"), "img9")
            continue


    

# /Hard 1

# Hard 2

temp_variant = "-1"
Base.CleareConsole() # Чистим консоль
if user_data["first_name"] == "Нуриддин":
    Base.PrintTextWithImage(Base.GetString("get_h_task_2_text").format(Base.GetString("get_h_task_2_text_condition")), "img4")
else:
    Base.PrintTextWithImage(Base.GetString("get_h_task_2_text").format(""), "img8")
while True:
    u_t_input = Base.GetInputUsersText()
    if u_t_input in ["1", "2"]:
        temp_variant = u_t_input
        break
    
    Base.CleareConsole()
    Base.PrintTextWithImage(Base.GetString("get_h_task_2_text_variant_error"), "img9")
    continue


Base.CleareConsole()
if temp_variant == "1":
    Base.PrintTextWithImage(Base.GetString("get_h_task_2_text_variant_1"), "img1")
elif temp_variant == "2":
    Base.PrintTextWithImage(Base.GetString("get_h_task_2_text_variant_2"), "img1")

u_t_input = Base.GetInputUsersText()

temp_result = Functions.HardTask_2(u_t_input, temp_variant)

Base.CleareConsole()
Base.PrintTextWithImage(Base.GetString("get_h_task_2_text_result").format(temp_result), "img1")
Base.SetViewBlockForInput()
time.sleep(5)


# /Hard 2


# End

Base.CleareConsole()
Base.PrintTextWithImage(Base.GetString("get_end_text").format(temp_result), "img5")
Base.SetViewBlockForInput()
time.sleep(10)

Base.CleareConsole()
Base.PrintTextWithImage("Как же я запарился все это делать, бошка болит", "img11")
Base.SetViewBlockForInput()

# /End