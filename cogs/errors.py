# -*- coding: UTF-8 -*-
import discord,asyncio
from discord.ext import commands
from discord.ext import *
from core.config import *
from core.classes import CogTop
from core.dbwork import *


class errors(CogTop):

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("遺失必要參數")
        else:
            await ctx.send(f'未知錯誤{error}')


def setup(bot):
    bot.add_cog(errors(bot))
