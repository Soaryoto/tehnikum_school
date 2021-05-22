import time
import telegram
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from Erie.core.core import Core
from Erie.database.worker import Worker

def GetDataInUpdater(updater):
    result = {
        "chat_id": updater.message.chat_id,
        "text": updater.message.text,
        "user_id" : updater.message.chat_id,
        "name": updater.message.from_user.first_name
    }
    return result

def Start(updater, context):
    data = GetDataInUpdater(updater)

    stiсker_data = ""
    text_data = ""
    text_set_lang = ""
    btns = []

    if Worker("tg").AddUser(data["user_id"], data["name"]) == 1:
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


def AnsverForText(updater, context):
    data = GetDataInUpdater(updater)
    locate = Worker("tg").GetLocateFromUser(data["user_id"])
    source = Core.GetLocalizationAnsverType(locate)
    desired_name = Worker("tg").GerDesiredName(data["user_id"])
    stiсker_data = ""
    msg_text = ""

    # Dance)
    if data["text"] in source["Question"][0]:
        stiсker_data = Core.GetSource("telegram_stiсkers_data", "Dance")
        context.bot.send_sticker(chat_id=data["chat_id"], sticker=stiсker_data)
        context.bot.send_message(chat_id=data["chat_id"], text="Тут должна быть музыка")
        return

    for i in range(0, len(source["Question"])):
        if data["text"] in source["Question"][i]:
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
    UserId = updater.callback_query.from_user.id
    Locate = updater.callback_query.data
    context.bot.delete_message(message_id = updater.callback_query.message.message_id, chat_id=updater.callback_query.message.chat.id)
    Worker("tg").SetLocateFromUser(UserId, Locate)