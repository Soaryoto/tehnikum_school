import time
import telegram
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, User
from Erie.core.core import Core
from Erie.database.worker import Worker

def GetDataInUpdater(updater):
    result = {
            "chat_id": None,
            "msg_id": None,
            "msg_text": None,
            "user_id": None,
            "username": None,
            "firstname": None,
            "lang": None
        }

    if updater.message is not None:
        result["chat_id"] = updater.message.chat_id
        result["msg_id"] = updater.message.message_id
        result["msg_text"] = updater.message.text
        result["user_id"] = updater.message.from_user.id
        result["username"] = updater.message.from_user.username
        result["firstname"] = updater.message.from_user.first_name
        result["lang"] = updater.message.from_user.language_code
    else:
        result["chat_id"] = updater.callback_query.message.chat_id
        result["msg_id"] = updater.callback_query.message.message_id
        result["msg_text"] = updater.callback_query.message.text
        result["user_id"] = updater.callback_query.from_user.id
        result["username"] = updater.callback_query.from_user.username
        result["firstname"] = updater.callback_query.from_user.first_name
        result["lang"] = updater.callback_query.from_user.language_code

    return result

def GetStateUser(userId):
    return Worker("tg").GetUserStateFromId(userId)

def SetStateUser(userId, value):
    return Worker("tg").SetUserStateFromId(userId, value)

def Start(updater, context):
    data = GetDataInUpdater(updater)

    stiсker_data = ""
    text_data = ""
    text_set_lang = ""
    btns = []

    if Worker("tg").AddUser(data["user_id"], data["firstname"], data["username"]) == 1:
        localizationType = Core.GetLocalizationTypes()

        for key in localizationType.keys():
            btns.append(InlineKeyboardButton(text=localizationType[key], callback_data=key))

        stiсker_data = Core.GetSource("telegram_stiсkers_data", "Hello")
        text_data = Core.GetRandomLocalizationString("ru_ru", "FirstEntry")
        text_set_lang = Core.GetRandomLocalizationString("ru_ru", "SetLang")
    else:
        locate = Worker("tg").GetLocateFromUser(data["user_id"])
        desired_name = Worker("tg").GerDesiredName(data["user_id"])

        stiсker_data = Core.GetSource("telegram_stiсkers_data", "Hello")
        text_data = Core.GetRandomLocalizationString(locate, "Hello").format(desired_name)


    context.bot.send_sticker(chat_id=data["chat_id"], sticker=stiсker_data)

    context.bot.send_message(text=text_data, chat_id=data["chat_id"])

    if len(btns) > 0:
        context.bot.send_message(text=text_set_lang, chat_id=data["chat_id"], reply_markup=InlineKeyboardMarkup([btns]))
    else:
        AddProductsButtonsInBusket(updater, context)


def AnsverForText(updater, context):
    data = GetDataInUpdater(updater)
    locate = Worker("tg").GetLocateFromUser(data["user_id"])
    source = Core.GetLocalizationAnsverType(locate)
    desired_name = Worker("tg").GerDesiredName(data["user_id"])
    stiсker_data = ""
    msg_text = ""

    # Temp code
    if Core.GetRandomLocalizationString(locate, "StartOrder") == data["msg_text"]:
        GetProductsFromUser(updater, context, "types")
        return
    if Core.GetRandomLocalizationString(locate, "HistoryOrder") == data["msg_text"]:
        GetOrders(updater, context)
        return

    # Dance)
    if data["msg_text"] in source["Question"][0]:
        stiсker_data = Core.GetSource("telegram_stiсkers_data", "Dance")
        audio = {"audio": Core.GetVoiceAndMusicInSource("")}
        context.bot.send_sticker(chat_id=data["chat_id"], sticker=stiсker_data)
        context.bot.send_message(chat_id=data["chat_id"], text="Тут должна быть музыка", file=audio)
        return

    for i in range(0, len(source["Question"])):
        if data["msg_text"] in source["Question"][i]:
            ansver_data = Core.GetRandomLocalizationAnsver(locate, i)
            msg_text = ansver_data[0].format(desired_name)
            stiсker_name = ansver_data[1]

            context.bot.send_chat_action(chat_id=data["chat_id"], action=telegram.ChatAction.TYPING)
            time.sleep(2)
            if stiсker_name != "":
                stiсker_data = Core.GetSource("telegram_stiсkers_data", stiсker_name)
                context.bot.send_sticker(chat_id=data["chat_id"], sticker=stiсker_data)
            context.bot.send_message(chat_id=data["chat_id"], text=msg_text)
            return

    msg_text = Core.GetRandomLocalizationString(locate, "ErrorUnderstandMsg")
    stiсker_data = Core.GetSource("telegram_stiсkers_data", "Whot")
    context.bot.send_chat_action(chat_id=data["chat_id"], action=telegram.ChatAction.TYPING)

    time.sleep(2)
    context.bot.send_sticker(chat_id=data["chat_id"], sticker=stiсker_data)
    context.bot.send_message(chat_id=data["chat_id"], text=msg_text)

