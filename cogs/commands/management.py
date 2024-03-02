import discord
import psutil
from datetime import datetime, timezone
from core.utils import colors,icon,utils,emojis
from discord.ext import commands
from core.classes import Cogs
from core.config import config
from ui.view import *

class Management(Cogs):
    # command ifno group
    @commands.group(name='info')
    async def info(self,ctx:commands.Context):
        pass

    @info.command(name='guild')
    async def guild(self,ctx:commands.Context):
        name=ctx.guild.name
        icon_url=ctx.guild.icon.url
        id=ctx.guild.id
        members_count=ctx.guild.member_count
        bot_count=len(ctx.guild.bots)
        real_users_count=members_count-bot_count
        owner_mention=ctx.guild.owner.mention
        created_date=ctx.guild.created_at.strftime('%Y年%m月%d日 %H時%M分%S秒')
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

        embed=discord.Embed(
        title='<:discord_api:1013700080118804580> |伺服器詳情',
        description='***%s***'%(name),
        color=colors.purple,
        timestamp=datetime.now())
        embed.set_thumbnail(url=icon_url)
        embed.add_field(name='伺服器ID',value='`%s`'%(id),inline=False)
        embed.add_field(name='創建時間',value='`%s`'%(created_date),inline=False)
        embed.add_field(name='總人數',value='`%s(使用者:%s，機器人:%s)`'%(
            members_count,
            real_users_count,
            bot_count
            ),inline=False)
        embed.add_field(name='加成狀態',value='`%d個`/`%d級`'%(booster,booster_level),inline=False)
        embed.add_field(name='總頻道數',value='`%s個`\n`(文字頻道:%s個，語音頻道:%s個)`\n(機器人僅顯示有權訪問)\n'%(channels_count,text_channels_count,voice_channels_count))
        embed.add_field(name='擁有者',value='%s'%(owner_mention),inline=False)
        embed.set_footer(text='Luminara', icon_url=icon.icon_url)

        return await ctx.reply(embed=embed)
    
    @info.command(name='user')
    async def user(self,ctx:commands.Context,user:discord.Member=None):
        if user==None:
            name=ctx.author.name
            avatar_url=ctx.author.avatar.url
            id=ctx.author.id
            created_date=ctx.author.created_at.strftime('%Y年%m月%d日 %H時%M分%S秒')
        else:
            name=user.name
            id=user.id
            avatar_url=user.avatar.url
            created_date=user.created_at.strftime('%Y年%m月%d日 %H時%M分%S秒')

        embed=discord.Embed(
        title='%s |使用者詳情'%(emojis.discord_api),
        description='***%s***'%(name),
        color=colors.purple,
        timestamp=datetime.now())
        embed.set_thumbnail(url=avatar_url)
        embed.add_field(name='`使用者ID`',value='%s'%(id),inline=False)
        embed.add_field(name='創建時間',value='`%s`'%(created_date),inline=False)
        embed.set_footer(text='Luminara', icon_url=icon.icon_url)

        return await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(Management(bot))
    