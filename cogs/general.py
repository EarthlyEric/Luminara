# -*- coding: UTF-8 -*-
from unicodedata import name
import nextcord
import cogs.UI.dropmenu
import psutil
from datetime import datetime
from core.utils import colors,icon,utils
from nextcord.ext import commands
from core.classes import Cogs
from core.config import config
from typing import Optional

class General(Cogs):
    @commands.command(name='help')
    async def help(self, ctx:commands.Context):
        view=cogs.UI.dropmenu.HelpView()

        embed=nextcord.Embed(color=colors.purple,timestamp=datetime.now())
        embed.set_author(name='Lost使用指南',icon_url=icon.guide_icon_url,url='https://blog.earthlyeric6.ml/')
        embed.add_field(name='Hello，我是Lost，很高興見到你!',value='你可以從下面選擇想看的指令使令用法類別。')
        embed.set_footer(text="Lost", icon_url=icon.icon_url)

        await ctx.reply(embed=embed,view=view)
 
    @commands.command(name='ping')
    async def ping(self, ctx:commands.Context):
        bot_uptime = datetime.utcnow() - self.bot.launch_time
        hours, remainder = divmod(int(bot_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)

        embed=nextcord.Embed(color=colors.purple,timestamp=datetime.now())
        embed.insert_field_at
        embed.set_author(name='Lost狀態',icon_url=icon.icon_url,url='https://blog.earthlyeric6.ml/')
        # CPU Usage
        cpu_usage=psutil.cpu_percent(interval=0.3)
        usage_bar=utils.processesBar(level=int(round(cpu_usage,0)))
        embed.add_field(name='<:CPU:1008034878882852954>|CPU',value=f'`{cpu_usage}%{usage_bar}`',inline=True)
        # RAM Usage
        ram=psutil.virtual_memory()
        ram_usage=ram.percent
        usage_bar=utils.processesBar(level=int(round(ram_usage,0)))
        embed.add_field(name='<:RAM:1008035593894236241>|RAM',value=f'`{ram_usage}%{usage_bar}`',inline=True)
        # Bot Info
        embed.add_field(name='<:server:1008236554042490950>|伺服器數量',value='`%s個`'%((str(len(self.bot.guilds)))),inline=False)
        embed.add_field(name='<:discord_api:1013700080118804580>|Discord API狀態', value='`%s ms`'%(str(round(self.bot.latency*1000))), inline=False)
        embed.add_field(name='<:clock_lost:1013705761064493096> Lost上線時間(本次進程)', value='`%s d, %s h, %s m, %s s`'%(days,hours,minutes,seconds), inline=False)
        embed.add_field(name='<:Lost:1008221589231386645>|Bot Version',value=' `%s`<:beta:1013696625031520276>'%(config.version),inline=False)
        # Footer
        embed.set_footer(text='Lost', icon_url=icon.icon_url)

        return await ctx.reply(embed=embed)

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


        embed=nextcord.Embed(
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
        embed.set_footer(text='Lost', icon_url=icon.icon_url)

        return await ctx.reply(embed=embed)
    
    @info.command(name='user')
    async def user(self,ctx:commands.Context,user:nextcord.Member=None):
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

        embed=nextcord.Embed(
        title='<:discord_api:1013700080118804580> |使用者詳情',
        description='***%s***'%(name),
        color=colors.purple,
        timestamp=datetime.now())
        embed.set_thumbnail(url=avatar_url)
        embed.add_field(name='`使用者ID`',value='%s'%(id),inline=False)
        embed.add_field(name='創建時間',value='`%s`'%(created_date),inline=False)
        embed.set_footer(text='Lost', icon_url=icon.icon_url)

        await ctx.reply(embed=embed)
        
    
     
def setup(bot):
    bot.add_cog(General(bot))