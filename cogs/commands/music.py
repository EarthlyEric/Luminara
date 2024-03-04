import discord
import wavelink
from datetime import datetime, timezone
from core.utils import colors,icon,utils,emojis
from discord.ext import commands
from classes import Cogs
from core.config import config
from ui.view import *

class Music(Cogs):
    def __init__(self, bot):
        super().__init__(bot)  

    
        

async def setup(bot):
    await bot.add_cog(Music(bot))