import json
import datetime
import random
import sys

class Core:

    @staticmethod
    def GetMainDir():
        return "Erie"

    @staticmethod
    def WriteErrorMes():
        name = datetime.datetime.now().strftime("%Y_%m_%d")
        mes = "Error " + str(datetime.datetime.now()) + "\n\t" + str(sys.exc_info()[1]) + "\n"
        with open(Core.GetMainDir() + '/logs/{0}.log'.format(name), 'a') as file:
            file.write(mes)

    @staticmethod
    def GetParamInConfig(key):
        result = ""

        try:
            data = []
            with open(Core.GetMainDir() + "/core/config.json", 'r') as file:
                data = json.loads(file.read())
            if len(data) > 0:
                result = data[key]
        except:
            Core.WriteErrorMes()

        return result

    @staticmethod
    def GetTelegramToken():
        data = Core.GetParamInConfig("telegram")
        return data["token"]

    @staticmethod
    def GetSource(file_name, key):
        result = ""
        try:
            data = []
            with open(Core.GetMainDir() + "/source/{}.json".format(file_name), 'r') as file:
                data = json.loads(file.read())
            if len(data) > 0:
                result = data[key]
        except:
            Core.WriteErrorMes()

        return result

    @staticmethod
    def GetLocalizationTypes():
        result = {
            "ru_ru" : "Русский"
        }
        return result

    @staticmethod
    def GetLocalization(locate):
        result = {}
        try:
            with open(Core.GetMainDir() + "/source/localization/{}.json".format(locate), 'r', encoding="UTF-8") as file:
                result = json.loads(file.read())
        except:
            Core.WriteErrorMes()
        return result

    @staticmethod
    def SetLocalization(locate, data):
        try:
            with open(Core.GetMainDir() + "/source/localization/{}.json".format(locate), 'w') as file:
                json.dump(data, file)
        except:
            Core.WriteErrorMes()
            return -1
        return 0

    @staticmethod
    def GetLocalizationStringRandom(locate, key):
        result = ""
        try:
            result = Core.GetLocalization(locate)
            rand_int = random.randint(0, len(result[key]) - 1)
            result = result[key][rand_int]
        except:
            Core.WriteErrorMes()
            result = "Произошла ошибка, свяжитесь с администратором"

        return result