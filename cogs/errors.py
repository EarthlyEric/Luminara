# -*- coding: UTF-8 -*-
import nextcord
from nextcord.ext import commands
from core.config import *
from core.classes import Cogs
from core.utils import colors,icon

class Errors(Cogs):
    @commands.Cog.listener()
    async def on_command_error(self, ctx:commands.Context, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed=nextcord.Embed(color=colors.red)
            embed.add_field(name=':question: 遺失必要參數',value='%s'%(error))
            embed.set_footer(text='Lost', icon_url=icon.icon_url)

            return await ctx.send(embed=embed)
        if isinstance(error,commands.CommandNotFound):
            embed=nextcord.Embed(color=colors.red)
            embed.add_field(name=':question: 未知命令',value='%s'%(error))
            embed.set_footer(text='Lost', icon_url=icon.icon_url)

            return await ctx.send(embed=embed)
        else:
            embed=nextcord.Embed(color=colors.red)
            embed.add_field(name=':question: 未知錯誤',value='%s'%(error))
            embed.set_footer(text='Lost', icon_url=icon.icon_url)
            
            return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Errors(bot))
