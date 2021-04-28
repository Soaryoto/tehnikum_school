# Функции выполняющие задания ДЗ


def EasyTask_1(text):
    arr = text.split(" ")
    # ооо, а я то не могу вывести обычным способои, ладно просто функцию выполню и все
    print_text = ""
    i = 0
    while i < len(arr):
        print_text = arr[i] # место print(arr[i])
        i += 1
    
    return arr

def EasyTask_2(arr_input_user):
    return sum(arr_input_user) # незнаю почему я вывел в функцию
