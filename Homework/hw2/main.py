# Dumbrovskiy Danila

# Задание 1 сумма числе от 1 до 100 while
result = 0
counter = 1
while counter <= 100:
    result += counter
    counter += 1


print()
print("Первое задание сложить числа от 1 до 100. Вот и получается {}".format(result))

# /Задание 1

# Задание 2
result = 0
counter = 1
while counter <= 14:
    num = 1
    while num <= counter:
        result += num
        num += 1
    counter += 1

#print(counter)

print()
print("Задача на сумму числового ряда до 14, получается {}".format(result))

# /Задание 2

# Задача 2 advenced

print()
print("Так, теперь вы сами можете выбрать количесво числовых рядов (выход = 0):")
while True:
    u_n = input("Вы: ")
    if u_n.isdigit() and  u_n != "0":
        result = 0
        counter = 1
        while counter <= int(u_n):
            result += sum(range(counter + 1))
            counter += 1
        print("Вот ваш ответ: {}".format(result))
        break
    elif u_n == "0":
        break
    else:
        print("Вы не правельно ввели параметр")

# /Задача 2 advenced

# Задача 3

funct = ["+", "-", "/", "*", "0"]
funct_text = ""
num_1 = 0
num_2 = 0
take_u_num = True
ask_u_take_last_num = True
funct_end_counter = 0
u_a_yes = ["да", "yes", "конечно", "угу"]

print()
print("Это последнее задание, калькулятор двух чисел)")
print("Умеет находить сумму(+), разность(-), произведение(*), частное(/) или же выйти(0)")
print("Хотите продолжить?")
u_t = input("Вы: ")
if u_t.strip().lower() in u_a_yes:
    while True:
        u_t = input("Действие: ")
        if u_t.strip().lower() in funct and u_t.strip().lower() != funct[-1]:
            funct_text = u_t.strip().lower()
            if ask_u_take_last_num and funct_end_counter > 0:
                u_t = input("Хотите использовать прошлые числа? Чтобы не повторял вопрос введите 'Никогда': ")
                if u_t.strip().lower() in u_a_yes:
                    print("Хорошо возму прошлые числа")
                    take_u_num = False
                elif u_t.strip().lower() == "никогда":
                    ask_u_take_last_num = False
                else:
                    print("Ок")
            
            while take_u_num:
                print("Введите число или 2 числа через пробел:")
                u_t = input("Вы: ")
                if len(u_t.split(" ")) == 2:
                    temp_arr = u_t.split(" ")
                    valid_1_num = temp_arr[0].isdigit() or (temp_arr[0].split(".")[0].isdigit() and temp_arr[0].split(".")[1].isdigit())
                    valid_2_num = temp_arr[0].isdigit() or (temp_arr[0].split(".")[0].isdigit() and temp_arr[0].split(".")[1].isdigit())
                    if valid_1_num and valid_2_num:
                        num_1 = float(temp_arr[0])
                        num_2 = float(temp_arr[1])
                        break
                    else:
                        print("Вы непрвельно ввели числа")
                        continue
                elif u_t.isdigit() or (u_t.split(".")[0].isdigit() and u_t.split(".")[1].isdigit()):
                    num_1 = float(u_t)
                    print("Окей, введите 2-ое число")
                    while True:
                        u_t = input("Вы: ")
                        if u_t.isdigit() or (u_t.split(".")[0].isdigit() and u_t.split(".")[1].isdigit()):
                            num_2 = float(u_t)
                            break
                        else:
                            print("Неправельно ввели")
                    break
                else:
                    print("Вы что-то неправильно ввели")
                    continue
            
            if funct_text == funct[0]: # +
                print("{} + {} = {}".format(num_1, num_2, num_1 + num_2))
            elif  funct_text == funct[1]: # -
                print("{} - {} = {}".format(num_1, num_2, num_1 - num_2))
            elif  funct_text == funct[2]: # /
                print("{} / {} = {}".format(num_1, num_2, num_1 / num_2))
            elif  funct_text == funct[3]: # *
                print("{} * {} = {}".format(num_1, num_2, num_1 * num_2))

            funct_end_counter += 1
        elif u_t.lower() == funct[-1]:
            print("До скорого)")
            break
        else:
            print("Вы неправельно ввели действие")

print("Всего {} пример(ов) сделали".format(funct_end_counter))

# /Задача 3