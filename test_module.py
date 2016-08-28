import discord
from discord.ext import commands

class testModule():
    #get bot class, you need this to do things such as bot.say
    def __init__(self, bot):
        self.bot = bot

    #Pass_contenxt True to get the message the user send
    @commands.command(pass_context=True, description='Returns Hi + username')
    #You can acces the message object throufh ctx
    async def hello(self, ctx):
        #here I actually use the ctx object to get the author's name
        await self.bot.say('Hi {}!'.format(ctx.message.author.name))

#every module requires a setup function, you need to pass bot
def setup(bot):
    #You add the cog to the main program, use bot.add_cog(modulename(bot))
    bot.add_cog(testModule(bot))
    
