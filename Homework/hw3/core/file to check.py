# Файл со всеми функциями из дз для запуска в онлайн компиляторах

# Базовые задачи

# Задача 1. “Pretty Print”
text = input("Введите предложение для массива: ")
arr = text.split(" ")
i = 0
while i < len(arr):
    print(arr[i])
    i += 1
    

# Задача 2. “Ввод-вывод”
arr = []
while True:
    num1 = input("Введите первое число: ")
    if num1 == "0":
        print("Значит не хотите вводить числа")
    elif num1.isdigit():
        arr.append(int(num1))
        while True:
            num2 = input("Введите следующее число: ")
            if num2 == "0":
                print("Хорошо, закончим. Сумма чисел равна {}".format(sum(arr)))
                break
            elif num2.isdigit():
                arr.append(int(num2))
                print("Сумма равна {}".format(sum(arr)))
            else:
                print("Неправельно ввели число")

    else:
        print("Неправельно ввели число")
    break

# Задача 3. “Килограмм асфальта”
while True:
    num1 = input("Введите стоимость асфальта: ")
    elif num1.isdigit():
        print(num1[::-1])
        break
    else:
        print("Неправельно ввели стоимость")


# Задача 4. “Power rangers”
text = input("Введите строку: ")
print(text[3:4]) # Первая строка
print(text[-2]) # Вторая строка
print(text[0:6]) # Третья строка
print(text[0:len(text) - 3]) # Четвертая строка

temp_text = ""
for i in range(1, len(text), 2):
    temp_text += text[i]
print(temp_text) # Пятая строка

temp_text = ""
for i in range(0, len(text), 2):
    temp_text += text[i]
print(temp_text) # Шестая строка

print(text[::-1]) # Седьмая строка

print(text[::-2]) # Восьмая строка
print(len(text)) # Восьмая строка


# Задача 5. “Без if’a”
text = input("Введите преддложение из 2 слов: ")
arr = text.split(" ")
print(arr[1], arr[0])


# Средние задачи

# Задача 1. “Калькулятор”

funct = ["+", "-", "/", "*"]
num_1 = 0
num_2 = 0
print("Калькулятор сумма(+), разность(-), произведение(*), частное(/) или же выйти(0)")

while True:
    t_funct = input("Действие:")
    if t_funct == "0":
        print("Калькулятор закончил работу")
        break
    if t_funct in funct:
        while True:
            t_num1 = input("Введите первое число: ")
            if t_num1.isdigit():
                num_1 = int(t_num1)
                while True:
                    t_num2 = input("Введите второе число: ")
                    if t_num2 == "0" and t_funct == funct[2]:
                        print("На 0 делить нельзя")
                        continue
                    elif t_num2.isdigit():
                        num_2 = int(t_num2)

                        if t_funct == funct[0]:
                            print("{} + {} = {}".format(num_1, num_2, num_1 + num_2))
                        elif t_funct == funct[1]:
                            print("{} - {} = {}".format(num_1, num_2, num_1 - num_2))
                        elif t_funct == funct[2]:
                            print("{} / {} = {}".format(num_1, num_2, num_1 / num_2))
                        elif t_funct == funct[3]:
                            print("{} * {} = {}".format(num_1, num_2, num_1 * num_2))
                    else:
                        print("Вы неправельно ввели число")
                        continue
                    break
            else:
                print("Вы неправельно ввели число")
                continue
            break
    else:
        print("Неправельно ввели действие")


# Задача 2. “Матемагия”
num = -1
print("Введите натуральное число:")
while True:
    num = input("n = ")
    if num.isdigit():
        num = int(num)
        break
    else:
        print("Yеправильно ввели число")

num_1 = 0
for i in range(1, num + 1):
    num_1 += i

num_2 = num * (num + 1) / 2

if num_1 == num_2:
    print("Они равны {}, {}".format(num_1, num_2))
else:
    print("Они не равны {}, {}".format(num_1, num_2))


# Задача 3. “Удаление элемента”

text = input("Введите список чисел через пробел: ")
arr = text.split(" ")
num = ""
while True:
    num = input("Введите индекс элемента для удаления: ")
    if num.isdigit():
        num = int(num)
        break
    else:
        print("Неправельно ввели индекс")
del_text = arr[num]
for i in range(num + 1, len(arr)):
    arr[i - 1] = arr[i]
arr[len(arr) - 1] = del_text
arr.pop()
print(arr)



# Конкурсные задачи

# Задача 1*. “Две желтые летающие овцы”
import random
print("Я буду Бобой и загадаю тебе число от 1 до 100, а ты Бибой который отгадывает")
rand_num = random.randint(1, 101)
last_num = 0
while True:
    u_t_input = input("Отгадайте число: ")
    if u_t_input.isdigit():
        num = int(u_t_input)
        if num == rand_num:
            print("Отлично, вы угадали число {}".format(rand_num))
            break
        result = ""
        temp_num = rand_num - num
        if -3 <= temp_num <= 3:
            if last_num != None:
                if rand_num < last_num < num or rand_num > last_num > num:
                    result = "Прохладно"
                else:
                    result = "Жарко"
            else:
                result = "Жарко"
        elif (temp_num > 3 or temp_num < -3) and (-10 <= temp_num <= 10):
            if last_num != None:
                if rand_num < last_num < num or rand_num > last_num > num:
                    result = "Холодно"
                else:
                    result = "Тепло"
            else:
                result = "Тепло"
        else:
            result = "Холодно"
            
        print(result)
    else:
        print("Вы неправельно ввели число")


# Задача 2*. “Ленивый Нуриддин”

print("Требуется сжать убрав дубликаты(1) или все нули байтов перенести в конец(2)")
while True:
    var = input("Выберите вариант:")
    if var in ["1", "2"]:
        break
if var == "1":
    text = input("Введите текст для сжатия:")#"Ппривет как деееела у тебяяя?"
    result = ""
    for word in text.split(" "):
        temp_char_counter = 0
        temp_save_char = ""
        for char in word:
            if temp_save_char == char or temp_save_char == "":
                temp_save_char = char
                temp_char_counter += 1
            else:
                if temp_char_counter <= 1:
                    result += str(temp_save_char)
                else:
                    result += str(temp_char_counter) + temp_save_char
                temp_save_char = char
                temp_char_counter = 1
        
        if temp_char_counter <= 1:
            result += temp_save_char
        else:
            result += str(temp_char_counter) + temp_save_char

        result += " "
    print(result)
elif var == "2":
    text = input("Введите байты через пробел:")#"12 0 24 231 42 32 0 213 23 0 1"
    temp_arr = text.split(" ")
    for index in range(0, len(temp_arr)):
        if temp_arr[index] == "0":
            temp_arr.append(temp_arr.pop(index))

    print(temp_arr)
        