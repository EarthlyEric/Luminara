# -*- coding: UTF-8 -*-
import discord
import wavelink
from discord.ext import commands

class theBot(commands.Bot):
    def __init__(self) -> None:
        intents: discord.Intents = discord.Intents.all()
        intents.message_content = True
        super().__init__(command_prefix="b$", intents=intents)

    async def setup_hook(self) -> None:
        nodes = [wavelink.Node(uri="https://lavalink4.alfari.id", password="catfein")]
        await wavelink.Pool.connect(nodes=nodes, client=self, cache_capacity=100)
    
    async def on_wavelink_node_ready(self, payload: wavelink.NodeReadyEventPayload) -> None:
        print(f"Wavelink Node connected: {payload.node!r} | Resumed: {payload.resumed}")

class Cogs(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

class Slash_Cogs(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        self.count = 0
        





