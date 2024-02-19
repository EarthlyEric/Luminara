import nextcord
from nextcord.ext import commands
from datetime import datetime
from core.config import *
from core.classes import Slash_Cogs
from core.utils import colors,icon,emojis

class Slash_Debugs(Slash_Cogs):
    extension_location_list={
        'general':'commands',
        'music':'commands',
        'management':'commands',
        'errors':'events',
        'events':'events',
        'tasks':'events'}
    @nextcord.slash_command(name='reload',description='重新載入指定的Extension')
    @commands.is_owner()
    async def reload(self,
        interaction: nextcord.Interaction,
        extension: str = nextcord.SlashOption(
        name='extension',
        choices={
            'general': 'general',
            'management':'management', 
            'music': 'music', 
            'errors': 'errors',
            'events':'events',
            'tasks':'tasks'
            })):
            extension=extension.replace("'","")
            extension_location=self.extension_location_list[f'{extension}']
            try:
                self.bot.reload_extension('cogs.%s.%s'%(extension_location,extension))
                print(f'[Debug][INFO] Reloaded {extension_location}.{extension}')
                embed = nextcord.Embed(title='重新載入中...', description='`%s` 載入成功'%(extension), color=colors.green,timestamp=datetime.now())
                embed.set_footer(text='Luminara•Debug System', icon_url=icon.icon_url)
                return await interaction.response.send_message(embed=embed)
            except Exception as e:
                print('[Debug][ERROR] %s')%(e)
                embed = nextcord.Embed(title='重新載入中...', description='載入失敗', color=colors.red,timestamp=datetime.now())
                embed.add_field(name='原因',value='`%s`'%(e))
                embed.set_footer(text='Luminara', icon_url=icon.icon_url)
                embed.set_footer(text='Luminara•Debug System', icon_url=icon.icon_url)
                return await interaction.response.send_message(embed=embed)
        
        
        

def setup(bot):
    bot.add_cog(Slash_Debugs(bot))