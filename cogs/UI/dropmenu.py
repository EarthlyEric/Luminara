from nextcord import Emoji
import nextcord

class Help(nextcord.ui.Select):
    def __init__(self):
        options=[
            nextcord.SelectOption(label='一般',description='基礎指令',emoji='<:general:1002820067324600380>'),
            nextcord.SelectOption(label='音樂',description="Let's start the music !",emoji='<:music:1002824345095241878>')
        ]
        super().__init__(
            placeholder='指令指南',
            min_values=1,
            max_values=1,
            options=options,
            )
class HelpView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Help())

