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
		msg = await ctx.send(embed=embed)
		await message.add_reaction(msg, emoji='🏃')

@bot.command(name="manga")
async def joe(ctx, arg):
	argument = str(arg)
	results = requests.get(f"https://api.jikan.moe/v3/search/manga?q={argument}&limit=2")
	for i in results.json()["results"]:
		embed=discord.Embed(title=f'{i["title"]}', url=f'{i["url"]}', description=f'{i["synopsis"]}', color=0x5800db)
		embed.set_image(url=f'{i["image_url"]}')
		msg = await ctx.send(embed=embed)
		await msg.add_reaction('🏃')		

@bot.event
async def on_reaction_add(reaction, user):
	if reaction.emoji == "🏃":
		message = reaction.message
		await message.edit(embed="Changed")

bot.run('ODI4NDcxMzE3Nzc4MTM3MTIw.YGqECg.3Vx8kNKpZ5dk96dgbds_ET9WECQ')