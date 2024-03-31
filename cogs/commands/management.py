# -*- coding: UTF-8 -*-
from typing import Optional
import discord
from datetime import datetime
from discord.ext import commands

from core.libs.class_define import Cogs
from ui.view import *
from core.utils import colors,icon,emojis

class Management(Cogs):

    @commands.hybrid_command(name="guild-info",description="顯示伺服器詳情",with_app_command=True)
    async def guild_info(self,ctx: commands.Context):
        name=ctx.guild.name
        icon_url=ctx.guild.icon.url
        id=ctx.guild.id
        members_count=ctx.guild.member_count
        bot_count=len([member for member in ctx.guild.members if member.bot])
        real_users_count=members_count-bot_count
        owner_mention=ctx.guild.owner.mention
        created_date=ctx.guild.created_at.strftime("%Y年%m月%d日 %H時%M分%S秒")
        booster=ctx.guild.premium_subscription_count
        channels_count=len(ctx.guild.channels)
        text_channels_count=len(ctx.guild.text_channels)
        voice_channels_count=len(ctx.guild.voice_channels)

        if booster<2:
            booster_level=0
        elif booster>=2:
            booster_level=1
        elif booster>=7:
            booster_level=2
        elif booster>=14:
            booster_level=3

        embed=discord.Embed(color=colors.purple, timestamp=datetime.now())
        embed.title="%s | 伺服器詳情"%(emojis.server)
        embed.description="***%s***"%(name)
        embed.set_thumbnail(url=icon_url)
        embed.add_field(name="伺服器ID",value="`%s`"%(id),inline=False)
        embed.add_field(name="創建時間",value="`%s`"%(created_date),inline=False)
        embed.add_field(name="總人數",value="`%s(使用者:%s，機器人:%s)`"%(
            members_count,
            real_users_count,
            bot_count
            ),inline=False)
        embed.add_field(name="加成狀態",value="`%d個`/`%d級`"%(booster,booster_level),inline=False)
        embed.add_field(name="總頻道數",value="`%s個`\n`(文字頻道:%s個，語音頻道:%s個)`\n(機器人僅顯示有權訪問)\n"%(channels_count,text_channels_count,voice_channels_count))
        embed.add_field(name="擁有者",value="%s"%(owner_mention),inline=False)
        embed.set_footer(text="Luminara")

        return await ctx.reply(embed=embed)
    
    @commands.hybrid_command(name="user-info",description="顯示使用者詳情",with_app_command=True)
    async def user_info(self,ctx: commands.Context,user:Optional[discord.User]):
        if not user:
            name=ctx.author.name
            avatar_url=ctx.author.avatar.url
            id=ctx.author.id
            created_date=ctx.author.created_at.strftime("%Y年%m月%d日 %H時%M分%S秒")
        else:
            name=user.name
            id=user.id
            avatar_url=user.avatar.url
            created_date=user.created_at.strftime("%Y年%m月%d日 %H時%M分%S秒")

        embed=discord.Embed(color=colors.purple, timestamp=datetime.now())
        embed.title="%s | 使用者詳情"%(emojis.user)
        embed.description="***%s***"%(name)
        embed.set_thumbnail(url=avatar_url)
        embed.add_field(name="`使用者ID`",value="%s"%(id),inline=False)
        embed.add_field(name="帳號創建時間",value="`%s`"%(created_date),inline=False)
        embed.set_footer(text="Luminara")

        return await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(Management(bot))
    