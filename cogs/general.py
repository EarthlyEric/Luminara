# -*- coding: UTF-8 -*-
import nextcord
import bot
import cogs.UI.dropmenu
from datetime import datetime
from core.embed_color import colors
from nextcord.ext import commands
from core.classes import Cogs
from core.config import config
from core.lib  import *


class General(Cogs):
    @commands.command()
    async def help(self, ctx:commands.Context):
        view=cogs.UI.dropmenu.HelpView()

        embed=nextcord.Embed(color=colors.purple)
        embed.set_author(name='歡迎使用 Lost !!',icon_url=bot.icon_url,url='https://blog.earthlyeric6.ml/')
        embed.add_field(name='Hello，我是Lost，很高興見到你!',value='你可以從下面選擇想看的指令使')
        embed.set_footer(text="Lost", icon_url=bot.icon_url)

        await ctx.reply(embed=embed,view=view)
 
    @commands.command()
    async def ping(self, ctx:commands.Context):
        delta_uptime = datetime.utcnow() - self.bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        embed=nextcord.Embed(title="Lost 狀態", color=colors.purple)#blue
        embed.add_field(name="Bot Core 版本", value=f"{config.version} :flag_tw: ", inline=False)
        embed.add_field(name="提供服務的伺服器數",value=f"{len(self.bot.guilds)}", inline= False)
        embed.add_field(name="目前延遲", value=f"{round(self.bot.latency*1000)} ms", inline=False)
        embed.add_field(name="已運作時間", value=f"{days} d, {hours} h, {minutes} m, {seconds} s", inline=False)
        embed.set_footer(text="Lost", icon_url=bot.icon_url)

        await ctx.reply(embed=embed)
    
        
def setup(bot):
    bot.add_cog(General(bot))