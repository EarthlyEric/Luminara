import discord
from discord.ext import tasks,commands
from core.classes import CogTop

class bot_tasks(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        self.update_ststus.start()

    @tasks.loop(seconds=60)
    async def update_ststus(self):
       await self.bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing, name =f"{self.bot.command_prefix}help｜Watch {len(self.bot.guilds)} servers")
        )
        
    @update_ststus.before_loop
    async def before_update_ststus(self):
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(bot_tasks(bot))