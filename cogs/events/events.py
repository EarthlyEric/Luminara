# -*- coding: UTF-8 -*-
import nextcord
from nextcord.ext import commands
from core.config import *
from core.classes import Cogs

class Events(Cogs):
    @commands.Cog.listener()
    async def on_guild_join(self, guild:nextcord.Guild):
        await print('%s'%(guild.name))

def setup(bot):
    bot.add_cog(Events(bot))
