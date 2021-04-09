import discord
from discord.ext import commands
import requests

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!weeb ')

@bot.event
async def on_ready():
	print("Bot running.")
	print(f"{discord.__version__}")

@bot.command(name="anime")
async def joe(ctx, arg):
	argument = str(arg)
	results = requests.get(f"https://api.jikan.moe/v3/search/anime?q={argument}&limit=1")
	for i in results.json()["results"]:
		embed=discord.Embed(title=f'{i["title"]}', url=f'{i["url"]}', description=f'{i["synopsis"]}', color=0x5800db)
		embed.set_image(url=f'{i["image_url"]}')
		await ctx.send(embed=embed)

@bot.command(name="manga")
async def joe(ctx, arg):
	argument = str(arg)
	results = requests.get(f"https://api.jikan.moe/v3/search/manga?q={argument}&limit=1")
	for i in results.json()["results"]:
		embed=discord.Embed(title=f'{i["title"]}', url=f'{i["url"]}', description=f'{i["synopsis"]}', color=0x5800db)
		embed.set_image(url=f'{i["image_url"]}')
		await ctx.send(embed=embed)

bot.run('#CLIENTID')