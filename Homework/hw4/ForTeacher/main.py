
# 1
def kub(a):
    return a**3


while True:
    num = input("Введите число для возведения в куб: ")
    if num.isdigit():
        num = int(num)
        print("Это число в кубе: ", kub(num))
        break
    else:
        print("Неправельно ввели число")



# 2
def GetMonthSeason(month_num):
    arr = {"Зима" : [12, 1, 2], "Весна" : [3, 4, 5], "Лето" : [6, 7 ,8], "Осень" : [9, 10, 11]}
    for key in arr:
        if month_num in arr[key]:
            return key

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

def GetFinalСontribution(sum, years):
    procent = 0.1
    result = (sum * procent) * years + sum
    return result


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

def IsSimpleNum(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


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

# 5

def IsHighAxleYear(year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return False
    return True


while True:
    num = input("Введите год на проверку высокосности(-1 выйти): ")
    if num == "-1":
        break
    elif num.isdigit():
        if IsHighAxleYear(int(num)):
            print("Этот год высокосный")
        else:
            print("Этот год обычный")
    else:
        print("Неправильно ввели год")


# 6

def TakeCount(num):
    num1 = num % 10
    num2 = ((num - (num % 10)) // 10)
    print(str(num2) + " десяток(ов)")
    print(str(num1) + " единиц(а)")

while True:
    print("Впишите число состоящие из двух цыфр и я разделю на классы: ")
    num = input()
    if num.isdigit() and len(num) == 2:
        TakeCount(int(num))
        break
    else:
        print("Неправельно вы ввели число")