def AnsverForRestType(updater, context):
    data = GetDataInUpdater(updater)

    locate = Worker("tg").GetLocateFromUser(data["user_id"])

    text_data = Core.GetRandomLocalizationString(locate, "DontAnderstandThisTypeMsg")
    stiсker_data = Core.GetSource("telegram_stiсkers_data", "Whot")

    context.bot.send_chat_action(chat_id=data["chat_id"], action=telegram.ChatAction.TYPING)
    time.sleep(1)
    context.bot.send_sticker(chat_id=data["chat_id"], sticker=stiсker_data)
    context.bot.send_message(chat_id=data["chat_id"], text=text_data)

def SetLangForUser(updater, context):
    data = GetDataInUpdater(updater)

    locate = updater.callback_query.data

    context.bot.delete_message(message_id=data["msg_id"], chat_id=data["chat_id"])
    Worker("tg").SetLocateFromUser(data["user_id"], locate)

    # Start buttons
    AddProductsButtonsInBusket(updater, context)

def CreateBtnSenderPhoneNumber(updater, context):
    data = GetDataInUpdater(updater)
    locate = Worker("tg").GetLocateFromUser(data["user_id"])

    send_phone_number = KeyboardButton(text=Core.GetRandomLocalizationString(locate, "SendPhoneNumber"), request_contact=True)

    btnsList = [[send_phone_number]]
    markup = ReplyKeyboardMarkup(btnsList, resize_keyboard=True, one_time_keyboard=True)

    text = Core.GetRandomLocalizationString(locate, "SendMePhone")
    context.bot.send_message(text=text, reply_markup=markup, chat_id=data["chat_id"])


def GetUserPhoneNumber(updater, context):
    pass

def SetUserLocation(updater, context):
    data = GetDataInUpdater(updater)

    longtude, latitude = updater.message.location.longitude, updater.message.location.latitude

    msg_text = Core.GetAddressFromCoords(longtude, latitude)
    context.bot.send_message(chat_id=data["chat_id"], text=msg_text)

def AddProductsButtonsInBusket(updater, context):
    data = GetDataInUpdater(updater)

    locate = Worker("tg").GetLocateFromUser(data["user_id"])

    start_order = KeyboardButton(Core.GetRandomLocalizationString(locate, "StartOrder"))
    history_order = KeyboardButton(Core.GetRandomLocalizationString(locate, "HistoryOrder"))

    btnsList = [[start_order]]
    if Worker("tg").UserHaveProductsInBascet(data["user_id"]):
        btnsList.append([history_order])
    markup = ReplyKeyboardMarkup(btnsList, resize_keyboard=True, one_time_keyboard=True)

    text = Core.GetRandomLocalizationString(locate, "GoodAddMainInformation")

    context.bot.send_message(text=text, reply_markup=markup, chat_id=data["chat_id"])

def SelectedProductsType(updater, context):
    data = GetDataInUpdater(updater)
    result = str(updater.callback_query.data).split(" ")[1]
    context.bot.delete_message(message_id=data["msg_id"], chat_id=data["chat_id"])
    GetProductsFromUser(updater, context, "product " + result)

def SelectedProduct(updater, context):
    data = GetDataInUpdater(updater)
    locate = Worker("tg").GetLocateFromUser(data["user_id"])

    result = str(updater.callback_query.data).split(" ")

    if result[1] == "return":
        context.bot.delete_message(message_id=data["msg_id"], chat_id=data["chat_id"])
        GetProductsFromUser(updater, context, "types")

    else:
        context.bot.delete_message(message_id=data["msg_id"], chat_id=data["chat_id"])
        Worker("tg").AddInUserBuscetProduct(data["user_id"], result[1])
        msg_text = Core.GetRandomLocalizationString(locate, "ProductAdded")
        msg_text = msg_text.format(Core.GetLocalizationProductName(locate, result[2]))

        history_order = KeyboardButton(Core.GetRandomLocalizationString(locate, "HistoryOrder"))
        markup = ReplyKeyboardMarkup([[history_order]], resize_keyboard=True, one_time_keyboard=True)

        if Worker("tg").UserHaveProductsInBascet(data["user_id"]):
            context.bot.send_message(chat_id=data["chat_id"], text=msg_text, reply_markup=markup)
        else:
            context.bot.send_message(chat_id=data["chat_id"], text=msg_text)
        GetProductsFromUser(updater, context, "product " + result[3])


