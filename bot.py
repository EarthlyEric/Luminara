# -*- coding: UTF-8 -*-
import discord,os,core.uptime.uptime
from discord.ext import commands
from datetime import datetime
from core.config import *


intents=discord.Intents.all()

bot = commands.Bot(command_prefix='>',intents=intents)
bot.remove_command("help")
bot.launch_time = datetime.utcnow()




@bot.event
async def on_ready():
    
    print("Alice is online")
    print(f"Login as {bot.user}")
    print(f"Alice Version: {printversion}")
    print(f"Discord.py API Version: {discord.__version__}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name =f"{bot.command_prefix}help"))

for coglist in os.listdir('./cogs'):
	if coglist.endswith('.py'):
		bot.load_extension(f'cogs.{coglist[:-3]}')



core.uptime.uptime.keep_alive()


bot.run(token)
