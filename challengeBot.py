import discord
from discord.ext import commands

description ='''
challengeBot is a discord bot that provides weekly coding challenges
from /r/dailyprogrammer. Bot created by the fellows of /r/programming
'''

startup_extensions = ['testModule']

bot = commands.Bot(command_prefix='!', description=description, pm_help=True)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

@bot.command(description='Returns pong')
async def ping():
    await bot.say('pong')
    
bot.run('')
