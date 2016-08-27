import discord
from discord.ext import commands

class testModule():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, description='Returns Hi + username')
    async def hello(self, ctx):
        await self.bot.say('Hi {}!'.format(ctx.message.author.name))

def setup(bot):
    bot.add_cog(testModule(bot))
    
