# -*- coding: UTF-8 -*-
import discord
import wavelink

import classes
from core.utils import emojis

class MusicControllerView(discord.ui.View):
    def __init__(self, player:wavelink.Player, bot: classes.theBot,timeout=180):
        super().__init__(timeout=timeout)
        self.bot = bot
        self.player = player

    @discord.ui.button(label="Skip", style=discord.ButtonStyle.blurple)
    async def skip(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.player.queue.is_empty:
            return await interaction.response.send_message(f"{emojis.errors} | 播放序列已經空了，無法進行操作!")
        elif self.player.paused:
            return await interaction.response.send_message(f"{emojis.errors} | 播放暫停中，無法進行操作!")   
        elif self.player.playing:
            await interaction.response.send_message(":track_next: | 已跳過當前曲目 !即將播放下一首曲目。")
            return await self.player.play(self.player.queue.get())
        
        