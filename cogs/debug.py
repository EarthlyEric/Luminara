from discord import slash_command
import nextcord
from nextcord.ext import commands
from core.config import *
from core.classes import Cogs
from core.utils import colors

class Debug(Cogs):
    @commands.command()
    @commands.is_owner()
    async def reload(self,ctx, extension):
        try:
            self.bot.reload_extension(f"cogs.{extension}")
            print(f'Reloaded {extension}')
            embed = nextcord.Embed(title='Reload', description=f'{extension} successfully reloaded', color=colors.green)
            return await ctx.send(embed=embed)
        except Exception as e:
            embed = nextcord.Embed(title='Error', description=f'{e}', color=colors.red)
            return await ctx.send(embed=embed)
        

def setup(bot):
    bot.add_cog(Debug(bot))