# -*- coding: UTF-8 -*-
import nextcord
import psutil
from datetime import datetime
from core.utils import colors,icon,utils,emojis
from nextcord.ext import commands
from core.classes import Cogs
from core.config import config
from ui.view import *

class General(Cogs):
    @commands.command(name='help')
    async def help(self, ctx:commands.Context):
        view=HelpView()
        embed=nextcord.Embed(color=colors.purple,timestamp=datetime.now())
        embed.set_author(name='Lost使用指南',icon_url=icon.guide_icon_url,url='https://blog.earthlyeric6.ml/')
        embed.add_field(name='Hello，我是Lost，很高興見到你!',value='你可以從下面選擇想看的指令使令用法類別。')
        embed.set_footer(text="Lost", icon_url=icon.icon_url)

        await ctx.reply(embed=embed,view=view)
 
    @commands.command(name='ping')
    async def ping(self, ctx:commands.Context):
        bot_uptime = datetime.utcnow() - self.bot.launch_time
        hours, remainder = divmod(int(bot_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        embed=nextcord.Embed(color=colors.purple,timestamp=datetime.now())
        embed.insert_field_at
        embed.set_author(name='Lost狀態',icon_url=icon.icon_url,url='https://blog.earthlyeric6.ml/')
        # CPU Usage
        cpu_usage=psutil.cpu_percent(interval=0.3)
        usage_bar=utils.processesBar(level=int(round(cpu_usage,0)))
        embed.add_field(name='%s|CPU'%(emojis.CPU),value=f'`{cpu_usage}%{usage_bar}`',inline=True)
        # RAM Usage
        ram=psutil.virtual_memory()
        ram_usage=ram.percent
        usage_bar=utils.processesBar(level=int(round(ram_usage,0)))
        embed.add_field(name='%s|RAM'%(emojis.RAM),value=f'`{ram_usage}%{usage_bar}`',inline=True)
        # Bot Info
        embed.add_field(name='%s|伺服器數量'%(emojis.server),value='`%s個`'%((str(len(self.bot.guilds)))),inline=False)
        embed.add_field(name='%s|Discord API狀態'%(emojis.discord_api), value='`%s ms`'%(str(round(self.bot.latency*1000))), inline=False)
        embed.add_field(name='%s Lost上線時間(本次進程)'%(emojis.clock), value='`%s d, %s h, %s m, %s s`'%(days,hours,minutes,seconds), inline=False)
        embed.add_field(name='%s|Bot Version'%(emojis.Lost),value=' `%s`<:beta:1013696625031520276>'%(config.version),inline=False)
        # Footer
        embed.set_footer(text='Lost', icon_url=icon.icon_url)

        return await ctx.reply(embed=embed)

    
    
def setup(bot):
    bot.add_cog(General(bot))