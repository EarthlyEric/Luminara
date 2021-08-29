# -*- coding: UTF-8 -*-
import discord,time
from discord import*
from discord.ext import *
from discord.ext import commands
from core.classes import CogTop
from core.json_loader import *
from bot import *

class Debug(CogTop):
 pass


def setup(bot):
    bot.add_cog(Debug(bot))