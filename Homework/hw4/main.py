from functions import *

# 1


while True:
    num = input("Введите число для возведения в куб: ")
    if num.isdigit():
        num = int(num)
        print("Это число в кубе: ", kub(num))
        break
    else:
        print("Неправельно ввели число")


# 2

while True:
    num = input("Введите число месяца: ")
    if num.isdigit():
        num = int(num)
        if 0 < num < 13:
            print("Сезон этого месяца: ", GetMonthSeason(num))
            break
        else:
            print("Вы ввели несуществующий месяц")
    else:
        print("Неправельно ввели число")


# 3

while True:
    sum_num = input("Введите сумму вклада: ")
    if sum_num.isdigit():
        sum_num = int(sum_num)
        years = input("На сколько лет вы вкладываете: ")
        if years.isdigit():
            years = int(years)
            print("В итоге получится: {}$".format(GetFinalСontribution(sum_num, years)))
            break
        else:
            print("Неправельно ввели число")
    else:
        print("Неправельно ввели число")

# 4

while True:
    num = input("Введите число на проверку простаты(-1 выйти): ")
    if num == "-1":
        break
    elif num.isdigit():
        num = int(num)
        if IsSimpleNum(num):
            print("Это число является простым")

        else:
            print("Это число не является простым")
    else:
        print("Неправельно ввели число")