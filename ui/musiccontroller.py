import discord
import datetime
import wavelink

from core.utils import utils

class MusicController(discord.Embed):
    def __init__(
            self,
            timestamp:datetime.datetime,
            track: wavelink.Playable
            ):
        super().__init__()
        self.title=f" **{track.title}** - `{track.author}`"
        self.description=f"```[{utils.convertMiliseconds(track.length)}]```"
        self.url=track.uri
        self.timestamp=timestamp
        self.color=discord.Color.blurple()
        self.set_footer(text="Luminara")
        