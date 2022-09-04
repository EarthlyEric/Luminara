# -*- coding: UTF-8 -*-
import imp
import nextcord
import os
import time
import platform
from nextcord.ext import commands
from datetime import datetime
from core.config import *
from core.utils import utils

intents=nextcord.Intents.all()

bot=commands.Bot(command_prefix='$',intents=intents)
bot.remove_command("help")
bot.launch_time=datetime.utcnow()

extension=['tasks','events','errors','general','music','debug']

def starting():
    os.system('cls' if os.name=='nt' else 'clear')
    logopath='./res/logo/logo.txt'
    f=open(logopath, 'r')
    print('____________________________________________________________________________________________________________')
    print(f.read())
    time.sleep(0.5)
    print('____________________________________________________________________________________________________________')
    print()
    utils.showinfo("作業系統",platform.platform())
    utils.showinfo('系統版本',platform.version())
    utils.showinfo('作業系統名稱', platform.system())
    utils.showinfo('系統位數', platform.architecture()[0])
    utils.showinfo('CPU 架構', platform.machine())
    utils.showinfo('系統名稱', platform.node())
    utils.showinfo('處理器', platform.processor())
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
    await bot.change_presence(
        activity=nextcord.Activity(type=nextcord.ActivityType.streaming, name='%shelp｜在 %s 個伺服器中'%(bot.command_prefix,str(len(bot.guilds))))
        )

def register_cogs():
    for filename in extension:
        bot.load_extension('cogs.%s'%(filename))
register_cogs()
bot.run(config.token)
