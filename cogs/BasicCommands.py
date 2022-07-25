# -*- coding: UTF-8 -*-
import nextcord
import bot
from datetime import datetime
from nextcord.ext import *
from nextcord.ext import commands
from core.classes import CogTop
from core.config import *
from core.lib  import *

class BasicCommands(CogTop):

    @commands.command()
    async def help(self, ctx:commands.Context):
        embed=nextcord.Embed(title="Lost 基本命令列表", color=0x0162b7) #blue
        embed.add_field(name="`e!help`", value="顯示命令列表", inline=True)
        embed.add_field(name="`e!ping`", value="顯示Lost 狀態", inline=True)
        embed.set_footer(text="Lost", icon_url=bot.icon_url)

        await ctx.reply(embed=embed)
 
    @commands.command()
    async def ping(self, ctx:commands.Context):
        delta_uptime = datetime.utcnow() - self.bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        embed=nextcord.Embed(title="Lost 狀態", color=0x0162b7)#blue
        embed.add_field(name="Bot Core 版本", value=f"{version} :flag_tw: ", inline=False)
        embed.add_field(name="提供服務的伺服器數",value=f"{len(self.bot.guilds)}", inline= False)
        embed.add_field(name="目前延遲", value=f"{round(self.bot.latency*1000)} ms", inline=False)
        embed.add_field(name="已運作時間", value=f"{days} d, {hours} h, {minutes} m, {seconds} s", inline=False)
        embed.set_footer(text="Lost", icon_url=bot.icon_url)

        await ctx.reply(embed=embed)
    
        
def setup(bot):
    bot.add_cog(BasicCommands(bot))