# -*- coding: UTF-8 -*-
import nextcord
from nextcord.ext import commands
import os
import time
import platform
import core.uptime.uptime
from datetime import datetime
from core.config import *
from core.lib import showinfo


intents=nextcord.Intents.all()

bot=commands.Bot(command_prefix='$',intents=intents)
bot.remove_command("help")
bot.launch_time=datetime.utcnow()

icon_url= "https://cdn-lost.reload-dev.ml/public/Lost.png"
cogsList=['tasks','events','errors','general','music']

def starting():
    os.system('cls' if os.name=='nt' else 'clear')
    logopath='./res/logo/logo.txt'
    f=open(logopath, 'r')
    print('____________________________________________________________________________________________________________')
    print(f.read())
    time.sleep(0.5)
    print('____________________________________________________________________________________________________________')
    print()
    showinfo("作業系統",platform.platform())
    showinfo('系統版本',platform.version())
    showinfo('作業系統名稱', platform.system())
    showinfo('系統位數', platform.architecture()[0])
    showinfo('CPU 架構', platform.machine())
    showinfo('系統名稱', platform.node())
    showinfo('處理器', platform.processor())
    print('Time:%s'%(datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")))
    print('____________________________________________________________________________________________________________')
    print('                                                                                                            ')
    print("Lost is online")
    print("Login as %s"%(bot.user))
    print("Lost Version: %s"%(config.version))
    print("nextcord.py API Version: %s"%(nextcord.__version__))
    print('____________________________________________________________________________________________________________')

@bot.event
async def on_ready():
    starting()
    time.sleep(2)
    core.uptime.uptime.keep_alive()
    await bot.change_presence(
        activity=nextcord.Activity(type=nextcord.ActivityType.streaming, name =f"{bot.command_prefix}help｜Watch {len(bot.guilds)} server")
        )

def register_cogs():
    for filename in cogsList:
        bot.load_extension('cogs.%s'%(filename))

register_cogs()
bot.run(config.token)
