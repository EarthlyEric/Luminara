# -*- coding: UTF-8 -*-
import discord
import wavelink
import logging
from discord import app_commands
from discord.ext import commands 

from core.config import config

class Bot(commands.Bot):
    def __init__(self) -> None:
        intents: discord.Intents = discord.Intents.all()
        intents.message_content = True

        super().__init__(command_prefix=config.commandPrefix, intents=intents)

    async def setup_hook(self) -> None:
        nodes = [wavelink.Node(
            identifier="Self-Hosted Node US 01",
            uri=config.lavalinkHost, 
            password=config.lavalinkPasswd,
            inactive_player_timeout=120)]
        await wavelink.Pool.connect(nodes=nodes, client=self, cache_capacity=100)

    async def on_wavelink_node_ready(self, payload: wavelink.NodeReadyEventPayload) -> None:
        print(f"Wavelink Node connected: {payload.node!r} | Resumed: {payload.resumed}")

class Cogs(commands.Cog):
    def __init__(self, bot):
        self.bot:Bot=bot

        





