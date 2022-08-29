# -*- coding: UTF-8 -*-
import nextcord
import cogs.UI.dropmenu
import psutil
from datetime import datetime
from core.utils import colors,icon,utils
from nextcord.ext import commands
from core.classes import Cogs
from core.config import config
from core.lib  import *


class General(Cogs):
    @commands.command()
    async def help(self, ctx:commands.Context):
        view=cogs.UI.dropmenu.HelpView()

        embed=nextcord.Embed(color=colors.purple)
        embed.set_author(name='Lost使用指南',icon_url=icon.guide_icon_url,url='https://blog.earthlyeric6.ml/')
        embed.add_field(name='Hello，我是Lost，很高興見到你!',value='你可以從下面選擇想看的指令使令用法類別。')
        embed.set_footer(text="Lost", icon_url=icon.icon_url)

        await ctx.reply(embed=embed,view=view)
 
    @commands.command()
    async def ping(self, ctx:commands.Context):
        delta_uptime = datetime.utcnow() - self.bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        embed=nextcord.Embed(color=colors.purple)
        embed.set_author(name='Lost狀態',icon_url=icon.icon_url,url='https://blog.earthlyeric6.ml/')
        # CPU Usage
        cpu_usage=psutil.cpu_percent(interval=0.3)
        usage_bar=utils.processesBar(level=int(round(cpu_usage,0)))
        embed.add_field(name='<:CPU:1008034878882852954>|CPU',value=f'`{cpu_usage}%{usage_bar}`',inline=True)
        # RAM Usage
        ram=psutil.virtual_memory()
        ram_usage=ram.percent
        usage_bar=utils.processesBar(level=int(round(ram_usage,0)))
        embed.add_field(name='<:RAM:1008035593894236241>|RAM',value=f'`{ram_usage}%{usage_bar}`',inline=True)

        embed.add_field(name='<:Lost:1008221589231386645> |Bot Version',value='`%s`'%(config.version),inline=False)
        embed.add_field(name='<:server:1008236554042490950> | 伺服器數量',value='`%s個`'%((str(len(self.bot.guilds)))),inline=True)

        
        """
        embed.add_field(name="提供服務的伺服器數",value=f"{len(self.bot.guilds)}", inline= False)
        embed.add_field(name="目前延遲", value=f"{round(self.bot.latency*1000)} ms", inline=False)
        embed.add_field(name="已運作時間", value=f"{days} d, {hours} h, {minutes} m, {seconds} s", inline=False)
        embed.set_footer(text="Lost", icon_url=icon.icon_url)
        """

        await ctx.reply(embed=embed)
    
        
def setup(bot):
    bot.add_cog(General(bot))