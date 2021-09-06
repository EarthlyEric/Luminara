# -*- coding: UTF-8 -*-
import discord
from discord.ext import commands
from discord.ext import *
from core.config import *
from core.classes import CogTop
from core.dbwork import *


 
class eventlister(CogTop):

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        guild_join(guild=guild)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        guild_remove(guild=guild)


def setup(bot):
    bot.add_cog(eventlister(bot))
