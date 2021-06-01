import asyncio
import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from Erie.telegram_core.functions import *
from Erie.core.core import Core


async def сheckUsers():
    while True:
        print("Hello")
        if datetime.datetime.now().hour == 5:
            await asyncio.sleep(int(60*60*24))
        else:
            hour = 0
            if datetime.datetime.now().hour > 5:
                hour = datetime.datetime.now().hour - 5
                pass
            else:
                hour = 5 - datetime.datetime.now().hour
            await asyncio.sleep(int(60*60*hour))

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
        HandlerStartCommand = CommandHandler(command="SendPhone", callback=CreateBtnSenderPhoneNumber, run_async=True)
        disp.add_handler(HandlerStartCommand)

        HandlerStartCommand = CommandHandler(command="TestButtons", callback=TestButtons, run_async=True)
        disp.add_handler(HandlerStartCommand)


        HandlerForLang = CallbackQueryHandler(pattern="product_types", callback=SelectedProductsType, run_async=True)
        disp.add_handler(HandlerForLang)

        HandlerForLang = CallbackQueryHandler(pattern="product", callback=SelectedProduct, run_async=True)
        disp.add_handler(HandlerForLang)

        for locate in Core.GetLocalizationTypes():
            HandlerForLang = CallbackQueryHandler(pattern=locate, callback=SetLangForUser, run_async=True)
            disp.add_handler(HandlerForLang)

        #Admins functions

        HandlerStartCommand = CommandHandler(command="AddProductsType", callback=AddProductsType, run_async=True)
        disp.add_handler(HandlerStartCommand)

        HandlerStartCommand = CommandHandler(command="AddProduct", callback=AddProduct, run_async=True)
        disp.add_handler(HandlerStartCommand)

        HandlerForLang = CallbackQueryHandler(pattern="test", callback=GetUserPhoneNumber, run_async=True)
        disp.add_handler(HandlerForLang)

        #/Admins functions

        HendlerAnsverText = MessageHandler(filters=Filters.contact, callback=GetUserPhoneNumber, run_async=True)
        disp.add_handler(HendlerAnsverText)

        HendlerAnsverText = MessageHandler(filters=Filters.location, callback=SetUserLocation, run_async=True)
        disp.add_handler(HendlerAnsverText)

        HendlerAnsverText = MessageHandler(filters=Filters.text, callback=AnsverForText, run_async=True)
        disp.add_handler(HendlerAnsverText)


        HendlerAnsverForRestType = MessageHandler(filters=Filters.all, callback=AnsverForRestType, run_async=True)
        disp.add_handler(HendlerAnsverForRestType)

        # asyncio.run(сheckUsers)

        # End
        updt.start_polling(drop_pending_updates=True)
        self.__updater.idle()

    def __exit__(self, exc_type, exc_val, exc_tb):  # Работает? Не знаю но оставлю на всякий пожарный
        print("Stop bot")
        self.__updater.idle()
