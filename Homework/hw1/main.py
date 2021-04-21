from random import randint
# Напечатал Danila Dumbrovskiy Ivanovich

# Простые переменки нужные для процесса

g_u_answer = ["да", "yes", "ok", "ок", "конечно"]
g_u_answer_no = ["нет", "no"]
b_indicator_dullness = 0
g_u_i = "Вы: "

img = ''',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,r,:,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,,,,@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,,,,,:@@:,,@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,,,,:M@@@,,,,::@M,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,,,:@@@:,,,,,,:,,:2@@@@@H:,,,,,,,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,@@9:,,,,,,,,,,,,,,,,,,,,S@@@i,,,,,,,,,,,,,,,,,,,,
,,,A@@r,,,,,:@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,:@@@,,,,,,,,,,,,,,,,,
,@@,,,r@@,;@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,#@@:,,,,,,,,B2,,,
@@,:s,i;@@@:,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,:@@:,,X@@BM@,,,
@:r:ss;:,HM:,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@@H:,,,@@,,,
@,,ssis:,,,,,,,,,,X@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,@;,,,
@:,:rr,,,,,,,,,,,:@@@:,,@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,&B,,,,
@,,,,,,,,,,,,,,,,,,,:,,r@:,@#:,,,,,,,,,,,,,,,2@@X,,,,,,,,,,@,,,,
@G,,,,,,,,,,,,,,,,,,,,,,:GBA@A@@,,,,,,,,,,,A@;,,r@@,,,,,,,s@,,,,
G@@@@@B;,,,,,,,,,,,,,,,,,,,,,:::,,,,,,#@H,;@:,s:rs@@,,,,,,#@,,,,
,,,,,,:5@@@@@@S,,,,,,,,,,,,,,,,,,,,,,,@@@,@3r;;ir:,G&,,,,:@@:,,,
,,,,,,,,,,,,,,s@@@@@@3::,,,,,,,,,,,,,,,,,:@:,:siis,,s:,,,,,;@;,,
,,,,,,,,,,,,,,,,,,,::G@@@@@#:,,,,,,,,,,,,:@;,,;sr,,,,,,,,,,,r@:,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,5@@@@@@X,,,,,,@X,,,,,,,,,,,,,,,,,@@,
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,rM@@@@@G:,,,,,,,,,,,,,,,,,,@:
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,G@@@@@@;,,,,,,,,,,,@3
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,5@@@@@@5,,,,,@M
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,sA@@@@@M
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'''

# Вступлени

print(img)
print()
print("Привет, сегодня я буду работать с текстом который вы будете мне давать")
print()

# /Вступление

# Задание 1 - без разници, есть такое слово или нет

    
print("Напиши мне буквы через пробел, а я тебе из него сделаю предложение: ")
u_t_sentence_for_new_sentence = input(g_u_i)

temp_arr = u_t_sentence_for_new_sentence.split(" ")

# Далее временные переменные для чисел
a = temp_arr[0]
b = temp_arr[int(len(temp_arr) /2)]
c = temp_arr[int(len(temp_arr) / 4 + len(temp_arr) / 2)]
d = temp_arr[len(temp_arr) -1]
i = temp_arr[int(len(temp_arr) / 4)]

print()
print("Я создал новые слова: ",(d+i+c+b+a+d).capitalize(), c+d+a+i)

print("Во, я самый грамотный бот на свете")

# /Задание 1 - Что там дальше?

# Задание 1.5 - это моё задание, дополнение
print()
print("У меня есть некая база знаний слов, хочешь узнать какие слова подойдут под эти буквы ?")
u_t_sentence_for_new_sentence = input(g_u_i)

