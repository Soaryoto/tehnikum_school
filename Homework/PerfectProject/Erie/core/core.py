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
            with open(Core.GetMainDir() + "/source/localization_new/{}.json".format(locate), 'w+') as file:
                json.dump(data, file)
        except:
            Core.WriteErrorMes()
            return -1
        return 0

    @staticmethod
    def GetRandomLocalizationString(locate, key):
        result = ""
        try:
            result = Core.GetLocalization(locate)
            rand_int = random.randint(0, len(result[key]) - 1)
            result = result[key][rand_int]
        except:
            Core.WriteErrorMes()
            result = "Произошла ошибка, свяжитесь с администратором"

        return result

    @staticmethod
    def GetLocalizationAnsverType(locate):
        result = ""
        try:
            result = Core.GetLocalization(locate)["DB_Ansver_Types"]
        except:
            Core.WriteErrorMes()
            result = "Произошла ошибка, свяжитесь с администратором"

        return result

    @staticmethod
    def GetRandomLocalizationAnsver(locate, index):
        result = ""
        try:
            ansvers = Core.GetLocalization(locate)
            ansvers = ansvers["DB_Ansver_Types"]["Ansver"][index]
            rand_int = random.randint(0, len(ansvers) - 1)
            ansverKey = ansvers[rand_int]

            result = Core.GetLocalization(locate)["DB_Ansvers"]
            rand_int = random.randint(0, len(result[ansverKey]) - 1)
            result = [result[ansverKey][rand_int], Core.GetRandomStikerAnsver(locate, ansverKey)]
        except:
            Core.WriteErrorMes()
            result = "Произошла ошибка, свяжитесь с администратором"

        return result

    @staticmethod
    def GetRandomStikerAnsver(locate, key):
        result = ""
        try:
            stickers = Core.GetLocalization(locate)["DB_AnsverSticker"][key]
            if len(stickers) > 0:
                rand_int = random.randint(0, len(stickers) - 1)
                result = stickers[rand_int]
            else:
                result = ""
        except:
            Core.WriteErrorMes()
            result = "Произошла ошибка, свяжитесь с администратором"

        return result