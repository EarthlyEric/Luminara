# -*- coding: UTF-8 -*-
import nextcord
import bot
from nextcord.ext import commands
from nextcord.ext import *
from core.config import *
from core.classes import Cogs
from core.db import *
from core.embed_color import colors


class Errors(Cogs):
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed=nextcord.Embed(title=f":question:  {ctx.author.name} 遺失必要參數 ",color=colors.red)
            embed.add_field(name=f"{error}",value='NULL')
            embed.set_footer(text=f"Lost", icon_url=bot.icon_url)

            await ctx.send(embed=embed)
        else:
            embed=nextcord.Embed(title=f":question:  {ctx.author.name} 未知錯誤 ",color=colors.red)
            embed.add_field(name=f"{error}",value='NULL')
            embed.set_footer(text=f"Lost", icon_url=bot.icon_url)
            
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Errors(bot))
