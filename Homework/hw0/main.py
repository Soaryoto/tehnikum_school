
# Напечатал Danila Dumbrovskiy Ivanovich

# Тому кто начал читать мой код, пожалуйста перестанте.
# Мой код не понять и не исправить поэтому и не мучайте себя и просто
# увеличте в следующей строке параметр worst_code
#
# worst_code = 1

# Весь текст который есть для перевода
text_title_1 = "Добро пожаловать в анонимный чат!"
text_title_2 = "В скором времени вы сможете хорошо пообщаться с другими людьми"
text_title_warning = "(Внимание некоторые пользователи сообщали что в чате с вами общался бот который вымогал личные данные)"
text_get_com_style = "Для продолжения выберите число от 1 до 3 (проверка от ботов)"

text_wait = "Подождите, ведётся поиск собеседника для вас ..."
text_find_interlocutor = "Ура, найден собеседник для вас. Можете начать ваше общение."

text_interlocutor = "Неизвестный"
text_you = "Вы"

text_end_error = "Система выдает ошибку, вы ввели другое число. Так как вы не способны выполнить условие мы предпологаем что вы бот и должны с вами попрощатся."

# /Весь текст который есть для перевода

# Просто переменки для бота

debug = False
debug_text = "debug version"
debug_сom_style_text = "3"

bot_name = "Махмуд" # Имя бота
bot_age = "25" # Возраст бота
bot_gender = False # True - девушка, False - парень
bot_сom_style = 0 # Стиль общения

bot_preference_min_age = 18 # Минимальный предпочетаемый возраст
bot_preference_max_age = 100 # Максимальный предпочетаемый возраст
bot_preference_gender = True # Предпочитаемый пол True - девушка, False - парень

bot_next_text_quest = False # Нужно когда выберает по одному варианту

bot_get_num_count = 0 # Нужно чтобы бот по разному запрашивал число

human_name = "" # Имя
human_age = -1 # Возраст
human_age_check = False
human_gender = False # True - девушка, False - парень
human_input_text = "" # Просто переменка для хранения текста

# /Просто переменки для бота

# /Весь текст бота который есть для перевода

# Общий стиль
bot_text_error = "Внимание! Произошла ошибка, свяжитесь с администратором и сообщите о проблеме"
bot_text_add_name = "сумму(с)"
bot_text_add_value = "с"
bot_text_sub_name = "вычестание(в)"
bot_text_sub_value = "в"
bot_text_comt_name = "произведение(п)"
bot_text_comt_value = "п"
bot_text_and = "и"
bot_text_or = "или"

# Стиль 1 = _st1
bot_text_first_quest_st1 = "Девушка?"

bot_text_second_quest_st1 = "Класс, меня зовут " + bot_name + ", а тебя?"

bot_text_third_quest_1_st1 = "Рад знакомству"
bot_text_third_quest_2_st1 = "Мне " + bot_age + ", а тебе ?"

bot_text_fourth_quest_st1 = "Я бы поболтал с тобой, но я мало знаю про Python и могу только найти " + bot_text_add_name +  ", " + bot_text_sub_name + " " + bot_text_and + " " + bot_text_comt_name + " из двух чисел. Выбери один вариант что ты хочешь чтобы я решил для тебя"

bot_text_fifth_quest_1_st1 = "Хорошо, осталось лишь"
bot_text_fifth_quest_2_st1 = "выберай"

bot_text_sixth_quest_1_st1 = "Отлично, осталось"
bot_text_sixth_quest_2_st1 = "и нужны последние два числа"

bot_text_get_first_num_1_st1 = "Хорошо, давай первое число"
bot_text_get_second_num_1_st1 = "Отлично, а теперь второе"

bot_text_get_first_num_2_st1 = "Так, давай тепер первое число"
bot_text_get_second_num_2_st1 = "Ну и второе"

bot_text_get_first_num_3_st1 = "Последнее задание, и давай первое число"
bot_text_get_second_num_3_st1 = "А про второе забыли?"

bot_text_answer_add_st1 = "Я сложил эти числа и у меня получилось"
bot_text_answer_sub_st1 = "Так, отнять значит. Ответ"
bot_text_answer_comt_st1 = "Как же я не люблю умножать, но хоть решил и у меня получилось"

bot_text_nice_joke_st1 = "Супер шутка, я пожалуй пойду."
bot_text_if_h_y_st1 = "Понятно, я пожалуй пойду."
bot_text_if_h_m_st1 = "Неее, ты мне не нужен, пока."

