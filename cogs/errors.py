# -*- coding: UTF-8 -*-
import discord
import bot
from discord.ext import commands
from discord.ext import *
from core.config import *
from core.classes import CogTop
from core.db import *


class errors(CogTop):

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(title=f":question:  {ctx.author.name} 遺失必要參數 ",color=0xed0202)#Red
            embed.add_field(name=f"{error}",value='NULL')
            embed.set_footer(text=f"Lost", icon_url=bot.icon_url)
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title=f":question:  {ctx.author.name} 未知錯誤 ",color=0xed0202)#Red
            embed.add_field(name=f"{error}",value='NULL')
            embed.set_footer(text=f"Lost", icon_url=bot.icon_url)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(errors(bot))
