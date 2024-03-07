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
        embed = discord.Embed('')
        if not ctx.guild:
            return await ctx.send('')
    
        player : wavelink.Player
        player = cast(wavelink.Player, ctx.voice_client)
        
        if not player:
            try:
                player = await ctx.author.voice.channel.connect(cls=wavelink.Player)  # type: ignore
            except AttributeError:
                return await ctx.send("Please join a voice channel first before using this command.")
                
            except discord.ClientException:
                return await ctx.send("I was unable to join this voice channel. Please try again.")
                

    
        

async def setup(bot):
    await bot.add_cog(Music(bot))