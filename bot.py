# -*- coding: UTF-8 -*-
import discord,os,core.start_menu
from discord.ext import commands
from datetime import datetime
from core.config import *
from core.lib import showinfo

#core.uptime.uptime.keep_alive()

intents=discord.Intents.all()

bot = commands.Bot(command_prefix='a!',intents=intents)
bot.remove_command("help")
bot.launch_time = datetime.utcnow()


@bot.event
async def on_ready():
    core.start_menu.start_menu()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name =f"{bot.command_prefix}help｜{len(bot.guilds)}"))

for coglist in os.listdir('./cogs'):
	if coglist.endswith('.py'):
		bot.load_extension(f'cogs.{coglist[:-3]}')

bot.run(token)
