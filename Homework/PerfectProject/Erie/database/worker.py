import sqlite3
from Erie.core.core import Core

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
        except:
            Core.WriteErrorMes()

        return result

    def AddUser(self, UserId, UserName):
        query = '''
            SELECT ID FROM {} WHERE ID = {}
        '''.format(
            self.__ConverTableName("USERS"),
            UserId
        )
        data = self.ExecuteQuery(query)
        if len(self.ExecuteQuery(query)) > 0:
            return -1

        query = '''
            INSERT INTO {0} (ID, USER_NAME, DESIRED_NAME) VALUES ({1}, "{2}", "{2}")
        '''.format(
            self.__ConverTableName("USERS"),
            UserId,
            UserName
        )

        self.ExecuteQuery(query)
        return 1

    def GerDesiredName(self, UserId):
        result = ""
        query = '''
            SELECT DESIRED_NAME FROM {0} WHERE ID = {1}
        '''.format(
            self.__ConverTableName("USERS"),
            UserId
        )

        tableSource = self.ExecuteQuery(query)
        if len(tableSource) > 0:
            result = tableSource[0][0]
        else:
            result = "Ошибка при выводе имени"
        return result




    def __ValideDatabase(self):

        #Таблица с пользователями
        query = '''
            CREATE TABLE IF NOT EXISTS {}
            (
                ID INT,
                USER_NAME STRING,
                DESIRED_NAME STRING,
                USER_FIRST_NAME STRING,
                USER_SECOND_NAME STRING,
                PHONE INTEGER,
                LANG INTEGER
            )
        '''.format(self.__ConverTableName("USERS"))
        self.ExecuteQuery(query)

        #Таблица с активностями пользователя
        query = '''
            CREATE TABLE IF NOT EXISTS {}
            (
                USER_ID INT,
                USER_ACTIVITY_TEG STRING,
                DATE_TIME STRING
            )
        '''.format(self.__ConverTableName("USERS_ACTIVITY"))
        self.ExecuteQuery(query)



