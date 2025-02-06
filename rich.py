import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Мы вошли как {bot.user.name}')

billionaires = [
    ("Elon Musk", "$250 миллиардов", "США"),
    ("Bernard Arnault & family", "$194 миллиарда", "Франция"),
    ("Jeff Bezos", "$145 миллиардов", "США"),
    ("Bill Gates", "$110 миллиардов", "США"),
    ("Warren Buffett", "$103 миллиарда", "США"),
    ("Larry Ellison", "$102 миллиарда", "США"),
    ("Larry Page", "$98 миллиардов", "США"),
    ("Sergey Brin", "$96 миллиардов", "США"),
    ("Mukesh Ambani", "$93 миллиарда", "Индия"),
    ("Steve Ballmer", "$91 миллиард", "США")
]

user_favorites = {}

@bot.command(name='richlist')
async def richlist(ctx):
    table_message = "# **Топ 10 богатейших людей мира:**\n"
    for person in billionaires:
        table_message += f"{person[0]}: {person[1]}\n"
    
    table_message += "\nПодробнее: [Самые богатые люди](https://www.securities.io/ru/%D1%81%D0%B0%D0%BC%D1%8B%D0%B5-%D0%B1%D0%BE%D0%B3%D0%B0%D1%82%D1%8B%D0%B5-%D0%BB%D1%8E%D0%B4%D0%B8/)"
    await ctx.send(table_message)

@bot.command(name='strana')
async def strana(ctx):
    country_message = "# **Где живут топ 10 богатейших людей мира:**\n"
    for person in billionaires:
        country_message += f"{person[0]}: {person[2]}\n"
    
    country_message += "\nПодробнее: [Страны, где живут миллиардеры](https://www.forbes.ru/article/45671-strany-gde-zhivut-milliardery?image=13183)"
    await ctx.send(country_message)

@bot.command(name='random_billionaire')
async def random_billionaire(ctx):
    person = random.choice(billionaires)
    message = f"🎲 **Случайный миллиардер:**\n**{person[0]}**\n💰 {person[1]}\n🌍 {person[2]}"
    await ctx.send(message)

@bot.command(name='add_favorite')
async def add_favorite(ctx, *, name: str):
    user_id = ctx.author.id
    if user_id not in user_favorites:
        user_favorites[user_id] = []
    
    for person in billionaires:
        if person[0].lower() == name.lower():
            user_favorites[user_id].append(person)
            await ctx.send(f"✅ {person[0]} добавлен в ваш список любимых миллиардеров!")
            return
    
    await ctx.send("❌ Миллиардер с таким именем не найден.")

@bot.command(name='my_favorites')
async def my_favorites(ctx):
    user_id = ctx.author.id
    if user_id not in user_favorites or not user_favorites[user_id]:
        await ctx.send("📭 Ваш список любимых миллиардеров пуст.")
        return
    
    message = "🌟 **Ваши любимые миллиардеры:**\n"
    for person in user_favorites[user_id]:
        message += f"{person[0]} - {person[1]} ({person[2]})\n"
    
    await ctx.send(message)

bot.run('MTI2NjA2MjE4ODUyNzc1MTIyOQ.GnUzAy.Irkz1Oee-1Gi5Q1AaB00AscehEZ33wHPKkt9GE') 
