# -*- coding: UTF-8 -*-
import nextcord
from nextcord.ext import commands
from core.config import *
from core.classes import CogTop
from core.db import *

class Events(CogTop):
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        guild_join(guild=guild)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        guild_remove(guild=guild)

def setup(bot):
    bot.add_cog(Events(bot))
