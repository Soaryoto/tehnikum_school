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



def HardTask_1_v1(hidden_number, num, last_num):
    result = ""
    temp_num = hidden_number - num
    if -3 <= temp_num <= 3:
        if last_num != None:
            if hidden_number < last_num < num or hidden_number > last_num > num:
                result = "cool"
            else:
                result = "hot"
        else:
            result = "hot"
    elif (temp_num > 3 or temp_num < -3) and (-10 <= temp_num <= 10):
        if last_num != None:
            if hidden_number < last_num < num or hidden_number > last_num > num:
                result = "cold"
            else:
                result = "heat"
        else:
            result = "heat"
    else:
        result = "cold"
        
    return result


def HardTask_1_v2(arr_result, types, numbers, range_num):
    result = range_num
    if types[0] == arr_result[0] and types[1] == arr_result[1]:
        if numbers[0] > numbers[1]:
            result[1] = numbers[0]
        else:
            result[0] = numbers[0]
    elif types[0] == arr_result[1] and types[1] == arr_result[0]:
        if numbers[0] > numbers[1]:
            result[0] = numbers[1]
        else:
            result[1] = numbers[1]
    return result


def HardTask_2(text, variant):
    result = None
    
    if variant == "1":
        result = ""
        for word in text.split(" "):
            temp_char_counter = 0
            temp_save_char = ""
            for char in word:
                print(char)
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

    elif variant == "2":
        result = ""
        temp_arr = text.split(" ")
        for index in range(0, len(temp_arr)):
            if temp_arr[index] == "0":
                temp_arr.append(temp_arr.pop(index))        
        result = " ".join(temp_arr)
    
    return result