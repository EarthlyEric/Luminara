# -*- coding: UTF-8 -*-
import discord
from discord.ext import commands
from core.config import *
from classes import Cogs

class Events(Cogs):
    @commands.Cog.listener()
    async def on_guild_join(self, guild:discord.Guild):
        await print('%s'%(guild.name))

async def setup(bot):
    await bot.add_cog(Events(bot))
