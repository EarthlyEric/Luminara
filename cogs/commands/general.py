# -*- coding: UTF-8 -*-
import discord
import psutil
import wavelink
from datetime import datetime,timezone
from discord.ext import commands

from classes import Cogs
from core.config import config
from ui.view import *
from core.utils import colors,icon,utils,emojis

class General(Cogs):
    @commands.hybrid_command(name="help", description="查看Luminara的使用指南", with_app_command=True)
    async def help(self, ctx: commands.Context):
        view=HelpView()
        
        embed=discord.Embed(color=colors.purple,timestamp=datetime.now())
        embed.set_author(name="Luminara使用指南",icon_url=icon.guide_icon_url,url="https://blog.earthlyeric6.ml/")
        embed.add_field(name="Hello，我是Luminara，很高興見到你!",value="你可以從下面選擇想看的命令類別。")
        embed.set_footer(text="Luminara")

        return await ctx.reply(embed=embed,view=view)
 
    @commands.hybrid_command(name="ping", description="查看Luminara的狀態", with_app_command=True)
    async def ping(self, ctx: commands.Context):
        bot_uptime = datetime.now(timezone.utc) - self.bot.launch_time
        hours, remainder = divmod(int(bot_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        cpu_usage=psutil.cpu_percent(interval=0.3)
        usage_bar=utils.processesBar(level=int(round(cpu_usage,0)))
        ram=psutil.virtual_memory()
        ram_usage=ram.percent
        usage_bar=utils.processesBar(level=int(round(ram_usage,0)))
        
        embed=discord.Embed(color=colors.purple,timestamp=datetime.now())
        embed.timestamp="Luminara狀態"
        embed.add_field(name="%s | CPU"%(emojis.CPU),value=f"`{cpu_usage}%{usage_bar}`",inline=True)
        embed.add_field(name="%s | RAM"%(emojis.RAM),value=f"`{ram_usage}%{usage_bar}`",inline=True)
        embed.add_field(name="%s | 伺服器數量"%(emojis.server),value="`%s個`"%((str(len(self.bot.guilds)))),inline=False)
        embed.add_field(name="%s | Discord API狀態"%(emojis.discord_api), value="`%s ms`"%(str(round(self.bot.latency*1000))), inline=False)
        embed.add_field(name="%s Luminara上線時間(本次進程)"%(emojis.clock), value="`%s d, %s h, %s m, %s s`"%(days,hours,minutes,seconds), inline=False)
        embed.add_field(name="%s | Bot Version"%(emojis.Lost),value=" `%s`<:beta:1013696625031520276>"%(config.version),inline=False)
        embed.set_footer(text="Luminara")

        return await ctx.reply(embed=embed)
   
async def setup(bot):
    await bot.add_cog(General(bot))