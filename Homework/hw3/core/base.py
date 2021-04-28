import core.localization as Localization
import core.image as Images
import os
import ctypes
import msvcrt
import subprocess

from ctypes import wintypes

global_local = "ru"

# Нашел функцию здесь https://stackoverflow.com/questions/43959168/python-console-fullscreen-maybe-using-os-system
def FullScreen(lines=None):
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    user32 = ctypes.WinDLL('user32', use_last_error=True)

    SW_MAXIMIZE = 3

    kernel32.GetConsoleWindow.restype = wintypes.HWND
    kernel32.GetLargestConsoleWindowSize.restype = wintypes._COORD
    kernel32.GetLargestConsoleWindowSize.argtypes = (wintypes.HANDLE,)
    user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)
    fd = os.open('CONOUT$', os.O_RDWR)
    try:
        hCon = msvcrt.get_osfhandle(fd)
        max_size = kernel32.GetLargestConsoleWindowSize(hCon)
        if max_size.X == 0 and max_size.Y == 0:
            raise ctypes.WinError(ctypes.get_last_error())
    finally:
        os.close(fd)
    cols = max_size.X
    hWnd = kernel32.GetConsoleWindow()
    if cols and hWnd:
        if lines is None:
            lines = max_size.Y
        else:
            lines = max(min(lines, 9999), max_size.Y)
        subprocess.check_call('mode.com con cols={} lines={}'.format(
                                cols, lines))
        user32.ShowWindow(hWnd, SW_MAXIMIZE)



def CleareConsole():
    os.system('cls')

def GetWidthConsole():
    return os.get_terminal_size().columns

def GetHeightConsole():
    return os.get_terminal_size().lines

def GetInputUsersText():
    print("_" * GetWidthConsole())
    return input(Localization.data.get(global_local).get("You") + ": ")

def SetViewBlockForInput():
    print("_" * GetWidthConsole())

def PrintTextWithImage(text, image_name):
    result = ""
    
    full_width = GetWidthConsole()
    full_height = GetHeightConsole()

    img_width = 0
    img_height = 0

    if image_name == "img1":
        result = Images.img1["view"]
        img_width = Images.img1["width"]
        img_height = Images.img1["height"]
    elif image_name == "img2":
        result = Images.img2["view"]
        img_width = Images.img2["width"]
        img_height = Images.img2["height"]
    elif image_name == "img3":
        result = Images.img3["view"]
        img_width = Images.img3["width"]
        img_height = Images.img3["height"]
    elif image_name == "img4":
        result = Images.img4["view"]
        img_width = Images.img4["width"]
        img_height = Images.img4["height"]
    elif image_name == "img5":
        result = Images.img5["view"]
        img_width = Images.img5["width"]
        img_height = Images.img5["height"]
    else:
        result = ""
 
    # Вариант 1
    #    ┌─────────────────────┐
    #   /  Привет, как дела ?  │
    #  /   Сегодня отличный    │
    # /    день чтобы погулять │
    # ─────────────────────────┘
    # h_m = 5
    # w_m = 5
    # 
    # Вариант 2
    #    ┌─────────────────────┐
    #   /  Привет, как дела ?  │
    #  /   Сегодня отличный    │
    # /    день чтобы погулять │
    # ───┐                     │
    #    │                     │
    #    │                     │
    #    └─────────────────────┘

    # Параметры рамкм для отступа текста
    text_frame_width = 6
    text_frame_height = 2

    # Максимальные параметры для текста
    text_width = full_width - img_width - text_frame_width - 20
    text_height = full_height - img_height - text_frame_height
    text_count_lines = 0
    
    temp_text = ""
    arr_linese_text = []
    for word in text.split(" "):

        if word == "":
            continue

        if temp_text == "":
            temp_text = word
        else:
            if len(temp_text + " " + word) > text_width:
                arr_linese_text.append(temp_text)
                temp_text = word
            else:
                temp_text += " " + word
    arr_linese_text.append(temp_text)

    text_count_lines = len(arr_linese_text)

    #Редактирую строки чтоб не было более легче и не было ошибок
        
    if text_count_lines <= 3:
        if text_count_lines == 1:
            arr_linese_text.append(" " * text_width)
            arr_linese_text.append(" " * text_width)
            text_count_lines = 3
        elif text_count_lines == 2:
            arr_linese_text.append(" " * text_width)
            text_count_lines = 3

    for index in range(text_count_lines):
        arr_linese_text[index] += " " * (text_width - len(arr_linese_text[index]))

            

    
    # Выбор вариант рамки из-за количество строк
    temp_arr = []
    if text_count_lines == 3:
        temp_arr = result.split("\n")
        temp_arr[text_frame_height] += "    ┌" + ("─" * (text_width + 1)) + "┐"
        temp_arr[text_frame_height + 1] += "   / " + arr_linese_text[0] + " │"
        temp_arr[text_frame_height + 2] += "  /  " + arr_linese_text[1] + " │"
        temp_arr[text_frame_height + 3] += " /   " + arr_linese_text[2] + " │"
        temp_arr[text_frame_height + 4] += ("─" * (text_width + 6)) + "┘"
        
    else:
        temp_arr = result.split("\n")
        temp_arr[text_frame_height] +=     "    ┌" + ("─" * (text_width + 2)) +  "┐"
        temp_arr[text_frame_height + 1] += "   /  " + arr_linese_text[0] +      " │"
        temp_arr[text_frame_height + 2] += "  /   " + arr_linese_text[1] +      " │"
        temp_arr[text_frame_height + 3] += " /    " + arr_linese_text[2] +      " │"
        temp_counter = text_frame_height + 4
        for index in range(3, len(arr_linese_text)):
            if temp_counter == text_frame_height + 4:
                temp_arr[temp_counter] +=  " ───┐ " + arr_linese_text[index] + " │"
            else:
                temp_arr[temp_counter] +=  "    │ " + arr_linese_text[index] + " │"
            temp_counter += 1
        
        temp_arr[temp_counter] +=          "    └" + ("─" * (text_width + 2)) + "┘"

        
    while len(temp_arr) < full_height - 2:
        temp_arr.append(" ")

    
    result = "\n".join(temp_arr)

    print(result)

    