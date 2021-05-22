from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from Erie.telegram_core.functions import *
from Erie.core.core import Core


class TelegramCore:
    __token = ""
    __updater = None
    __dispatcher = None

    def __init__(self, token):
        self.__updater = Updater(token=token, workers=5)
        self.__dispatcher = self.__updater.dispatcher

    def InitHandlers(self):
        disp = self.__dispatcher
        updt = self.__updater
        # Begin

        HandlerStartCommand = CommandHandler(command="start", callback=Start, run_async=True)
        disp.add_handler(HandlerStartCommand)

        for locate in Core.GetLocalizationTypes():
            HandlerForLang = CallbackQueryHandler(pattern=locate, callback=SetLangForUser, run_async=True)
            disp.add_handler(HandlerForLang)


        HendlerAnsverText = MessageHandler(filters=Filters.text, callback=AnsverForText, run_async=True)
        disp.add_handler(HendlerAnsverText)

        HendlerAnsverForRestType = MessageHandler(filters=Filters.all, callback=AnsverForRestType, run_async=True)
        disp.add_handler(HendlerAnsverForRestType)

        # End
        updt.start_polling(drop_pending_updates=True)
        self.__updater.idle()

    def __exit__(self, exc_type, exc_val, exc_tb):  # Работает? Не знаю но оставлю на всякий пожарный
        print("Stop bot")
        self.__updater.idle()