if u_t_sentence_for_new_sentence.lower() in g_u_answer:
    b_notable_words = ["привет", "как", "дела", "лол", "магия", "прогер", "автоэлектростеклоподъемник"]
    b_answer_q_1_5 = ""

    temp_t = b_notable_words[0] # В условии не хочу использовать длинную переменную
    if temp_t[0] in temp_arr and temp_t[1] in temp_arr and temp_t[2] in temp_arr and temp_t[3] in temp_arr and temp_t[4] in temp_arr and temp_t[5] in temp_arr:
        b_answer_q_1_5 = b_answer_q_1_5 + temp_t

    temp_t = b_notable_words[1]
    if temp_t[0] in temp_arr and temp_t[1] in temp_arr:
        if b_answer_q_1_5 == "":
            b_answer_q_1_5 = b_answer_q_1_5 + temp_t
        else:
            b_answer_q_1_5 = b_answer_q_1_5 + " " + temp_t
        
    temp_t = b_notable_words[2]
    if temp_t[0] in temp_arr and temp_t[1] in temp_arr and temp_t[2] in temp_arr and temp_t[3] in temp_arr:
        if b_answer_q_1_5 == "":
            b_answer_q_1_5 = b_answer_q_1_5 + temp_t
        else:
            b_answer_q_1_5 = b_answer_q_1_5 + " " + temp_t

    temp_t = b_notable_words[3]
    if temp_t[0] in temp_arr and temp_t[1] in temp_arr:
        if b_answer_q_1_5 == "":
            b_answer_q_1_5 = b_answer_q_1_5 + temp_t
        else:
            b_answer_q_1_5 = b_answer_q_1_5 + " " + temp_t
        
    temp_t = b_notable_words[4]
    if temp_t[0] in temp_arr and temp_t[1] in temp_arr and temp_t[2] in temp_arr and temp_t[3] in temp_arr and temp_t[4] in temp_arr:
        if b_answer_q_1_5 == "":
            b_answer_q_1_5 = b_answer_q_1_5 + temp_t
        else:
            b_answer_q_1_5 = b_answer_q_1_5 + " " + temp_t

    temp_t = b_notable_words[5]
    if temp_t[0] in temp_arr and temp_t[1] in temp_arr and temp_t[2] in temp_arr and temp_t[3] in temp_arr and temp_t[4] in temp_arr and temp_t[5] in temp_arr:
        if b_answer_q_1_5 == "":
            b_answer_q_1_5 = b_answer_q_1_5 + temp_t
        else:
            b_answer_q_1_5 = b_answer_q_1_5 + " " + temp_t

    if b_answer_q_1_5 == "":
        print("Ой, я не знаю ни одного слово из этих букв")
    elif len(b_answer_q_1_5.split(" ")) == 1:
        print("Я знаю только одно слово '{}' из этих букв".format(b_answer_q_1_5))
    else:
        print("Отлично я знаю парочку слов: ", b_answer_q_1_5)
else:
    print("Не хочешь как хочешь")
    b_indicator_dullness = b_indicator_dullness + 1
# /Задание 1.5

# Задание 2 - Ща сделаем

print()
print("Сейчас я буду пытаться заменить часть строки в предложении")
print("Введите предложение: ")
u_t_sentence_for_replase = input(g_u_i)

print("Какое словы вы хотите заменить?")
u_t_world_for_replase = input(g_u_i)

print("А на что вы хотите заменить?")
u_t_world_to_replase = input(g_u_i)

print()
bot_t_answer_for_replase = "Я заменил слово, и теперь получилось такое предложение :\n{}"
print(
    bot_t_answer_for_replase.format(
            u_t_sentence_for_replase.replace(u_t_world_for_replase, u_t_world_to_replase)
        )
    )


# /Задание 2 - кончилось

# Задание 2.534233412

print()
print("Хм, хочешь тоже попробовать менять слова в предложении?")
u_t_sentence_for_new_sentence = input(g_u_i)

b_list_tasks = [
    ["а", "a) ", "Сегодня самый ясный день(нет)", "ясный", "пасмурный"],
    ["б", "б) ", "Много я сегодня написал, но забыл сдать", "но забыл", "и"],
    ["в", "в) ", "Вчера я узнал очень мало", "мало", "много"],
    ["г", "г) ", "Завтра я начну работать", "Завтра", "Сегодня"]
]

u_selected_option = -1

if u_t_sentence_for_new_sentence.lower() in g_u_answer:
    print("Отлично, теперь выбери предложение: ")
    print(b_list_tasks[0][1],b_list_tasks[0][2])
    print(b_list_tasks[1][1],b_list_tasks[1][2])
    print(b_list_tasks[2][1],b_list_tasks[2][2])
    print(b_list_tasks[3][1],b_list_tasks[3][2])

    print()
    u_t_sentence_for_new_sentence = input(g_u_i)

    if u_t_sentence_for_new_sentence == b_list_tasks[0][0]:
        u_selected_option = 0
    elif  u_t_sentence_for_new_sentence == b_list_tasks[1][0]:
        u_selected_option = 1
    elif  u_t_sentence_for_new_sentence == b_list_tasks[2][0]:
        u_selected_option = 2
    elif  u_t_sentence_for_new_sentence == b_list_tasks[3][0]:
        u_selected_option = 3
        
    if u_selected_option == -1:
        print("Ой, ты выбрать какой-то странный вариант, у меня таких нет. Пока придётся пропускать")
    else:
        print("Хорошо, теперь замени слово '{}' на '{}', а я проверю)".format(b_list_tasks[u_selected_option][3], b_list_tasks[u_selected_option][4]))
        u_t_sentence_for_new_sentence = input(g_u_i)
        if u_t_sentence_for_new_sentence == b_list_tasks[u_selected_option][2].replace(b_list_tasks[u_selected_option][3], b_list_tasks[u_selected_option][4]):
            print("Вы отлично справились )")
        else:
            print("У тебя ошибочка) Должно было получится '{}'".format(b_list_tasks[u_selected_option][2].replace(b_list_tasks[u_selected_option][3], b_list_tasks[u_selected_option][4])))
