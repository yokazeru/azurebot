import disnake
from disnake.ext import commands
import os
import asyncio.tasks
from asyncio.tasks import sleep
import datetime
from disnake.utils import format_dt
from disnake.enums import ButtonStyle
from disnake.ui import View
from bonus import bonus

intents = disnake.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents)

class RowButtons(disnake.ui.View):
        def __init__(self):
            super().__init__(timeout=None)

            self.add_item(disnake.ui.Button(url="https://discord.gg/6pvBUgreQ8", label=f"Сервер поддержки", style=disnake.ButtonStyle.grey))

class RowButtons2(disnake.ui.View):
        def __init__(self):
            super().__init__(timeout=None)

            self.add_item(disnake.ui.Button(emoji="<:verified:1162374085544771594>", label=f"Офицальное сообщество AzureBot!", style=disnake.ButtonStyle.grey, disabled=True))

class InfoCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.slash_command(description="Показывает список команд и помогает в их использовании.")
    async def help(interaction):
        embed=disnake.Embed(title="Список команд", color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.add_field(name="> Информация:", value="- </help:1162080903783264396> — Показывает список команд и помогает в их использовании.\n- </about:1162343074916216893> — Покажет подробную информацию о боте.\n- </user:1162350614353805355> — Информация о пользователе.\n- </avatar:1162352556454977566> — Аватар пользователя.\n- </stats:1162356556730474496> — Показывает текущую статистику бота.\n- </server:1162367500135178271> — Отображает полную информацию о сервере.", inline=True)
        embed.add_field(name="> Развлечения:", value="- </ball:1162395911809417346> — Шар с предсказаниями. Который ответит на ваш вопрос.\n- </coinflip:1162396888792825936> — Подбросить монетку. И проверить свою удачу.\n- </qrcode:1162414094293401703> — Создаст qr код по вашему запросу.", inline=True)
        embed.add_field(name="> Премиум команды:", value="- </ai:1162336738853781524> — Сгенерирует ответ на вопрос по запросу пользователя.", inline=True)
        embed.set_footer(text=f"AzureBot", icon_url=f"https://cdn.discordapp.com/attachments/698473661312532490/1162085887849541642/sd2.png?ex=653aa7d2&is=652832d2&hm=4331d032f166c174311808bbe6dc001bfe05335899076fde83895090379f5dcb&")
        await interaction.response.send_message(embed=embed)

    @bot.slash_command(description="Покажет подробную информацию о боте.")
    async def about(interaction):
        embed=disnake.Embed(title=f"AzureBot", color=0x2e2f33, timestamp=datetime.datetime.now())
        embed.add_field(name="> Язык программирования:", value="<:disnake:1162344907164364870> Disnake 2.4.0")
        embed.add_field(name="> Версия:", value="1.0")
        embed.add_field(name="> Разработчик:", value="<:yooshito:1162345956679888896> yooshito.")
        embed.set_footer(text=f"AzureBot", icon_url=f"https://cdn.discordapp.com/attachments/698473661312532490/1162085887849541642/sd2.png?ex=653aa7d2&is=652832d2&hm=4331d032f166c174311808bbe6dc001bfe05335899076fde83895090379f5dcb&")
        embed.set_thumbnail(url=f"https://cdn.discordapp.com/attachments/698473661312532490/1162085887849541642/sd2.png?ex=653aa7d2&is=652832d2&hm=4331d032f166c174311808bbe6dc001bfe05335899076fde83895090379f5dcb&")
        await interaction.response.send_message(embed=embed, view=RowButtons())

    @bot.slash_command(description="Информация о пользователе.", options=[
        disnake.Option("пользователь", description="Выберите пользователя", type=disnake.OptionType.user, required=False
        ),])
    async def user(interaction, пользователь: disnake.Member = commands.Param(lambda inter: inter.author)):
        if пользователь == None:
            created_at = format_dt(interaction.author.created_at, 'D')
            joined_at = format_dt(interaction.author.joined_at, 'D')
            embed=disnake.Embed(title=f"Информация о {interaction.author.name}", color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.add_field(name="> Дата создания аккаунта:", value=f"{created_at}", inline=True)
            embed.add_field(name="> Дата присоединения:", value=f"{joined_at}", inline=True)
            embed.set_footer(text=f"AzureBot", icon_url=f"https://cdn.discordapp.com/attachments/698473661312532490/1162085887849541642/sd2.png?ex=653aa7d2&is=652832d2&hm=4331d032f166c174311808bbe6dc001bfe05335899076fde83895090379f5dcb&")
            embed.set_thumbnail(url=f"{interaction.author.avatar}")
            await interaction.response.send_message(embed=embed)
        else:
            created_at = format_dt(пользователь.created_at, 'D')
            joined_at = format_dt(пользователь.joined_at, 'D')
            embed=disnake.Embed(title=f"Информация о {пользователь.name}", color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.add_field(name="> Дата создания аккаунта:", value=f"{created_at}", inline=True)
            embed.add_field(name="> Дата присоединения:", value=f"{joined_at}", inline=True)
            embed.set_footer(text=f"AzureBot", icon_url=f"https://cdn.discordapp.com/attachments/698473661312532490/1162085887849541642/sd2.png?ex=653aa7d2&is=652832d2&hm=4331d032f166c174311808bbe6dc001bfe05335899076fde83895090379f5dcb&")
            embed.set_thumbnail(url=f"{пользователь.avatar}")
            await interaction.response.send_message(embed=embed)

    @bot.slash_command(description="Аватар пользователя.", options=[
        disnake.Option("пользователь", description="Выберите пользователя", type=disnake.OptionType.user, required=False
        ),])
    async def avatar(interaction, пользователь: disnake.Member = commands.Param(lambda inter: inter.author)):
        if пользователь == None:
            embed=disnake.Embed(title=f"Аватар {пользователь.name}", color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"AzureBot", icon_url=f"https://cdn.discordapp.com/attachments/698473661312532490/1162085887849541642/sd2.png?ex=653aa7d2&is=652832d2&hm=4331d032f166c174311808bbe6dc001bfe05335899076fde83895090379f5dcb&")
            embed.set_image(url=f"{interaction.author.avatar}")
            await interaction.response.send_message(embed=embed)
        else:
            embed=disnake.Embed(title=f"Аватар {пользователь.name}", color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"AzureBot", icon_url=f"https://cdn.discordapp.com/attachments/698473661312532490/1162085887849541642/sd2.png?ex=653aa7d2&is=652832d2&hm=4331d032f166c174311808bbe6dc001bfe05335899076fde83895090379f5dcb&")
            embed.set_image(url=f"{пользователь.avatar}")
            await interaction.response.send_message(embed=embed)

    @bot.slash_command(description="Отображает полную информацию о сервере.")
    async def server(interaction):
        ha1 = str(interaction.guild.verification_level)
        ha0 = ha1.replace("very_high", "Очень высокая")
        ha2 = ha0.replace("high", "Высокая")
        ha3 = ha2.replace("medium", "Средняя")
        ha4 = ha3.replace("low", "Низкая")
        ha = ha4.replace("none", "null")
        total_member = interaction.guild.member_count
        max_member = interaction.guild.max_members
        total_channel = len(interaction.guild.channels)
        afk_c = interaction.guild.afk_channel
        voice_channel = len(interaction.guild.voice_channels)
        roles_1 = len(interaction.guild.roles)
        roles = int(roles_1 - 1)
        bot = len(list(filter(lambda m: m.bot, interaction.guild.members)))
        totals_members = int(total_member - bot)
        cr_1 = format_dt(interaction.guild.created_at, 'D')
        cr_2 = format_dt(interaction.guild.created_at, 'R')
        bon = bonus
        if interaction.guild.id == 1162050199057862768:
            embed=disnake.Embed(title=f"Информация о сервере {interaction.guild.name}", color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.add_field(name='> Участники:', value=f'Всего: **{total_member}**\nБоты: **{bot}**\nУчастники: **{totals_members}**', inline=True)
            embed.add_field(name='> Каналы:', value=f'Всего Каналов: **{total_channel}**\nТекстовые: **{len(interaction.guild.text_channels)}**\nГолосовые: **{voice_channel}**', inline=True)
            embed.add_field(name='> Информация:', value=f'Кол-во ролей: **{roles}**\nЭмоджи: **{len(interaction.guild.emojis)}**\nСтикеры: **{len(interaction.guild.stickers)}**\n', inline=True)
            embed.add_field(name='', value=f'Владелец: <@!{interaction.guild.owner_id}>\nДата создания сервера: {cr_1} ({cr_2})\nУровень проверки: **{ha}**', inline=False)
            embed.add_field(name='', value=f'**На данном сервере активирован премиум! :blue_heart:**', inline=False)
            embed.set_footer(text=f"AzureBot", icon_url=f"https://cdn.discordapp.com/attachments/698473661312532490/1162085887849541642/sd2.png?ex=653aa7d2&is=652832d2&hm=4331d032f166c174311808bbe6dc001bfe05335899076fde83895090379f5dcb&")
            embed.set_thumbnail(url=interaction.guild.icon)
            await interaction.response.send_message(embed=embed, view=RowButtons2())
        else:
            if f"{interaction.guild.id}" in bon:
                embed=disnake.Embed(title=f"Информация о сервере {interaction.guild.name}", color=0x2e2f33, timestamp=datetime.datetime.now())
                embed.add_field(name='> Участники:', value=f'Всего: **{total_member}**\nБоты: **{bot}**\nУчастники: **{totals_members}**', inline=True)
                embed.add_field(name='> Каналы:', value=f'Всего Каналов: **{total_channel}**\nТекстовые: **{len(interaction.guild.text_channels)}**\nГолосовые: **{voice_channel}**', inline=True)
                embed.add_field(name='> Информация:', value=f'Кол-во ролей: **{roles}**\nЭмоджи: **{len(interaction.guild.emojis)}**\nСтикеры: **{len(interaction.guild.stickers)}**\n', inline=True)
                embed.add_field(name='', value=f'Владелец: <@!{interaction.guild.owner_id}>\nДата создания сервера: {cr_1} ({cr_2})\nУровень проверки: **{ha}**', inline=False)
                embed.add_field(name='', value=f'**На данном сервере активирован премиум! :blue_heart:**', inline=False)
                embed.set_footer(text=f"AzureBot", icon_url=f"https://cdn.discordapp.com/attachments/698473661312532490/1162085887849541642/sd2.png?ex=653aa7d2&is=652832d2&hm=4331d032f166c174311808bbe6dc001bfe05335899076fde83895090379f5dcb&")
                embed.set_thumbnail(url=interaction.guild.icon)
                await interaction.response.send_message(embed=embed)
            else:
                embed=disnake.Embed(title=f"Информация о сервере {interaction.guild.name}", color=0x2e2f33, timestamp=datetime.datetime.now())
                embed.add_field(name='> Участники:', value=f'Всего: **{total_member}**\nБоты: **{bot}**\nУчастники: **{totals_members}**', inline=True)
                embed.add_field(name='> Каналы:', value=f'Всего Каналов: **{total_channel}**\nТекстовые: **{len(interaction.guild.text_channels)}**\nГолосовые: **{voice_channel}**', inline=True)
                embed.add_field(name='> Информация:', value=f'Кол-во ролей: **{roles}**\nЭмоджи: **{len(interaction.guild.emojis)}**\nСтикеры: **{len(interaction.guild.stickers)}**\n', inline=True)
                embed.add_field(name='', value=f'Владелец: <@!{interaction.guild.owner_id}>\nДата создания сервера: {cr_1} ({cr_2})\nУровень проверки: **{ha}**', inline=False)
                embed.set_footer(text=f"AzureBot", icon_url=f"https://cdn.discordapp.com/attachments/698473661312532490/1162085887849541642/sd2.png?ex=653aa7d2&is=652832d2&hm=4331d032f166c174311808bbe6dc001bfe05335899076fde83895090379f5dcb&")
                embed.set_thumbnail(url=interaction.guild.icon)
                await interaction.response.send_message(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(InfoCommand(bot))
print(f"> Extension {__name__} is ready\n----------\n")