import discord #import the discord.py lib
from discord.ext import commands #import the commands extension
import asyncio #import asyncio for the sleep function

description ='''
challengeBot is a discord bot that provides weekly coding challenges
from /r/dailyprogrammer. Bot created by the fellows of /r/programming
''' #description of the bot

#list of modules that the bot imports
startup_extensions = ['testModule'] 

#init the bot class, the prefix for the commands, the bot description and help
bot = commands.Bot(command_prefix='!', description=description, pm_help=True)


#Makes a background task
async def background_task():
    #starts when the bot is done loading
    await bot.wait_until_ready()
    #while is True while the bot is active
    while not bot.is_closed:
        #Bot prints 'I am alive' every 5 seconds to your console
        print('I am alive')
        await asyncio.sleep(5)
        
@bot.event
#triggers when the bot is done loading
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    #loads all the extions mentioned in the list above
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

@bot.command(description='Returns pong')
#triggers when you type prefix+function name, so: !ping
async def ping():
    #await is a asyncio keyword and bot.say types something out in discord
    await bot.say('pong')

#starts the background tasks in another loop
bot.loop.create_task(background_task())
#starts the bot, you need to put in your bot token here obtained by discord    
bot.run('')
