# 1
def kub(a):
    return a**3


# 2
def GetMonthSeason(month_num):
    arr = {"Зима" : [12, 1, 2], "Весна" : [3, 4, 5], "Лето" : [6, 7 ,8], "Осень" : [9, 10, 11]}
    for key in arr:
        if month_num in arr[key]:
            return key


# 3

def GetFinalСontribution(sum, years):
    procent = 0.1
    result = (sum * procent) * years + sum
    return result


# 4

def IsSimpleNum(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

