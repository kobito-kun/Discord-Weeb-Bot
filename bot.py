import discord
from discord.ext import commands
import requests

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
	print("Bot running.")
	print(f"{discord.__version__}")

@bot.command(name="anime")
async def anime(ctx, arg):
	argument = str(arg)
	results = requests.get(f"https://api.jikan.moe/v3/search/anime?q={argument}&limit=1")
	for i in results.json()["results"]:
		embed=discord.Embed(title=f'{i["title"]}', url=f'{i["url"]}', description=f'{i["synopsis"]}', color=0x5800db)
		embed.set_image(url=f'{i["image_url"]}')
		msg = await ctx.send(embed=embed)

@bot.command(name="manga")
async def manga(ctx, arg):
	argument = str(arg)
	results = requests.get(f"https://api.jikan.moe/v3/search/manga?q={argument}&limit=1")
	for i in results.json()["results"]:
		embed=discord.Embed(title=f'{i["title"]}', url=f'{i["url"]}', description=f'{i["synopsis"]}', color=0x5800db)
		embed.set_image(url=f'{i["image_url"]}')
		msg = await ctx.send(embed=embed)

@bot.command(name="memes")
async def manga(ctx, arg):
	argument = str(arg)
	res = requests.get("https://api.imgflip.com/get_memes").json()
	res = res['data']['memes']
	names = []
	if argument == "list":
		embed=discord.Embed(title="Top Meme List", description="Will display most of it.")
		embed.set_author(name="Kobi", url="https://kobi.lol", icon_url="https://kobi.lol/media/mika-bg.png")
		for i in res:
			embed.add_field(name=f"{i['id']}", value=f"{i['name']}", inline=False)
		await ctx.send(embed=embed)		
	elif argument != "":
		for i in res:
			if argument.lower() in str(i['name']).lower():
				embed=discord.Embed(title=f"{i['name']}", description=f"{i['id']}")
				embed.set_image(url=f"{i['url']}")
				await ctx.send(embed=embed)
	else:
		await ctx.send("OOF, looks like there is a problem here, please do `!>memes <list/name>")

bot.run('')