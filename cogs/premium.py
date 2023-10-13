import disnake
from disnake.ext import commands
import os
import asyncio.tasks
from asyncio.tasks import sleep
import datetime
import openai
from disnake.enums import ButtonStyle
from disnake.ui import View
from bonus import bonus

token_openai = "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"
openai.api_key = token_openai
intents = disnake.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents)

class RowButtons(disnake.ui.View):
        def __init__(self):
            super().__init__(timeout=None)

            self.add_item(disnake.ui.Button(url="https://boosty.to/azurebot", label=f"Boosty", style=disnake.ButtonStyle.grey))

class PremiumCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.slash_command(description="Сгенерирует ответ на вопрос по запросу пользователя.", options=[
        disnake.Option(
            "запрос", description="Введите ваш запрос", type=disnake.OptionType.string, required=True
            ),],)
    async def ai(interaction, *, запрос):
        bon = bonus
        if f"{interaction.guild.id}" in bon:
            await interaction.response.defer()
            result = str(запрос)
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=result,
                temperature=0.9,
                max_tokens=1000,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.6,
                stop=["You:"]
            )
            embed=disnake.Embed(title=f"{result}", description=response['choices'][0]['text'], color=0x2e2f33, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"AzureBot", icon_url=f"https://cdn.discordapp.com/attachments/698473661312532490/1162085887849541642/sd2.png?ex=653aa7d2&is=652832d2&hm=4331d032f166c174311808bbe6dc001bfe05335899076fde83895090379f5dcb&")
            await interaction.followup.send(embed=embed)
        else:
            embed=disnake.Embed(title=f"Ошибка!", description="Премиум функция будет доступна только за поддержку проекта.\n\nЕсли вы оплатили премиум, но вам не выдали подписку. Подождите некоторое время или напишите в поддержку сервера.", color=0xff4d4d, timestamp=datetime.datetime.now())
            embed.set_footer(text=f"AzureBot", icon_url=f"https://cdn.discordapp.com/attachments/698473661312532490/1162085887849541642/sd2.png?ex=653aa7d2&is=652832d2&hm=4331d032f166c174311808bbe6dc001bfe05335899076fde83895090379f5dcb&")
            await interaction.response.send_message(embed=embed, view=RowButtons(), ephemeral=True)

def setup(bot: commands.Bot):
    bot.add_cog(PremiumCommand(bot))
print(f"> Extension {__name__} is ready\n----------\n")