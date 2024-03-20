import discord
import datetime

import wavelink

class MusicController(discord.Embed):
    def __init__(
            self,
            timestamp:datetime.datetime,
            track: wavelink.Playable
            ):
        super().__init__()
        self.title=f" **{track.title}**"
        self.timestamp=timestamp
        self.color=discord.Color.blurple()
        self.set_author(name="音樂播放控制器",icon_url="https://cdn.discordapp.com/emojis/1002824345095241878.png")
        self.set_footer(text="Luminara")
        