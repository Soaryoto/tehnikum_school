from random import randint
# Напечатал Danila Dumbrovskiy Ivanovich

# Я оставил пометки для учителя чтобы быстро найти заданные задания #teacher_tehnikum_school
# Пометки
# В коментариях я разделил весь код на куски. Начала куска это "Задание", а конец "/Задание"

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
print("Привет, зовут меня КОТ. Некоторые меня называют Барсик. Почему, наверное из-за того что моему автору лень придумывать имена.")
print()

# /Вступление

# Задание 1 - без разници, есть такое слово или нет #teacher_tehnikum_school

    
print("Напиши мне буквы через пробел, а я тебе из него сделаю предложение: ")
u_t_sentence_for_new_sentence = input(g_u_i)

temp_arr = u_t_sentence_for_new_sentence.split(" ")
b_a_text = ""

for count_words in range(randint(3, 6)):
    for count_chars in range(randint(2, 6)):
        index_char = randint(0, len(temp_arr) - 1)
        b_a_text += temp_arr[index_char]
    b_a_text += " "

print()
print("Я создал предложение: ", b_a_text.capitalize())

print("Во, я самый грамотный бот на свете")

# /Задание 1 - Что там дальше?

# Задание 1.5 - это моё задание, дополнение
print()
print("У меня есть некая база знаний слов, хочешь узнать какие слова подойдут под эти буквы ?")
u_t_sentence_for_new_sentence = input(g_u_i)

if u_t_sentence_for_new_sentence.lower() in g_u_answer:
    b_notable_words = ["привет", "как", "дела", "лол", "магия", "прогер", "автоэлектростеклоподъемник"]
    b_answer_q_1_5 = ""

    for word in b_notable_words:
        have_this_word = True
        for char in word:
            if char not in temp_arr:
                have_this_word = False

        if have_this_word:
            if b_answer_q_1_5 == "":
                b_answer_q_1_5 += word
            else:
                b_answer_q_1_5 += " " + word
        

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


# Задание 1.9 - тут задача которой до этого не было #teacher_tehnikum_school

print()
print("Тут просят проверить на то что является ли ваше предложение палиндромом, введите бысрее предложение и я проверю")
u_t_for_checks = input(g_u_i)

if u_t_for_checks.lower().replace(" ", "") == u_t_for_checks.lower().replace(" ", "")[::-1]:
    print("О, знаешь что, твоё предложение является палиндромом")
else:
    print("Я тут посмотрел, твоё предлажение не является палиндромом")

# /Задание 1.9

# Задание 2 - Ща сделаем #teacher_tehnikum_school

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

# Задание 3 #teacher_tehnikum_school

print()
print("Так, сейчас мы займемся удалением повторяющикся символов из предложения")
u_t_for_del_chars = input(g_u_i)
b_t_answer = u_t_for_del_chars.replace(" ", "") # убираем пробелы

for char in b_t_answer:
    counter = 0
    for char2 in b_t_answer:
        if char == char2:
            counter += 1
    
    if counter > 1:
        b_t_answer = b_t_answer.replace(char, "", counter - 1)

print("Удалил все повторяющиеся буквы, и у меня получилось",b_t_answer)

# /Задание 3

# Задание 3.3 Почему 3.3, просто задачу 3 и 4 уже использовал а между ними еще одна появилась #teacher_tehnikum_school

print()
print("Введите мне предложение и я исправлю количество пробелов в нем")
u_t_for_del_gaps = input(g_u_i)


# И как же правильно сделать то? Я сделал первый вариан который пришёл в голову

b_t_answer = ""
u_t_for_del_gaps = u_t_for_del_gaps.split(" ")
for word in u_t_for_del_gaps:
    if word != "":
        if b_t_answer != "":
            b_t_answer += " " + word
        else:
            b_t_answer += word

print("Ок, я отредактировал: ",b_t_answer)


# /Задание 3.3

# Задание 3.7 Анологично с задачей 3.3 #teacher_tehnikum_school

print()
print("Введите предложение в котором я найду номер самых больших слов и выведу вам")
u_t_sentence_for_find_max_world = input(g_u_i)
temp_arr = u_t_sentence_for_find_max_world.split(" ")
max_length = 0

b_t_answer = "Я нашёл самые большие слова, они под номером {}"
b_t_answer_num = ""

for word in temp_arr:
    if max_length < len(word):
        max_length = len(word)



