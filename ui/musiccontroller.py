import discord
import datetime
import wavelink

from core.utils import utils,emojis

class MusicController(discord.Embed):
    def __init__(
            self,
            timestamp:datetime.datetime,
            track: wavelink.Playable
            ):
        super().__init__()
        self.title=f"{emojis.notes} | **{track.title}** - `{track.author}`"
        self.description=f"`[{utils.convertMiliseconds(track.length)}/]`"
        self.url=track.uri
        if track.artwork:
            self.set_thumbnail(url=track.artwork) 
        self.timestamp=timestamp
        self.color=discord.Color.blurple()
        self.set_footer(text="Luminara")

        super.__init__(self)
        