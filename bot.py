import discord
from discord.ext import commands

bot = commands.Bot(command_Prefix='%')

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
bot.run('NDYxOTUzNTk5NDI2MDAyOTU2.Dh_47w.V34Te-LudmfY9aPGGvkml4MYAKo')
