import time
import telegram
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from Erie.core.core import Core
from Erie.database.worker import Worker

def get_data(updater):
    result = {
        "chat_id": updater.message.chat_id,
        "text": updater.message.text,
        "user_id" : updater.message.chat_id,
        "name": updater.message.from_user.first_name
    }
    return result

def Start(updater, context):
    data = get_data(updater)

    stiсker_data = ""
    text_data = ""
    btns = []

    if Worker("tg").AddUser(data["user_id"], data["name"]) == 0:
        localizationType = Core.GetLocalizationTypes()

        for key in localizationType.keys():
            btns.append(InlineKeyboardButton(text=localizationType[key], callback_data=key))

        stiсker_data = Core.GetSource("telegram_stiсkers_data", "Hello")
        text_data = Core.GetLocalizationStringRandom("ru_ru", "FirstEntry")
    else:
        desired_name = Worker("tg").GerDesiredName(data["user_id"])
        stiсker_data = Core.GetSource("telegram_stiсkers_data", "Hello")
        text_data = Core.GetLocalizationStringRandom("ru_ru", "Hello").format(desired_name)


    context.bot.send_sticker(chat_id=data["chat_id"], sticker=stiсker_data)
    if len(btns) > 0:
        context.bot.send_message(text=text_data, chat_id=data["chat_id"], reply_markup=InlineKeyboardMarkup([btns]))
    else:
        context.bot.send_message(text=text_data, chat_id=data["chat_id"])


def text_answ(updater, context):
    chat_id = updater.message.chat_id
    message_text = updater.message.text
    context.bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
    time.sleep(2)
    context.bot.send_message(chat_id=chat_id, text=message_text)


def CreateButtons(updater, context):
    chat_id = updater.message.chat_id
    btn1 = [KeyboardButton(text="Нажми меня!", callback_data="first")]
    btn2 = [KeyboardButton(text="Неет, нажми меня!", callback_data="second")]
    context.bot.send_message(chat_id=chat_id, text="Выбери кнопку",
                             reply_markup=ReplyKeyboardMarkup([btn1, btn2], resize_keyboard=True,
                                                              one_time_keyboard=True))


def btnFirstClick(updater, context):
    chat_id = updater.message.chat_id
    context.bot.send.send_message(chat_id=chat_id, text="btnFirstClick")


def btnSecondClick(updater, context):
    chat_id = updater.message.chat_id
    context.bot.send.send_message(chat_id=chat_id, text="btnSecondClick")
