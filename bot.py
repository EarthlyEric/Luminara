# -*- coding: UTF-8 -*-
import discord
import datetime
import time
import platform
import asyncio
from discord.ext import commands
from datetime import datetime, timezone
from core.config import *
from core.utils import utils

intents=discord.Intents.all()

bot=commands.Bot(command_prefix='b$',intents=intents)
bot.remove_command("help")
bot.launch_time=datetime.now(timezone.utc)

def start_up():
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
    print("Luminara is online")
    print("Login as %s"%(bot.user))
    print("Luminara Version: %s"%(config.version))
    print("Discord API Version: %s"%(discord.__version__))
    print('____________________________________________________________________________________________________________')
    
@bot.event
async def on_ready():
    start_up()
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.streaming, name='%shelp｜在 %s 個伺服器中'%(bot.command_prefix,str(len(bot.guilds))))
        )

async def main():
    async with bot:
        # Debug Commands
        await bot.load_extension('cogs.debugs')
        #bot.load_extension('cogs.slash_debugs')
        # Events Cogs
        #bot.load_extension('cogs.events.events')
        #bot.load_extension('cogs.events.errors')
        #bot.load_extension('cogs.events.tasks')
        # Traditional Commands
        await bot.load_extension('cogs.commands.general')
        await bot.load_extension('cogs.commands.management')
        #bot.load_extension('cogs.commands.music')
        await bot.start(config.token)

asyncio.run(main())