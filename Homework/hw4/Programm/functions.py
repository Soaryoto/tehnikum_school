from PySide2 import QtWidgets
from PySide2.QtWidgets import QListWidgetItem
import sys
from ui import Ui_Form
import core as Core

# Это функции для UI

def StartTelegram():
    APP = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    Core.UI = Ui_Form()
    Core.UI.setupUi(Form)
    Form.show()
    Core.UI.pushButton.clicked.connect(SendUserText)

    sys.exit(APP.exec_())

def SendUserText():
    Core.USER_INPUT = Core.UI.lineEdit.text()
    Core.UI.lineEdit.setText("")
    item = QListWidgetItem("Вы: " + str(Core.USER_INPUT))
    Core.UI.listWidget.addItem(item)

def SendBotText(text):
    item = QListWidgetItem("Бот: " + text)
    Core.UI.listWidget.addItem(item)


# А это функции для дз

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

# 5

def IsHighAxleYear(year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return False
    return True

# 6

def TakeCount(num):
    num1 = num % 10
    num2 = ((num - (num % 10)) // 10)
    print(str(num2) + " десяток(ов)")
    print(str(num1) + " единиц(а)")