def GetProductsFromUser(updater, context, type_data):
    data = GetDataInUpdater(updater)
    locate = Worker("tg").GetLocateFromUser(data["user_id"])

    msg_text = "Ничего нет из известного("
    btns = []

    if type_data == "types":
        SetStateUser(data["user_id"], "view_product_types")
        temp_data_tables = Worker("tg").GetProductsType()
        for row in temp_data_tables:
            text_btn = Core.GetLocalizationProductsType(locate, str(row[1]))
            btns.append([InlineKeyboardButton(text=text_btn, callback_data="product_types " + str(row[0]))])

    if type_data.startswith("product"):
        SetStateUser(data["user_id"], "selected_product_types_" + type_data.split(" ")[1])
        temp_data_tables = Worker("tg").GetProductsForType(type_data.split(" ")[1])
        for row in temp_data_tables:
            text_btn = Core.GetLocalizationProductName(locate, str(row[1]))
            btns.append([InlineKeyboardButton(text=text_btn, callback_data="product {} {} {}".format(str(row[0]), str(row[1]), str(row[2])) )])

        btns.append([InlineKeyboardButton(text=Core.GetRandomLocalizationString(locate, "Return"), callback_data="product return")])

    if len(btns) > 0:
        markup = InlineKeyboardMarkup(btns)
        if type_data == "types":
            msg_text = Core.GetRandomLocalizationString(locate, "SelectProductsType")
            context.bot.send_message(chat_id=data["chat_id"], text=msg_text, reply_markup=markup)
            return
        elif  type_data.startswith("product"):
            msg_text = Core.GetRandomLocalizationString(locate, "SelectProduct")
            context.bot.send_message(chat_id=data["chat_id"], text=msg_text, reply_markup=markup)
            return

    # if error
    context.bot.send_message(chat_id=data["chat_id"], text=msg_text)

def GetOrders(updater, context):
    data = GetDataInUpdater(updater)
    locate = Worker("tg").GetLocateFromUser(data["user_id"])

    dataOrder = Worker("tg").GetUserOrder(data["user_id"])

    msg_text = "У вас в корзмне:\n"
    for dataProduct in dataOrder:
        msg_text += Core.GetLocalizationProductName(locate, str(dataProduct[1])) + "\n"

    markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(text="Заказать", callback_data="send_order buy")],
            [InlineKeyboardButton(text="Очистить", callback_data="send_order clear")],
            [InlineKeyboardButton(text="Вернутся", callback_data="send_order return")]
    ])

    context.bot.send_message(chat_id=data["chat_id"], text=msg_text, reply_markup=markup)

def TreatmentOrders(updater, context):
    data = GetDataInUpdater(updater)
    locate = Worker("tg").GetLocateFromUser(data["user_id"])

    result = str(updater.callback_query.data).split(" ")
    msg_text = ""

    if result[1] == "return":
        context.bot.delete_message(message_id=data["msg_id"], chat_id=data["chat_id"])
        GetProductsFromUser(updater, context, "types")
    elif result[1] == "clear":
        context.bot.delete_message(message_id=data["msg_id"], chat_id=data["chat_id"])
        msg_text = "Ваша карзина очищена"
        context.bot.send_message(chat_id=data["chat_id"], text=msg_text)
        context.bot.send_chat_action(chat_id=data["chat_id"], action=telegram.ChatAction.TYPING)
        time.sleep(1)
        GetProductsFromUser(updater, context, "types")
    elif result[1] == "buy":
        context.bot.delete_message(message_id=data["msg_id"], chat_id=data["chat_id"])
        msg_text = "Заказ оформлен"
        context.bot.send_message(chat_id=data["chat_id"], text=msg_text)


#functions from add

def AddProductsType(updater, context):
    data = GetDataInUpdater(updater)
    locate = Worker("tg").GetLocateFromUser(data["user_id"])

    temd_data = data["msg_text"].replace("/AddProductsType", "").strip().split(" ")
    try:
        key = temd_data[0]
        name = temd_data[1]
        Worker("tg").AddProductsType(userId=data["user_id"], key=key, name=name, locate=locate)
    except Exception as ex:
        Core.WriteErrorMes(ex.args[0])

def AddProduct(updater, context):
    data = GetDataInUpdater(updater)
    locate = Worker("tg").GetLocateFromUser(data["user_id"])

    temd_data = data["msg_text"].replace("/AddProduct", "").strip().split(" ")
    try:
        key = temd_data[0]
        name = temd_data[1].replace("_", " ")
        category = temd_data[2]
        Worker("tg").AddProduct(userId=data["user_id"], key=key, name=name, category=category, locate=locate)
    except Exception as ex:
        Core.WriteErrorMes(ex.args[0])

#functions from tests
def TestButtons(updater, context):
    data = GetDataInUpdater(updater)
    locate = Worker("tg").GetLocateFromUser(data["user_id"])

    temd_data = data["msg_text"].replace("/TestButtons", "").strip().split(" ")
    count = temd_data[0]

    btnsList = []
    for i in range(0, int(count)):
        btnsList.append([InlineKeyboardButton(text="Кнопка" + str(i), callback_data="test btn" + str(i))])

    markup = InlineKeyboardMarkup(btnsList)
    text = "Тестируем количество кнопок"

    context.bot.send_message(text=text, chat_id=data["chat_id"], reply_markup=markup)