for word in temp_arr:
    if len(word) == max_length:
        if b_t_answer_num == "":
            b_t_answer_num += str(temp_arr.index(word) + 1)
        else:
            b_t_answer_num += ", " + (temp_arr.index(word) + 1)

print(b_t_answer.format(b_t_answer_num))

# /Задание 3.7

# Задание 4 - Делаем цикл!) #teacher_tehnikum_school

print()
print("Сейчас я бы хотел найти в вашем предложение большое слово, хотите ли вы использовать предыдущее предложение?")
u_t_answer = input(g_u_i)

if u_t_answer.lower() in g_u_answer:
    print("А вы ленивый) Ну хорошо, я возму прошлое предложение")
else:
    print("Ну тогда введите новое предложение и я найду в нем")
    u_t_sentence_for_find_max_world = input(g_u_i)

words_with_max_world = u_t_sentence_for_find_max_world.split(" ")

counter = 0
max_length = -1
max_length_word = ""

for word in words_with_max_world:
    if max_length < len(word):
        max_length_word = word
        max_length = len(word)
        counter = 1
    elif max_length == len(word):
        counter += 1
    

if counter > 1:
    print("Прости, мне нужно было выбрать лишь одно слово, а тут их {} шт. Ну а само слово это '{}'".format(counter, max_length_word))
else:
    print("Хе хе, самое большое слово '{}'".format(max_length_word))

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

# Задание 5.5

print("У меня тока что появился вопрос. Ты знаешь как зовут того кота, который появился в самом начале ?")
print("а)", "Простой кот")
print("б)", "Кот Бонго")
print("в)", "Лапки вверх")
print("г)", "Я не знаю правельного ответа")
u_t_text = input(g_u_i)

if u_t_text.lower() == "а":
    print("Ну да, выгледит как обычный кот, но его знают как Кот Бонго")
elif u_t_text.lower() == "б":
    print("Да верно, это был Кот Бонго")
elif u_t_text.lower() == "в":
    print("Ха-ха, смешной вариант, но это был Кот Бонго")
elif u_t_text.lower() == "г":
    print("Значит вы его не знаете, это был Кот Бонго")
else:
    print("Что-то вы странный вариант выбрали")
    print("Ну да ладно, это был Кот Бонго")

# /Задание 5.5

# Задание 6 Ищем количество строчних и прописных букв, только вот почему только анг? #teacher_tehnikum_school
print("\nНадеюсь не устали! p.s. я устал)")
print("Так теперь мне в вашем предложении нужно посчитать количесво строчных и прописных букв")

print("Хотите ли вы использовать прошлое предложение где я искал большие слова?")
u_t_answer = input(g_u_i)
u_t_for_count_chars = ""

b_t_answer = "Всего в вашем предложении "
many_count = ["{} прописных и ", "{} строчных"]
one_count = ["всего {} прописная и ", "{} строчная"]
count_big_char = 0
count_small_char = 0

if u_t_answer.lower() in g_u_answer:
    print("Замечательно, значит вы уже устали)")
    u_t_for_count_chars = u_t_sentence_for_find_max_world
else:
    print("Ну тогда введите новое предложение и я найду в нем")
    u_t_for_count_chars = input(g_u_i)

for char in u_t_for_count_chars:
    if char != "" and char.isalpha() and char.lower() == char:
        count_small_char += 1
    elif char != "" and char.isalpha():
        count_big_char += 1

if count_big_char > 1:
    b_t_answer += many_count[0].format(count_big_char)
else:
    b_t_answer += one_count[0].format(count_big_char)
    
if count_small_char > 1:
    b_t_answer += many_count[1].format(count_small_char)
else:
    b_t_answer += one_count[1].format(count_small_char)

print(b_t_answer)

# /Задание 6


# Задание 7 #teacher_tehnikum_school

print("Теперь посчитаем количество слов, это самое лёгкое")

print("Хотите так же использовать прошлое предложение?")
u_t_answer = input(g_u_i)
u_t_for_count_word = ""
if u_t_answer.lower() in g_u_answer:
    u_t_for_count_word = u_t_for_count_chars
else:
    print("Ну тогда введите новое предложение")
    u_t_for_count_word = input(g_u_i)


print("В предложении {} слов(о)".format(len(u_t_for_count_word.split(" "))))
# /Задание 7

print()
print()
print("Ну все, все задания были выполнены")
