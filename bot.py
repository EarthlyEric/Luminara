# -*- coding: UTF-8 -*-
import nextcord
import os
import time
import platform
from nextcord.ext import commands
from datetime import datetime
from core.lavalink.lavalink import init_lavalink
from core.config import *
from core.utils import utils

intents=nextcord.Intents.all()

bot=commands.Bot(command_prefix='$',intents=intents)
bot.remove_command("help")
bot.launch_time=datetime.utcnow()



def starting():
    os.system('cls' if os.name=='nt' else 'clear')
    print('____________________________________________________________________________________________________________')
    print(open('./res/logo/logo.txt', 'r').read())
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
    print("Nextcord API Version: %s"%(nextcord.__version__))
    print('____________________________________________________________________________________________________________')

def register_cogs():
    # Debug Commands
    bot.load_extension('cogs.debugs')
    bot.load_extension('cogs.slash_debugs')
    # Events Cogs
    bot.load_extension('cogs.events.events')
    bot.load_extension('cogs.events.errors')
    bot.load_extension('cogs.events.tasks')
    # Traditional Commands
    bot.load_extension('cogs.commands.general')
    bot.load_extension('cogs.commands.management')
    bot.load_extension('cogs.commands.music')

@bot.event
async def on_ready():
    starting()
    await bot.change_presence(
        activity=nextcord.Activity(type=nextcord.ActivityType.streaming, name='%shelp｜在 %s 個伺服器中'%(bot.command_prefix,str(len(bot.guilds))))
        )

register_cogs()
init_lavalink()
time.sleep(5)
bot.run(config.token)