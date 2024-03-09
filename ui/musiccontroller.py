import discord
import datetime

class MusicController(discord.Embed):
    def __init__(
            self,
            title:str,
            timestamp:datetime.datetime,
            
            ):
        super().__init__()
        self.title=title
        self.timestamp=timestamp
        self.color=discord.Color.blurple()
        self.set_author(name='音樂播放控制器',icon_url='https://cdn.discordapp.com/emojis/1002824345095241878.png')
        self.set_footer(text='Luminara')
        