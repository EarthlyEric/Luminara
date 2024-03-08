# -*- coding: UTF-8 -*-
import discord
import wavelink
from datetime import datetime, timezone
from core.utils import colors,icon,utils,emojis
from discord.ext import commands
from typing import cast

from classes import Cogs
from core.config import config
from ui.view import *

class Music(Cogs):
    def __init__(self, bot):
        super().__init__(bot)
    
    @commands.command(name='play')
    async def play(self,ctx: commands.Context, *, query: str):
        embed = discord.Embed()
        if not ctx.guild:
            embed.color=colors.red
            embed.timestamp=datetime.now(timezone.utc)
            embed.title="%s | 無法在私人訊息中使用此命令 !" % (emojis.errors)
            embed.set_footer(text='Luminara')
            return await ctx.send(embed=embed)
    
        player : wavelink.Player
        player = cast(wavelink.Player, ctx.voice_client)
        
        if not player:
            try:
                embed.color=colors.green
                embed.timestamp=datetime.now(timezone.utc)
                embed.title="%s | 成功加入您所處的語音頻道 `%s`" % (emojis.success,ctx.author.voice.channel.mention)
                player = await ctx.author.voice.channel.connect(cls=wavelink.Player)  
            except AttributeError:
                return await ctx.send("Please join a voice channel first before using this command.")   
            except discord.ClientException:
                return await ctx.send("I was unable to join this voice channel. Please try again.")
                

    
        

async def setup(bot):
    await bot.add_cog(Music(bot))