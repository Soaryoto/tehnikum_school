import discord
from discord import utils
import datetime
import config
import database


async def setInfo(channel):
    emb = discord.Embed( title = "Объявления сервера BAIK Technologies", color = discord.Color.red())

    emb.set_author( name = "ITARAKANI", icon_url = "https://avatanplus.com/files/resources/mid/573743ea56ca8154afe14b74.png")
    emb.set_footer( text = "BAIKbot", icon_url = "https://img.icons8.com/ios/500/discord-logo.png")

    emb.timestamp = datetime.datetime.now()

    emb.add_field( name = "Обновления:", value = "На сервере введён в тестовом режими автоматический подсчёт рабочего времени \n Данный счетчик будет вычислять количество проведённого времени в определённых каналах", inline = False)
    emb.add_field( name = "Каналы:", value = "Все каналы временно открыты для всех пользователей \n Канал 'Временное отсутствие' предназначен для подсчёта отсутствия сотрудника на рабочем месте", inline = False)
    emb.add_field( name = "Важно:", value = "Данный функционал не до конца доработан и продуман \n всё подсчитанное время не будет полностью отображать ваше время работы", inline = False)

    await channel.send(embed = emb)
    
async def commands(content, channel):
    commande = content[len(config.PREFFIX):]
    if commande == "clear":
        await channel.purge(limit = 100)
    if commande == "info":
        await channel.purge(limit = 1)
        await setInfo(channel)
    if commande == "info users":
        await channel.purge(limit = 1)
        await getInfoUsers(channel)
    print(commande)

async def getInfoUsers(channel):
    emb = discord.Embed( title = "Информация о сотрудниках", color = discord.Color.red())
    data = database.getData()
    for i in range(len(data["users_data"])):
        user_data = data["users_data"][i]
        key = "presence"
        string = "Работал: " + str(user_data[key][0]) + ":" + str(user_data[key][1]) + ":" + str(user_data[key][2]) + "\n"
        key = "absence"
        string += "Отдыхал: " + str(user_data[key][0]) + ":" + str(user_data[key][1]) + ":" + str(user_data[key][2]) + "\n"
        key = "last_actions"
        string += "Последняя активность: " + str(user_data[key][0]) + ":" + str(user_data[key][1]) + ":" + str(user_data[key][2])
        emb.add_field( name = user_data["name"], value = string, inline = False)
    await channel.send(embed = emb)

def updateVoiceChennel(self, user, where_from, where_to):
    date = datetime.datetime.now()
    if where_from.channel is None:
        database.setAttendanceUser(user.name, database.ACTIONS[1])
    elif where_to.channel is None:
        database.setAttendanceUser(user.name, database.ACTIONS[0])
    elif where_from.channel.id in config.ABSENCE_CHANEL:
        database.setAttendanceUser(user.name, database.ACTIONS[1])
    else:
        database.setAttendanceUser(user.name, database.ACTIONS[0])
