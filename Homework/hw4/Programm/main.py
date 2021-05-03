from functions import *

StartTelegram()

# Теперь у меня собственный Телеграм )

# 1

while True:
    SendBotText("Введите число для возведения в куб:")
    num = Core.USER_INPUT
    if num.isdigit():
        num = int(num)
        print("Это число в кубе: ", kub(num))
        break
    else:
        SendBotText("Неправельно ввели число")

