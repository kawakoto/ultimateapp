import discord
from discord.ext import commands
token = 'ODU5ODYzNTU0MzI4MTAwODc0.YNy4Vg.iV5KacndtIJlMLd0C9VK6aItfe0'
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
embed = discord.Embed
BOT_PREFIX = '.'
bot = commands.Bot(command_prefix=BOT_PREFIX, case_insensitive=True)


bot.run(token)