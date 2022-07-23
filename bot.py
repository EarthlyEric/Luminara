# -*- coding: UTF-8 -*-
import discord
import os
import time
import platform
import core.uptime.uptime
from datetime import datetime
from core.config import *
from core.lib import showinfo
from discord.ext import commands

intents=discord.Intents.all()

bot=commands.Bot(command_prefix='$',intents=intents)
bot.remove_command("help")
bot.launch_time=datetime.utcnow()

icon_url= ""

def starting():
    logopath='./res/logo/logo.txt'
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
    print("Lost is online")
    print(f"Login as {bot.user}")
    print(f"Lost Version: {version}")
    print(f"Discord.py API Version: {discord.__version__}")
    print('____________________________________________________________________________________________________________')

@bot.event
async def on_ready():
    starting()
    time.sleep(2)
    core.uptime.uptime.keep_alive()
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.playing, name =f"{bot.command_prefix}help｜Watch {len(bot.guilds)} server")
        )

for coglist in os.listdir('./cogs'):
	if coglist.endswith('.py'):
		bot.load_extension(f'cogs.{coglist[:-3]}')

bot.run(token)
