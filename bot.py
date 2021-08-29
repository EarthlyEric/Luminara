# -*- coding: UTF-8 -*-
import discord,json,os,time,core.uptime.uptime
from discord.ext import commands
from discord.ext import *
from datetime import datetime
from core.classes import CogTop
from core.json_loader import *

intents=discord.Intents.all()

bot = commands.Bot(command_prefix='>',intents=intents)
bot.remove_command("help")
bot.launch_time = datetime.utcnow()

out=0

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

bot.load_extension('core.debugcmds')


core.uptime.uptime.keep_alive()

if __name__ == "__main__":
     bot.run(token)
