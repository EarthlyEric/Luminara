# -*- coding: UTF-8 -*-
from discord import Emoji
import discord

class Help(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="一般",value="general",description="基礎指令",emoji="<:general:1002820067324600380>"),
            discord.SelectOption(label="音樂",value="music",description="Let's start the music !",emoji="<:music:1002824345095241878>")
        ]
        super().__init__(
            placeholder="指令指南",
            min_values=1,
            max_values=1,
            options=options,
            )
        async def callback(self,interaction:discord.Interaction):
            value=self.values[0]
            if value=="general":
                return await interaction.response.send_message("尚未完成")
            elif value=="music":
                return await interaction.response.send_message("尚未完成")

class HelpView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Help())

class PlayButton(discord.ui.Button):
    def __init__(self):
        super().__init__(label="播放",style=discord.ButtonStyle.green)
        
    async def callback(self,interaction:discord.Interaction):
        await interaction.response.send_message("尚未完成")

class MusicControllerView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(PlayButton())
            