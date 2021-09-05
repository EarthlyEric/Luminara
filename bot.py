# -*- coding: UTF-8 -*-
import discord,os,core.uptime.uptime,time,platform
from discord.ext import commands
from datetime import datetime
from core.config import *
from core.lib import showinfo

core.uptime.uptime.keep_alive()

intents=discord.Intents.all()

bot = commands.Bot(command_prefix='>',intents=intents)
bot.remove_command("help")
bot.launch_time = datetime.utcnow()




@bot.event
async def on_ready():
    logopath='res\logo\logo.txt'
    f=open(logopath, 'r')
    time.sleep(1)
    print('____________________________________________________________________________________________________________')

    print(f.read())

    
    print('____________________________________________________________________________________________________________')
    print('                                                                                                            ')
    time.sleep(1)
    now_type0=datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    showinfo("作業系統",platform.platform())
    showinfo('系統版本',platform.version())
    showinfo('作業系統名稱', platform.system())
    showinfo('系統位數', platform.architecture()[0])
    showinfo('CPU 架構', platform.machine())
    showinfo('系統名稱', platform.node())
    showinfo('處理器', platform.processor())
    print(f'Time:{now_type0}')
    print('____________________________________________________________________________________________________________')
    print('                                                                                                            ')
    time.sleep(1)
    print("Alice is online")
    print(f"Login as {bot.user}")
    print(f"Alice Version: {printversion}")
    print(f"Discord.py API Version: {discord.__version__}")
    print('____________________________________________________________________________________________________________')

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name =f"{bot.command_prefix}help"))

for coglist in os.listdir('./cogs'):
	if coglist.endswith('.py'):
		bot.load_extension(f'cogs.{coglist[:-3]}')

bot.run(token)
