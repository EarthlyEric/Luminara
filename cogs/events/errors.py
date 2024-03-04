# -*- coding: UTF-8 -*-
from datetime import datetime
import discord
from discord.ext import commands
from core.config import *
from classes import Cogs
from core.utils import colors,icon

class Errors(Cogs):
    @commands.Cog.listener()
    async def on_command_error(self, ctx:commands.Context, error):
        print(error)
        if isinstance(error, commands.MissingRequiredArgument):
            embed=discord.Embed(color=colors.red,timestamp=datetime.now())
            embed.add_field(name=':question: 遺失必要參數',value='%s'%(error))
            embed.set_footer(text='Luminara', icon_url=icon.icon_url)

            return await ctx.send(embed=embed)
        if isinstance(error,commands.CommandNotFound):
            embed=discord.Embed(color=colors.red,timestamp=datetime.now())
            embed.add_field(name=':question: 未知命令',value='%s'%(error))
            embed.set_footer(text='Luminara', icon_url=icon.icon_url)

            return await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Errors(bot))