# Стиль 2 = _st2
bot_text_first_quest_st2 = "Хай я " + bot_name + ", на связи девушка?"

bot_text_second_quest_st2 = "А сколько же годиков ей ?"

bot_text_third_quest_st2 = "Ты мне подходишь."

bot_text_fourth_quest_st2 = "Ок, надо уже начинать. Короче, выберай " + bot_text_add_name +  ", " + bot_text_sub_name + " " + bot_text_or + " " + bot_text_comt_name + ". Пока я даю шанс пользуйся."

bot_text_fifth_quest_1_st2 = "Ну решил я твою легкую задачку, какие там остались? Вроде"
bot_text_fifth_quest_2_st2 = "только. Ну выбирай"

bot_text_sixth_quest_1_st2 = "Осталось"
bot_text_sixth_quest_2_st2 = "давай уже заканчивать, хочу спать"

bot_text_get_first_num_1_st2 = "Всё, а то я усну пока выберешь. Пиши первое число"
bot_text_get_second_num_1_st2 = "Ну числа ты знаешь, уже хорошо. Ток мне нужно два числа"

bot_text_get_first_num_2_st2 = "Отслично, давай свои числа"
bot_text_get_second_num_2_st2 = "Мне напоминать надо про второе?"

bot_text_get_first_num_3_st2 = "Что так долго пишешь ?"
bot_text_get_second_num_3_st2 = "Угадай что сейчас скажу"


bot_text_answer_add_st2 = "Плюс мину равно"
bot_text_answer_sub_st2 = "Скучно как-то, получается"
bot_text_answer_comt_st2 = "Я так хорош что моментально ответил на твою задачку. Если что ответ"

bot_text_nice_joke_st2 = "Что серьёзно, я пока не интересуюсь таким."
bot_text_if_h_y_st2 = "Понятно, ты меня не интересуешь."
bot_text_if_h_m_st2 = "Оу сори, но мне пора."

# Стиль 3 = _st3
bot_text_first_quest_st3 = "Добрый вечер, девушка "

bot_text_second_quest_st3 = "!!!!!!!!!!!!!!!!!!!!!!!ошибка"

bot_text_third_quest_st3 = "!!!!!!!!!!!!!!!!!!!!ошибка"

bot_text_fourth_quest_st3 = "Я бы хотел проверить себя на скорость решений математических задачь. Напишите " + bot_text_add_name +  ", " + bot_text_sub_name + " " + bot_text_or + " " + bot_text_comt_name + " и я постораюсь быстро их решить."

bot_text_fifth_quest_1_st3 = "Отлично получилось, теперь осталось"
bot_text_fifth_quest_2_st3 = "выберайте что будем следующее делать"

bot_text_sixth_quest_1_st3 = "Осталось"
bot_text_sixth_quest_2_st3 = ", в следующий раз я по больше задачь порешаю"

bot_text_get_first_num_1_st3 = "Первое число введите"
bot_text_get_second_num_1_st3 = "Теперь второе"

bot_text_get_first_num_2_st3 = "Замечачтельно, первое число"
bot_text_get_second_num_2_st3 = "А второе?"

bot_text_get_first_num_3_st3 = "Пишите первое число"
bot_text_get_second_num_3_st3 = "Как замечательно, теперь второе"

bot_text_answer_add_st3 = "Значит сложение чисел, так посмотрим. Хорошо, получилось"
bot_text_answer_sub_st3 = "Вычтем, вычтем. И получается"
bot_text_answer_comt_st3 = "Произведение! Люблю умножать. Так, получаеться ответ"

bot_text_nice_joke_st3 = "Супер шутка, я пожалуй пойду. !ошибка"
bot_text_if_h_y_st3 = "Понятно, я пожалуй пойду. !ошибка"
bot_text_if_h_m_st3 = "Какая же беда, я сейчас не могу говорить, до скорой встречи"


# /Весь текст бота который есть для перевода


# Далее ничего интересного нет


# Тут начало всех тектовых сообщений !!!!!!!!!!!!!!!!!!!!!!!!
print(text_title_1)
print(text_title_2)
print(text_title_warning)

if debug:
    print(debug_text, "style = " + debug_сom_style_text)
    сom_style_text = debug_сom_style_text
else:
    сom_style_text = input(text_get_com_style + ": ")

