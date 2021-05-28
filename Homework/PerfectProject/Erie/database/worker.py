import sqlite3
from Erie.core.core import Core
from Erie.database import query_scripts as TempQuery

class Worker:

    __prefix = ""

    def __init__(self, tag):
        self.__prefix = tag + "_"
        self.__ValideDatabase()

    def __ConverTableName(self, name):
        result = self.__prefix.upper() + name
        return result


    def ExecuteQuery(self, query_string):
        result = ""
        try:
            conn = sqlite3.connect(Core.GetMainDir() + "/database/data/main_database.sqlite")
            cursor = conn.cursor()

            if query_string.upper().find("SELECT") == -1:
                cursor.execute(query_string)
                conn.commit()
            else:
                result = cursor.execute(query_string).fetchall()

            conn.close()
        except Exception as exc:
            Core.WriteErrorMes(exc.args[0])

        return result

    def AddUser(self, UserId, UserName, FirstName = ""):
        query = TempQuery.find_user_for_id.format(
            self.__prefix,
            UserId
        )
        data = self.ExecuteQuery(query)
        if len(self.ExecuteQuery(query)) > 0:
            return -1

        if FirstName == "":
            FirstName = UserName

        query = TempQuery.add_user.format(
            self.__prefix,
            UserId,
            UserName,
            FirstName
        )

        self.ExecuteQuery(query)
        return 1

    def GerDesiredName(self, UserId):
        result = ""
        query = TempQuery.get_desire_user_name.format(
            self.__prefix,
            UserId
        )

        tableSource = self.ExecuteQuery(query)
        if len(tableSource) > 0:
            result = tableSource[0][0]
        else:
            result = "Ошибка при выводе имени"
        return result

    def SetLocateFromUser(self, UserId, Locate):
        query = TempQuery.set_locate_for_user.format(
            self.__prefix,
            UserId,
            Locate
        )
        self.ExecuteQuery(query)

    def GetLocateFromUser(self, UserId):
        result = ""
        query = TempQuery.get_locate_for_user.format(
            self.__prefix,
            UserId
        )

        tableSource = self.ExecuteQuery(query)
        if len(tableSource) > 0:
            result = tableSource[0][0]
        else:
            result = "Ошибка при выводе языка"
        return result

    def UserHaveProductsInBascet(self, userId):
        result = False

        query = TempQuery.get_products_in_basket.format(
            self.__prefix,
            userId
        )

        tableSource = self.ExecuteQuery(query)
        if len(tableSource) > 0:
            result = len(tableSource)
        else:
            Core.WriteErrorMes(errorText="Ошибка проверки количества продуктов у пользователя id = {}".format(userId))

        return result

    def GetProductsType(self):
        result = []

        query = TempQuery.get_product_type

        result = self.ExecuteQuery(query)

        return result

    def __ValideDatabase(self):

        #Таблица с пользователями
        query = TempQuery.table_users.format(self.__prefix)
        self.ExecuteQuery(query)

        #Таблица с активностями пользователя
        query = TempQuery.table_users_activity.format(self.__prefix)
        self.ExecuteQuery(query)

        #Таблица с типами товаров
        query = TempQuery.table_product_types
        self.ExecuteQuery(query)

        #Таблица с товарами
        query = TempQuery.table_products
        self.ExecuteQuery(query)

        #Таблица с карзиной
        query = TempQuery.table_basket.format(self.__prefix)
        self.ExecuteQuery(query)



