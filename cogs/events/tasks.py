# -*- coding: UTF-8 -*-
import discord
from discord.ext import tasks,commands

class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
        self.update_status.start()

    @tasks.loop(seconds=60)
    async def update_status(self):
       await self.bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.streaming, name ="%shelp｜在 %s 個伺服器中"%(self.bot.command_prefix,str(len(self.bot.guilds))))
        )
         
    @update_status.before_loop
    async def before_update_ststus(self):
        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(Tasks(bot))