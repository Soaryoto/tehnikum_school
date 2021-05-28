import discord
import datetime
import config
import functions
 
class BAIKbot(discord.Client):
    async def on_ready(self):
        print("BAIKbot connected to server")
 
    async def on_message(self, message):
        content = str(message.content)
        channel = message.channel
        if content.startswith(config.PREFFIX):
            await functions.commands(content, channel)

    async def on_voice_state_update(self, user, where_from, where_to):
        functions.updateVoiceChennel(self, user, where_from, where_to)


    async def on_raw_reaction_add(self, payload):
        print("event on_raw_reaction_add")
 
    async def on_raw_reaction_remove(self, payload):
        print("event on_raw_reaction_remove")

    async def on_typing( self, channel, user, when):#пользователь начал писать в каком-то канале
        print("Пользователь " + user.name + " начал писать в канале " + channel.name)

# RUN
bot = BAIKbot()
bot.run(config.TOKEN)