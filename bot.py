import discord
from discord.ext import commands

bot = (command_Prefix='%')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def kick(ctx, userName: discord.User):
    if True: ctx.message.author.Permissions.administrator
        await BSL.kick(userName)
    else:
        permission_error = str('Sorry ' + ctx.message.author + ' you do not have permissions to do that!')
        await BSL.send_message(ctx.message.channel, permission_error)
