import json
import datetime
import random
import sys
import requests


class Core:

    @staticmethod
    def GetMainDir():
        return "Erie"

    @staticmethod
    def WriteErrorMes(errorText = ""):
        name = datetime.datetime.now().strftime("%Y_%m_%d")
        mes = "Error " + str(datetime.datetime.now()) + "\n\t"
        if errorText != "":
            mes += errorText
        else:
            mes += str(sys.exc_info()[1]) + "\n"
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
        except Exception as exc:
            Core.WriteErrorMes(exc.args[0])

        return result

    @staticmethod
    def GetTelegramToken():
        data = Core.GetParamInConfig("telegram")
        return data["token"]

    @staticmethod
    def GetGeolocationToken():
        data = Core.GetParamInConfig("telegram")
        return data["geo_loc"]

    @staticmethod
    def GetSource(file_name, key):
        result = ""
        try:
            data = []
            with open(Core.GetMainDir() + "/source/{}.json".format(file_name), 'r') as file:
                data = json.loads(file.read())
            if len(data) > 0:
                result = data[key]
        except Exception as exc:
            Core.WriteErrorMes(exc.args[0])

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
        except Exception as exc:
            Core.WriteErrorMes(exc.args[0])
        return result

    @staticmethod
    def SetLocalization(locate, data):
        try:
            with open(Core.GetMainDir() + "/source/localization_new/{}.json".format(locate), 'w+') as file:
                json.dump(data, file)
        except Exception as exc:
            Core.WriteErrorMes(exc.args[0])
            return -1
        return 0

    @staticmethod
    def GetRandomLocalizationString(locate, key):
        result = ""
        try:
            result = Core.GetLocalization(locate)
            rand_int = random.randint(0, len(result[key]) - 1)
            result = result[key][rand_int]
        except Exception as exc:
            Core.WriteErrorMes(exc.args[0])
            result = "Произошла ошибка, свяжитесь с администратором"

        return result

    @staticmethod
    def GetLocalizationAnsverType(locate):
        result = ""
        try:
            result = Core.GetLocalization(locate)["DB_Ansver_Types"]
        except Exception as exc:
            Core.WriteErrorMes(exc.args[0])
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
        except Exception as exc:
            Core.WriteErrorMes(exc.args[0])
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
        except Exception as exc:
            Core.WriteErrorMes(exc.args[0])
            result = "Произошла ошибка, свяжитесь с администратором"

        return result

    @staticmethod
    def GetLocalizationProducts(locate, type):
        result = {}
        try:
            with open(Core.GetMainDir() + "/source/products/localization/{}.json".format(locate), 'r', encoding="UTF-8") as file:
                result = json.loads(file.read())
        except Exception as exc:
            Core.WriteErrorMes(exc.args[0])
        return result[type]

    @staticmethod
    def SendGetQuery(url, params):
        result = None
        json_data = None
        try:
            result = requests.get(url=url, params=params)
            json_data = result.json()
        except Exception as ex:
            Core.WriteErrorMes(ex.args[0])

        return json_data;


    @staticmethod
    def GetAddressFromCoords(latitude, longitude):
        params = {
            "apikey": Core.GetTelegramToken(),
            "format": "json",
            "lang": "ru_RU",
            "kind": "house",
            "geocode": (latitude, longitude)
        }

        data = Core.SendGetQuery(url="http://geocode-maps.yandex.ru/1.x/", params=params)
        addres = ""

        try:
            addres = data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"][
            "GeocoderMetaData"]["AddressDetails"]["Country"]["AddressLine"]
        except Exception as ex:
            Core.WriteErrorMes(ex.args[0])

        return addres