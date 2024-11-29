import disnake
from disnake.ext import commands
import os
from botconfig import token_id
import asyncio.tasks
from asyncio.tasks import sleep
from disnake.utils import format_dt
import datetime
import time

intents = disnake.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    global starttime 
    starttime = time.time()

    print(f"Бот запущен на {bot.user.name}")
    print(f"Disnake.py API версия: {disnake.__version__}")
    print(f"Кол-во команд: {len(bot.slash_commands)}")
    print(f"Меня создал: yokazeru")
    print("-------------------")

    while True:
      await bot.change_presence(
            activity=disnake.Streaming(
                name=f'в разработке...', url='https://www.twitch.tv/discord', twitch_name="discord", game="Minecraft"))
      await asyncio.sleep(300)

@bot.slash_command(description="Показывает текущую статистику бота.")
async def stats(interaction):
  await interaction.response.defer()
  msg = len(bot.cached_messages)
  cogs_total = len(bot.cogs)
  cogs_toal = int(cogs_total + 1)
  ping = round(bot.latency * 1000)
  uptime = format_dt(starttime, 'R')
  channels = len([member for member in bot.get_all_channels()])

  embed=disnake.Embed(title=f"Статистика AzureBot", description=f"Модулей в боте: **{cogs_toal}**\nКол-во команд: **{len(bot.slash_commands)}**", color=0x2e2f33, timestamp=datetime.datetime.now())
  embed.add_field(name="> Статистика:", value=f"Серверов: **{len(bot.guilds)}**\nПользователей: **{len(bot.users)}**\nКаналов: **{channels}**")
  embed.add_field(name="> Информация:", value=f"Задержка: **{ping} ms**\nВремя работы: {uptime}\nКол-во сообщений: **{msg}**")
  embed.set_footer(text=f"AzureBot", icon_url=f"https://cdn.discordapp.com/attachments/698473661312532490/1162085887849541642/sd2.png?ex=653aa7d2&is=652832d2&hm=4331d032f166c174311808bbe6dc001bfe05335899076fde83895090379f5dcb&")
  embed.set_thumbnail(url=f"{bot.user.avatar}")
  await interaction.followup.send(embed=embed)

bot.load_extension("cogs.info")
bot.load_extension("cogs.premium")
bot.load_extension("cogs.fun")

bot.run(token_id)
