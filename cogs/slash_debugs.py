# -*- coding: UTF-8 -*-
import discord
from discord.ext import commands
from datetime import datetime

from classes import Slash_Cogs
from core.utils import colors, icon, emojis

class Slash_Debugs(Slash_Cogs):
    extension_location_list = {
        "general": "commands",
        "music": "commands",
        "management": "commands",
        "errors": "events",
        "events": "events",
        "tasks": "events"
    }

    @discord.app_commands.command(name="reload", description="重新載入指定的Extension")
    @discord.app_commands.choices(extensions=[
        discord.app_commands.Choice(name="general", value="general"),
        discord.app_commands.Choice(name="management", value="management"),
        discord.app_commands.Choice(name="music", value="music"),
        discord.app_commands.Choice(name="errors", value="errors"),
        discord.app_commands.Choice(name="events", value="events"),
        discord.app_commands.Choice(name="tasks", value="tasks")
    ])
    @commands.is_owner()
    async def reload(self, interaction: discord.Interaction, extensions: discord.app_commands.Choice[str]):
        extension = extensions.value.replace('"', '')
        extension_location = self.extension_location_list[f"{extension}"]
        try:
            self.bot.reload_extension(f"cogs.{extension_location}.{extension}")
            print(f"[Debug][INFO] Reloaded {extension_location}.{extension}")
            embed = discord.Embed(title="重新載入中...", description=f"`{extension}` 載入成功", color=colors.green, timestamp=datetime.now())
            embed.set_footer(text="Luminara•Debug System", icon_url=icon.icon_url)
            return await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(f"[Debug][ERROR] {e}")
            embed = discord.Embed(title="重新載入中...", description="載入失敗", color=colors.red, timestamp=datetime.now())
            embed.add_field(name="原因", value=f"`{e}`")
            embed.set_footer(text="Luminara", icon_url=icon.icon_url)
            embed.set_footer(text="Luminara•Debug System", icon_url=icon.icon_url)
            return await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Slash_Debugs(bot))