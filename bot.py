import discord
from discord.ext import commands

bot = commands.Bot(command_Prefix='%')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context = True)
async def kick(ctx, userName: discord.User):
    await bot.kick(userName)
