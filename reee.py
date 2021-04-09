import discord
from discord.ext import commands
from googletrans import Translator
from PyDictionary import PyDictionary
dictionary=PyDictionary()
translator = Translator()
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='yeet ')

@bot.event
async def on_ready():
    print("Yeet")
    print(f"{discord.__version__}")

@bot.command()
async def joe(ctx, arg):
    times = int(arg)
    for i in range(times):
        await ctx.send('<@!389739574961766401>')

@bot.command(name="translate")
async def translate(ctx, arg):
	text = str(arg)
	result = translator.translate(text, dest="en")
	await ctx.send(result.text)

@bot.command(name="def")
async def definition(ctx, arg):
	text = str(arg)
	result = dictionary.meaning(text)
	for i in result.values():
		for a in i:
			await ctx.send(f"```{a}```")

bot.run('ODI4NDcxMzE3Nzc4MTM3MTIw.YGqECg.9HKau2HqxXTpbgCdRPiqwjvpu7A')