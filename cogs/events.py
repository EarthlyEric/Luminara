# -*- coding: UTF-8 -*-
import nextcord
from nextcord.ext import commands
from core.config import *
from core.classes import Cogs
from core.db import *

class Events(Cogs):
    @commands.Cog.listener()
    async def on_guild_join(self, guild:nextcord.Guild):
        print('%s'%(guild.name))

def setup(bot):
    bot.add_cog(Events(bot))
