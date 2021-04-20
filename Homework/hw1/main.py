# Напечатал Danila Dumbrovskiy Ivanovich

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

print((d+i+c+b+a+d).capitalize(), c+d+a+i)

print("Во, я самый грамотный бот на свете")

# /Задание 1 - Что там дальше?

# Задание 2 - Ща сделаем

print("Введите предложение: ")
u_t_sentence_for_replase = input()

print("Какое словы вы хотите заменить?")
u_t_world_for_replase = input()

print("А на что вы хотите заменить?")
u_t_world_to_replase = input()

bot_t_answer_for_replase = "Я заменил слово, и теперь получилось такое предложение :\n{}"
print(
    bot_t_answer_for_replase.format(
            u_t_sentence_for_replase.replace(u_t_world_for_replase, u_t_world_to_replase)
        )
    )

# /Задание 2 - кончилось

# Задание 3 - Не делать, так там требуется цикл котрый мы не учили

# Задание 4 - Так а тут сказали что только 4 слова в предложении, значит делаем без цыклов)
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