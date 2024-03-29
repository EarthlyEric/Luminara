# -*- coding: UTF-8 -*-
import discord
import datetime
import time
import platform
import asyncio
from discord.ext import commands
from datetime import datetime, timezone

import classes
from core.config import *
from core.utils import utils
from ui.musiccontroller import MusicControllerView

bot=classes.theBot()
bot.remove_command("help")
bot.launch_time=datetime.now(timezone.utc)


def start_up():
    print("____________________________________________________________________________________________________________")
    print(open("./res/logo/logo.txt", "r").read())
    time.sleep(0.3)
    print("____________________________________________________________________________________________________________")
    print()
    utils.showinfo("OS Platform",platform.platform())
    utils.showinfo("系統位數", platform.architecture()[0])
    utils.showinfo("CPU 架構", platform.machine())
    utils.showinfo("System Name", platform.node())
    print("Time:%s"%(datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")))
    print("____________________________________________________________________________________________________________")
    print("                                                                                                            ")
    print("Luminara is online")
    print("Login as %s"%(bot.user))
    print("Luminara Version: %s"%(config.version))
    print("Discord API Version: %s"%(discord.__version__))
    print("____________________________________________________________________________________________________________")
    
@bot.event
async def on_ready():
    start_up()
    slash = await bot.tree.sync()
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.streaming, name="%shelp|在 %s 個伺服器中"%(bot.command_prefix,str(len(bot.guilds))))
        )

@bot.command(name="test")
async def test(ctx):
    await ctx.send("",view=MusicControllerView(ctx=ctx,bot=bot))

async def main():
    async with bot:
        # Debug Commands
        await bot.load_extension("cogs.debugs")
        await bot.load_extension("cogs.slash_debugs")
        # Events Cogs
        await bot.load_extension("cogs.events.events")
        await bot.load_extension("cogs.events.errors")
        await bot.load_extension("cogs.events.tasks")
        # Traditional Commands
        await bot.load_extension("cogs.commands.general")
        await bot.load_extension("cogs.commands.management")
        await bot.load_extension("cogs.commands.music")
                
        await bot.start(config.token)

asyncio.run(main())