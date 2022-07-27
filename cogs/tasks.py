import nextcord
from nextcord.ext import tasks,commands

class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        self.update_ststus.start()

    @tasks.loop(seconds=60)
    async def update_ststus(self):
       await self.bot.change_presence(
        activity=nextcord.Activity(type=nextcord.ActivityType.streaming, name =f"{self.bot.command_prefix}help｜Watch {len(self.bot.guilds)} servers")
        )
        
    @update_ststus.before_loop
    async def before_update_ststus(self):
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(Tasks(bot))