if сom_style_text == "1" or сom_style_text == "2" or сom_style_text == "3":

    bot_сom_style = int(сom_style_text)

    print(text_wait)
    print(text_find_interlocutor)

    if bot_сom_style == 1 or bot_сom_style == 3:
        print(text_interlocutor + ":", bot_text_first_quest_st1)

        human_input_text = input(text_you + ": ")

        if human_input_text == "Да" or human_input_text == "да" or human_input_text == "Yes" or human_input_text == "yes": # Проверяю, девушка или нет
            human_gender = True
            
            print(text_interlocutor + ":", bot_text_second_quest_st1)
            
            human_input_text = input(text_you + ": ")
            human_name = human_input_text

            print(bot_name + ":", bot_text_third_quest_1_st1, human_name + ".", bot_text_third_quest_2_st1)

            human_input_text = input(text_you + ": ")
            human_age = int(human_input_text)
            
            if human_age >= bot_preference_min_age and human_age < bot_preference_max_age:
                human_age_check = True
                # Здесь конец и потверждение по всем условиям, а после выполнение основной задачи(она ниже выполняеться)

            elif human_age >= bot_preference_max_age:
                print(bot_name + ":", bot_text_nice_joke_st1)
            else:
                print(bot_name + ":", bot_text_if_h_y_st1)
        else:
            print(bot_text_if_h_m_st1)
        
    elif bot_сom_style == 2:
        print(text_interlocutor + ":",bot_text_first_quest_st2)
        human_input_text = input(text_you + ": ")
        
        if human_input_text == "Да" or human_input_text == "да" or human_input_text == "Yes" or human_input_text == "yes": # Проверяю, девушка или нет
            human_gender = True
            print(bot_name + ":",bot_text_second_quest_st2)
            human_input_text = input(text_you + ": ")
            human_age = int(human_input_text)
            
            if human_age >= bot_preference_min_age and human_age < bot_preference_max_age:
                print(bot_name + ":",bot_text_third_quest_st2)
                human_age_check = True
                # Здесь конец и потверждение по всем условиям, а после выполнение основной задачи(она ниже выполняеться)

            elif human_age >= bot_preference_max_age:
                print(bot_name + ":", bot_text_nice_joke_st2)
            else:
                print(bot_name + ":", bot_text_if_h_y_st2)


        else:
            print(bot_name + ":",bot_text_if_h_m_st2)

    elif bot_сom_style == 3 and False: # Не могу пока придумать
        print(text_interlocutor + ":",bot_text_first_quest_st3)
        human_input_text = input(text_you + ": ")

else:
    print(text_end_error)