else:
    print("Думаешь не решишь)")
    b_indicator_dullness = b_indicator_dullness + 1

# /Задание 2.534233412

# Задание 3 - Не делать, так там требуется цикл котрый мы не учили

# Задание 4 - Так а тут сказали что только 4 слова в предложении, значит делаем без цыклов)

print()
print("Введите предложение из 4 слов и я определю какое из слов большое:")
u_t_sentence_for_find_max_world = input(g_u_i)

word_with_max_symbols = ""
words_with_max_world = u_t_sentence_for_find_max_world.split(" ")
temp_arr = [
    len(words_with_max_world[0]),
    len(words_with_max_world[1]),
    len(words_with_max_world[2]),
    len(words_with_max_world[3])
]

if temp_arr[0] > temp_arr[1] and temp_arr[0] > temp_arr[2] and temp_arr[0] > temp_arr[3]:
    word_with_max_symbols = words_with_max_world[0]
elif temp_arr[1] > temp_arr[0] and temp_arr[1] > temp_arr[2] and temp_arr[1] > temp_arr[3]:
    word_with_max_symbols = words_with_max_world[1]
elif temp_arr[2] > temp_arr[1] and temp_arr[2] > temp_arr[0] and temp_arr[2] > temp_arr[3]:
    word_with_max_symbols = words_with_max_world[2]
elif temp_arr[3] > temp_arr[1] and temp_arr[3] > temp_arr[2] and temp_arr[3] > temp_arr[0]:
    word_with_max_symbols = words_with_max_world[3]

if word_with_max_symbols == "":
    print("Прости, мне нужно было выбрать лишь одно слово, а тут их несколько")
else:
    print("Хе хе, самое большое слово '{}'".format(word_with_max_symbols))

# /Задание 4 - Конец основным заданиям


# Задание 5 - тоже моё задание

print()
print()
print("Окей, сейчас будет отступление")
print("Я хочу поиграть, в угадай число. Выбери число от 1 до 10. У меня будет 3 попытки. Хотите поиграть?")

b_answer_txt = "Это число {}"
b_task_txt = "это число меньше(м) или больше(б) моего?"

b_answer_num = -1

b_answer_num_min = 1
b_answer_num_max = 11

u_t_text = input(g_u_i)
if u_t_text.lower() in g_u_answer:
    print()
    print("Окей, значит вы загадали")

    b_a_o = True
    error = False

    # Шанс 1
    b_answer_num = randint(b_answer_num_min, b_answer_num_max)
    print(b_answer_txt.format(b_answer_num))
    u_t_text = input(g_u_i)

    if u_t_text.lower() in g_u_answer:
        b_a_o = False
        print("Ура, с первого раза получилось")

    elif  u_t_text.lower() in g_u_answer_no:
        print("Жаль что не угодал, а",b_task_txt)
        u_t_text = input(g_u_i)
        if u_t_text.lower() == "м":
            b_answer_num_max = b_answer_num
        elif u_t_text.lower() == "б":
            b_answer_num_min = b_answer_num
        else:
            b_a_o = False
            error = True
    else:
        b_a_o = False
        error = True

    # Шанс 2
    if b_a_o:
        b_answer_num = randint(b_answer_num_min, b_answer_num_max)
        print(b_answer_txt.format(b_answer_num))
        u_t_text = input(g_u_i)

        if u_t_text.lower() in g_u_answer:
            b_a_o = False
            print("На второй раз удалось)")

        elif  u_t_text.lower() in g_u_answer_no:
            print("Жаль что не угодал, а",b_task_txt)
            u_t_text = input(g_u_i)
            if u_t_text.lower() == "м":
                b_answer_num_max = b_answer_num
            elif u_t_text.lower() == "б":
                b_answer_num_min = b_answer_num
            else:
                b_a_o = False
                error = True
        else:
            b_a_o = False
            error = True


    # Шанс 3
    if b_a_o:
        b_answer_num = randint(b_answer_num_min, b_answer_num_max)
        print(b_answer_txt.format(b_answer_num))
        u_t_text = input(g_u_i)

        if u_t_text.lower() in g_u_answer:
            b_a_o = False
            print("Наконец я угодал")
        elif u_t_text.lower() in g_u_answer_no:
            print("Эх, не получилось мне угодать ни разу")
        else:
            error = True
            
        

    # Что-то пошло не так
    if error:
        print("Ой, какая-то ошибка вышла!")
        error = False

else:
    b_indicator_dullness = b_indicator_dullness + 1
    print("Вы на столько скучный, {} раза отказались от участия".format(b_indicator_dullness))

# /Задание 5