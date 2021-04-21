# Напечатал Danila Dumbrovskiy Ivanovich

# Простые переменки нужные для процесса

g_u_answer = ["да", "yes", "ok", "ок"]
b_indicator_dullness = 0

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
u_t_sentence_for_new_sentence = input()

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
u_t_sentence_for_new_sentence = input()

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
    b_indicator_dullness = b_indicator_dullness + 1
# /Задание 1.5

# Задание 2 - Ща сделаем

print()
print("Сейчас я буду пытаться заменить часть строки в предложении")
print("Введите предложение: ")
u_t_sentence_for_replase = input()

print("Какое словы вы хотите заменить?")
u_t_world_for_replase = input()

print("А на что вы хотите заменить?")
u_t_world_to_replase = input()

print()
bot_t_answer_for_replase = "Я заменил слово, и теперь получилось такое предложение :\n{}"
print(
    bot_t_answer_for_replase.format(
            u_t_sentence_for_replase.replace(u_t_world_for_replase, u_t_world_to_replase)
        )
    )

# /Задание 2 - кончилось

# Задание 3 - Не делать, так там требуется цикл котрый мы не учили

# Задание 4 - Так а тут сказали что только 4 слова в предложении, значит делаем без цыклов)
print()
print("Введите предложение из 4 слов и я определю какое из слов большое:")
u_t_sentence_for_find_max_world = input()

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