import disnake
from disnake.ext import commands
import os
import asyncio.tasks
from asyncio.tasks import sleep
import datetime
import random
import qrcode

intents = disnake.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents)

class FunCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    global choice 
    SIDE = ["Орёл", "Решка"]

    @bot.slash_command(description="Подбросить монетку. И проверить свою удачу.", options=[
        disnake.Option(
            "сторона", description="Выберите сторону", type=disnake.OptionType.string, choices=SIDE, required=True
            ),],)
    async def coinflip(self, inter, сторона=None):
        number = random.randint(1,2)
        if сторона == "Орёл":
            if number == 1:
                embed = disnake.Embed(title="Монетка", description="И вы... выиграли!!!\nВыпал орёл",
                                        color=0x2e2f33, timestamp=datetime.datetime.now())
                embed.set_footer(text=f"AzureBot", icon_url=f"https://cdn.discordapp.com/attachments/698473661312532490/1162085887849541642/sd2.png?ex=653aa7d2&is=652832d2&hm=4331d032f166c174311808bbe6dc001bfe05335899076fde83895090379f5dcb&")
                await inter.response.send_message(embed=embed)
            else:
                embed = disnake.Embed(title="Монетка", description="И вы... проиграли\nВыпала решка",
                                        color=0x2e2f33, timestamp=datetime.datetime.now())
                embed.set_footer(text=f"AzureBot", icon_url=f"https://cdn.discordapp.com/attachments/698473661312532490/1162085887849541642/sd2.png?ex=653aa7d2&is=652832d2&hm=4331d032f166c174311808bbe6dc001bfe05335899076fde83895090379f5dcb&")
                await inter.response.send_message(embed=embed)
        if сторона == "Решка":
            if number == 2:
                embed = disnake.Embed(title="Монетка", description="И вы... выиграли!!!\nВыпала решка",
                                        color=0x2e2f33, timestamp=datetime.datetime.now())
                embed.set_footer(text=f"AzureBot", icon_url=f"https://cdn.discordapp.com/attachments/698473661312532490/1162085887849541642/sd2.png?ex=653aa7d2&is=652832d2&hm=4331d032f166c174311808bbe6dc001bfe05335899076fde83895090379f5dcb&")
                await inter.response.send_message(embed=embed)
            else:
                embed = disnake.Embed(title="Монетка", description="И вы... проиграли\nВыпал орёл",
                                        color=0x2e2f33, timestamp=datetime.datetime.now())
                embed.set_footer(text=f"AzureBot", icon_url=f"https://cdn.discordapp.com/attachments/698473661312532490/1162085887849541642/sd2.png?ex=653aa7d2&is=652832d2&hm=4331d032f166c174311808bbe6dc001bfe05335899076fde83895090379f5dcb&")
                await inter.response.send_message(embed=embed)

    @bot.slash_command(description="Шар с предсказаниями. Который ответит на ваш вопрос.", options=[
        disnake.Option("вопрос", description="Введите вопрос", type=disnake.OptionType.string, required=True
        ),])
    async def ball(self, inter, вопрос):
        otvet = random.choice(["Да", "Может быть да", "Нет", "Может быть нет", "Я не знаю, спроси ещё раз", "Хммм... дай подумать", "Слишком сложно, чтобы дать ответ"])
        embed = disnake.Embed(title="Шар предсказаний",
                                        color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.add_field(name="> Вопрос:", value=f"{вопрос}")
        embed.add_field(name="> Ответ:", value=f"{otvet}")
        embed.set_footer(text=f"AzureBot", icon_url=f"https://cdn.discordapp.com/attachments/698473661312532490/1162085887849541642/sd2.png?ex=653aa7d2&is=652832d2&hm=4331d032f166c174311808bbe6dc001bfe05335899076fde83895090379f5dcb&")
        await inter.response.send_message(embed=embed)

    @bot.slash_command(description="Создаст qr код по вашему запросу.", options=[
        disnake.Option("текст", description="Введите текст или укажите ссылку", type=disnake.OptionType.string, required=True
        ),])
    async def qrcode(self, inter, текст):
        img = qrcode.make(текст)

        img.save('img/qrcode.png')

        embed = disnake.Embed(
                                        color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.set_image(file=disnake.File(fp='img/qrcode.png'))
        embed.set_footer(text=f"AzureBot", icon_url=f"https://cdn.discordapp.com/attachments/698473661312532490/1162085887849541642/sd2.png?ex=653aa7d2&is=652832d2&hm=4331d032f166c174311808bbe6dc001bfe05335899076fde83895090379f5dcb&")
        await inter.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(FunCommand(bot))
print(f"> Extension {__name__} is ready\n----------\n")