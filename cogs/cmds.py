# -*- coding: UTF-8 -*-
from os import name
import discord,pymysql,humanize
from discord import embeds
from datetime import datetime
from discord.ext import *
from discord.ext import commands
from core.classes import CogTop
from core.config import *
from core.lib  import *


class Basiccmds(CogTop):

    @commands.group()
    async def help(self, ctx):
        embed=discord.Embed(title="Alice 命令列表", color=0x0162b7)#blue
        embed.add_field(name="`a!help`", value="顯示命令列表", inline=True)
        embed.add_field(name="`a!ping`", value="顯示Alice 狀態", inline=True)
        embed.add_field(name="`a!set`", value="設定專用指令", inline=True)
        embed.add_field(name="`a!imgall`", value="隨機Alice圖片(all)", inline=True)
        embed.set_footer(text=f"Alice Plus", icon_url="https://raw.githubusercontent.com/EarthlyEric/Alice-RES/master/Alice-icon.png")
        await ctx.send(embed=embed)
    
    @help.command()
    async def set(swlf, ctx):
        embed=discord.Embed(title="`a!set`命令列表", color=0x0162b)#blue
        embed.add_field(name="`a!set <參數>`", value= "以下為參數", inline=False)
        embed.add_field(name="`come`", value="設定此處為歡迎訊息發出頻道")
        embed.set_footer(text=f"Alice Plus", icon_url="https://raw.githubusercontent.com/EarthlyEric/Alice-RES/master/Alice-icon.png")
        await ctx.send(embed=embed)
 
    @commands.command()
    async def ping(self, ctx):
        delta_uptime = datetime.utcnow() - self.bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        embed=discord.Embed(title="Alice Plus 狀態", color=0x0162b7)#blue
        embed.add_field(name="Bot Core 版本", value=f"{printversion} :flag_tw: ", inline=False)
        embed.add_field(name="提供服務的伺服器數",value=f"{len(self.bot.guilds)}", inline= False)
        embed.add_field(name="目前延遲", value=f"{round(self.bot.latency*1000)} ms", inline=False)
        embed.add_field(name="已運作時間", value=f"{days} d, {hours} h, {minutes} m, {seconds} s", inline=False)
        embed.set_footer(text=f"Alice Plus", icon_url="https://raw.githubusercontent.com/EarthlyEric/Alice-RES/master/Alice-icon.png")
        await ctx.send(embed=embed)
    
    @commands.group()
    @commands.is_owner()
    async def set(self, ctx):
        pass

    @commands.command()
    async def imgall(self, ctx):
        imgurl = randomimgall()

        embed=discord.Embed(title=":minidisc:", color=0x0162b7)#blue
        embed.set_image(url=f"{imgurl}")
        embed.set_footer(text=f"Alice Plus", icon_url="https://raw.githubusercontent.com/EarthlyEric/Alice-RES/master/Alice-icon.png")
        await ctx.send(embed=embed)
        
        
def setup(bot):
    bot.add_cog(Basiccmds(bot))