# Задачи
if human_age_check and human_gender == bot_preference_gender: # Тут я вынес код за остальные условия, чтобы не копировать код в остальные условия. P. S. Я запарюсь ошибки искать

    # Вопрос?
    if bot_сom_style == 1:
        print(bot_name + ":", bot_text_fourth_quest_st1)
    elif bot_сom_style == 2:
        print(bot_name + ":", bot_text_fourth_quest_st2)
    elif bot_сom_style == 3:
        print(bot_name + ":", bot_text_fourth_quest_st3)


    # Здесь мы получаем начальную мат. функцию
    human_input_text = input(text_you + ": ")
    ht = human_input_text

    a = bot_text_add_value # bot_text_add_name
    s = bot_text_sub_value # bot_text_sub_name
    c = bot_text_comt_value # bot_text_comt_name

    # Получение первого числа
    if bot_сom_style == 1:
        print(bot_name + ":", bot_text_get_first_num_1_st1)
    elif bot_сom_style == 2:
        print(bot_name + ":", bot_text_get_first_num_1_st2)
    elif bot_сom_style == 3:
        print(bot_name + ":", bot_text_get_first_num_1_st3)
    num_1 = int(input(text_you + ": "))
    

    # Получение второго числа
    if bot_сom_style == 1:
        print(bot_name + ":", bot_text_get_second_num_1_st1)
    elif bot_сom_style == 2:
        print(bot_name + ":", bot_text_get_second_num_1_st2)
    elif bot_сom_style == 3:
        print(bot_name + ":", bot_text_get_second_num_1_st3)
    num_2 = int(input(text_you + ": "))


    # Тут идут словия решений
    if ht == a: # --------------- Сложение ---------------
        
        if bot_сom_style == 1:
            print(bot_name + ":", bot_text_answer_add_st1, num_1 + num_2)
            print(bot_name + ":", bot_text_fifth_quest_1_st1, bot_text_sub_name, bot_text_and, bot_text_comt_name, bot_text_fifth_quest_2_st1)
        elif bot_сom_style == 2:
            print(bot_name + ":", bot_text_answer_add_st2, num_1 + num_2)
            print(bot_name + ":", bot_text_fifth_quest_1_st2, bot_text_sub_name, bot_text_and, bot_text_comt_name, bot_text_fifth_quest_2_st2)
        elif bot_сom_style == 3:
            print(bot_name + ":", bot_text_answer_add_st3, num_1 + num_2)
            print(bot_name + ":", bot_text_fifth_quest_1_st3, bot_text_sub_name, bot_text_and, bot_text_comt_name, bot_text_fifth_quest_2_st3)

        human_input_text = input(text_you + ": ")
        ht = human_input_text

        # Получение первого числа
        if bot_сom_style == 1:
            print(bot_name + ":", bot_text_get_first_num_2_st1)
        elif bot_сom_style == 2:
            print(bot_name + ":", bot_text_get_first_num_2_st2)
        elif bot_сom_style == 3:
            print(bot_name + ":", bot_text_get_first_num_2_st3)
        num_1 = int(input(text_you + ": "))
        

        # Получение второго числа
        if bot_сom_style == 1:
            print(bot_name + ":", bot_text_get_second_num_2_st1)
        elif bot_сom_style == 2:
            print(bot_name + ":", bot_text_get_second_num_2_st2)
        elif bot_сom_style == 3:
            print(bot_name + ":", bot_text_get_second_num_2_st3)
        num_2 = int(input(text_you + ": "))

        if ht == s: # --- тут получаем разность и после произведение
            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_answer_sub_st1, num_1 - num_2)
                print(bot_name + ":", bot_text_sixth_quest_1_st1, bot_text_comt_name, bot_text_sixth_quest_2_st1)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_answer_sub_st2, num_1 - num_2)
                print(bot_name + ":", bot_text_sixth_quest_1_st2, bot_text_comt_name, bot_text_sixth_quest_2_st1)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_answer_sub_st3, num_1 - num_2)
                print(bot_name + ":", bot_text_sixth_quest_1_st3, bot_text_comt_name, bot_text_sixth_quest_2_st1)
            
            # Получение первого числа
            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_get_first_num_3_st1)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_get_first_num_3_st2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_get_first_num_3_st3)
            num_1 = int(input(text_you + ": "))
            

            # Получение второго числа
            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_get_second_num_3_st1)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_get_second_num_3_st2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_get_second_num_3_st3)
            num_2 = int(input(text_you + ": "))

            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_answer_comt_st1, num_1 * num_2)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_answer_comt_st2, num_1 * num_2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_answer_comt_st3, num_1 * num_2)

        elif ht == c: # --- тут получаем произведение и после разность
            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_answer_comt_st1, num_1 * num_2)
                print(bot_name + ":", bot_text_sixth_quest_1_st1, bot_text_sub_name, bot_text_sixth_quest_2_st1)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_answer_comt_st2, num_1 * num_2)
                print(bot_name + ":", bot_text_sixth_quest_1_st2, bot_text_sub_name, bot_text_sixth_quest_2_st2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_answer_comt_st3, num_1 * num_2)
                print(bot_name + ":", bot_text_sixth_quest_1_st3, bot_text_sub_name, bot_text_sixth_quest_2_st3)

            # Получение первого числа
            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_get_first_num_3_st1)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_get_first_num_3_st2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_get_first_num_3_st3)
            num_1 = int(input(text_you + ": "))
            

            # Получение второго числа
            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_get_second_num_3_st1)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_get_second_num_3_st2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_get_second_num_3_st3)
            num_2 = int(input(text_you + ": "))

            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_answer_sub_st1, num_1 - num_2)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_answer_sub_st2, num_1 - num_2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_answer_sub_st3, num_1 - num_2)

        else:
            print(bot_name + ":", bot_text_error)

    elif ht == s: # --------------- Разность ---------------
        if bot_сom_style == 1:
            print(bot_name + ":", bot_text_answer_sub_st1, num_1 - num_2)
            print(bot_name + ":", bot_text_fifth_quest_1_st1, bot_text_add_name, bot_text_and, bot_text_comt_name, bot_text_fifth_quest_2_st1)
        elif bot_сom_style == 2:
            print(bot_name + ":", bot_text_answer_sub_st2, num_1 - num_2)
            print(bot_name + ":", bot_text_fifth_quest_1_st2, bot_text_add_name, bot_text_and, bot_text_comt_name, bot_text_fifth_quest_2_st2)
        elif bot_сom_style == 3:
            print(bot_name + ":", bot_text_answer_sub_st3, num_1 - num_2)
            print(bot_name + ":", bot_text_fifth_quest_1_st3, bot_text_add_name, bot_text_and, bot_text_comt_name, bot_text_fifth_quest_2_st3)

        human_input_text = input(text_you + ": ")
        ht = human_input_text

        # Получение первого числа
        if bot_сom_style == 1:
            print(bot_name + ":", bot_text_get_first_num_2_st1)
        elif bot_сom_style == 2:
            print(bot_name + ":", bot_text_get_first_num_2_st2)
        elif bot_сom_style == 3:
            print(bot_name + ":", bot_text_get_first_num_2_st3)
        num_1 = int(input(text_you + ": "))
        

        # Получение второго числа
        if bot_сom_style == 1:
            print(bot_name + ":", bot_text_get_second_num_2_st1)
        elif bot_сom_style == 2:
            print(bot_name + ":", bot_text_get_second_num_2_st2)
        elif bot_сom_style == 3:
            print(bot_name + ":", bot_text_get_second_num_2_st3)
        num_2 = int(input(text_you + ": "))

        if ht == a: # --- тут получаем сумма и после произведение
            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_answer_add_st1, num_1 + num_2)
                print(bot_name + ":", bot_text_sixth_quest_1_st1, bot_text_comt_name, bot_text_sixth_quest_2_st1)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_answer_add_st2, num_1 + num_2)
                print(bot_name + ":", bot_text_sixth_quest_1_st2, bot_text_comt_name, bot_text_sixth_quest_2_st2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_answer_add_st3, num_1 + num_2)
                print(bot_name + ":", bot_text_sixth_quest_1_st3, bot_text_comt_name, bot_text_sixth_quest_2_st3)
            
            # Получение первого числа
            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_get_first_num_3_st1)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_get_first_num_3_st2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_get_first_num_3_st3)
            num_1 = int(input(text_you + ": "))
            

            # Получение второго числа
            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_get_second_num_3_st1)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_get_second_num_3_st2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_get_second_num_3_st3)
            num_2 = int(input(text_you + ": "))

            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_answer_comt_st1, num_1 * num_2)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_answer_comt_st2, num_1 * num_2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_answer_comt_st3, num_1 * num_2)

        elif ht == c: # --- тут получаем произведение и после сумма
            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_answer_comt_st1, num_1 * num_2)
                print(bot_name + ":", bot_text_sixth_quest_1_st1, bot_text_add_name, bot_text_sixth_quest_2_st1)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_answer_add_st2, num_1 * num_2)
                print(bot_name + ":", bot_text_sixth_quest_1_st2, bot_text_add_name, bot_text_sixth_quest_2_st2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_answer_add_st3, num_1 * num_2)
                print(bot_name + ":", bot_text_sixth_quest_1_st3, bot_text_add_name, bot_text_sixth_quest_2_st3)
            
            # Получение первого числа
            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_get_first_num_3_st1)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_get_first_num_3_st2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_get_first_num_3_st3)
            num_1 = int(input(text_you + ": "))
            

            # Получение второго числа
            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_get_second_num_3_st1)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_get_second_num_3_st2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_get_second_num_3_st3)
            num_2 = int(input(text_you + ": "))

            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_answer_add_st1, num_1 + num_2)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_answer_add_st2, num_1 + num_2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_answer_add_st3, num_1 + num_2)

        else:
            print(bot_name + ":", bot_text_error)

    elif ht == c: # --------------- Произведение ---------------
        if bot_сom_style == 1:
            print(bot_name + ":", bot_text_answer_comt_st1, num_1 - num_2)
            print(bot_name + ":", bot_text_fifth_quest_1_st1, bot_text_add_name, bot_text_and, bot_text_sub_name, bot_text_fifth_quest_2_st1)
        elif bot_сom_style == 2:
            print(bot_name + ":", bot_text_answer_comt_st2, num_1 - num_2)
            print(bot_name + ":", bot_text_fifth_quest_1_st2, bot_text_add_name, bot_text_and, bot_text_sub_name, bot_text_fifth_quest_2_st2)
        elif bot_сom_style == 3:
            print(bot_name + ":", bot_text_answer_comt_st3, num_1 - num_2)
            print(bot_name + ":", bot_text_fifth_quest_1_st3, bot_text_add_name, bot_text_and, bot_text_sub_name, bot_text_fifth_quest_2_st3)


        human_input_text = input(text_you + ": ")
        ht = human_input_text

        # Получение первого числа
        if bot_сom_style == 1:
            print(bot_name + ":", bot_text_get_first_num_2_st1)
        elif bot_сom_style == 2:
            print(bot_name + ":", bot_text_get_first_num_2_st2)
        elif bot_сom_style == 3:
            print(bot_name + ":", bot_text_get_first_num_2_st3)
        num_1 = int(input(text_you + ": "))
        

        # Получение второго числа
        if bot_сom_style == 1:
            print(bot_name + ":", bot_text_get_second_num_2_st1)
        elif bot_сom_style == 2:
            print(bot_name + ":", bot_text_get_second_num_2_st2)
        elif bot_сom_style == 3:
            print(bot_name + ":", bot_text_get_second_num_2_st3)
        num_2 = int(input(text_you + ": "))

        if ht == a: # --- тут получаем сумму и после разность
            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_answer_add_st1, num_1 + num_2)
                print(bot_name + ":", bot_text_sixth_quest_1_st1, bot_text_sub_name, bot_text_sixth_quest_2_st1)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_answer_add_st2, num_1 + num_2)
                print(bot_name + ":", bot_text_sixth_quest_1_st2, bot_text_sub_name, bot_text_sixth_quest_2_st2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_answer_add_st3, num_1 + num_2)
                print(bot_name + ":", bot_text_sixth_quest_1_st3, bot_text_sub_name, bot_text_sixth_quest_2_st3)
            
            # Получение первого числа
            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_get_first_num_3_st1)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_get_first_num_3_st2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_get_first_num_3_st3)
            num_1 = int(input(text_you + ": "))
            

            # Получение второго числа
            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_get_second_num_3_st1)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_get_second_num_3_st2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_get_second_num_3_st3)
            num_2 = int(input(text_you + ": "))

            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_answer_sub_st1, num_1 - num_2)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_answer_sub_st2, num_1 - num_2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_answer_sub_st3, num_1 - num_2)

        elif ht == s: # --- тут получаем разность и после сумму
            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_answer_sub_st1, num_1 - num_2)
                print(bot_name + ":", bot_text_sixth_quest_1_st1, bot_text_add_name, bot_text_sixth_quest_2_st1)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_answer_sub_st2, num_1 - num_2)
                print(bot_name + ":", bot_text_sixth_quest_1_st2, bot_text_add_name, bot_text_sixth_quest_2_st2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_answer_sub_st3, num_1 - num_2)
                print(bot_name + ":", bot_text_sixth_quest_1_st3, bot_text_add_name, bot_text_sixth_quest_2_st3)
            
            # Получение первого числа
            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_get_first_num_3_st1)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_get_first_num_3_st2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_get_first_num_3_st3)
            num_1 = int(input(text_you + ": "))
            

            # Получение второго числа
            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_get_second_num_3_st1)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_get_second_num_3_st2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_get_second_num_3_st3)
            num_2 = int(input(text_you + ": "))

            if bot_сom_style == 1:
                print(bot_name + ":", bot_text_answer_add_st1, num_1 + num_2)
            elif bot_сom_style == 2:
                print(bot_name + ":", bot_text_answer_add_st2, num_1 + num_2)
            elif bot_сom_style == 3:
                print(bot_name + ":", bot_text_answer_add_st3, num_1 + num_2)

        else:
            print(bot_name + ":", bot_text_error)
    else:
        print(bot_name + ":", bot_text_error)


    this_is_comment = "Главное не забыть добавить загадки"

# Подарили как-то программисту котенка. Ну выпустил он его погулять по
# квартире. А кот-то шибко умный не был, ну и наделал посреди комнаты.
# Посмотрел программер на кучу, потом на кота, потом на кучу и
# опять на кота и говорит: - Что-то не доработано в этой операционной
# системе!

# Мой приятель уверяет, что был свидетелем этого случая.
# Девица осваивает компьютер. Из-за долгих поисков каждой
# клавиши дело идет медленно. Парнишка-наставник ее утешает:
# - Это нормально! У тебя ж опыта нет.
# Последнее предложение (произнесенное без пауз) шокировало
# всех присутствующих.

    print(bot_name + ":", "Я бы мог продолжить но дальше мне не хватает знаний, в дальнейшем я получше смогу с вами общатся. Пока)")
    print("Пользователь вышел из чата!")


# Ну я же сказал, скучный код