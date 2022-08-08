from http import client
from random import randint
from time import time
import discord
import roblox
import datetime
from roblox import Client
import discord.ext
from discord.ext import commands
from discord.commands import Option,slash_command
from discord.ext.commands import MissingPermissions
from discord.utils import get
import roblox.utilities.exceptions
from roblox.utilities.exceptions import BadRequest

from roblox import InternalServerError
import roblox.thumbnails
from roblox.thumbnails import AvatarThumbnailType
import os
from discord.utils import get

class Rank(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    
    @slash_command(guild_ids=[935566950568951838],description="Accepts user into group.")
    async def accept(self,ctx,username:Option(str,"Roblox Username")):
        roblox = Client('_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_48B91D6DEBA80E3C30E20F92D86B7C81ADFC8B0094B384D4AD56DD9F28C992E134C032E7605D37C462D5AD4D5A7236321F645FD6C10D891D3C4BCA91A5C0D335474995E42A1617C2EAE3605BF2CA5D60529179953DF7CD82803A52FEECBC106191733E1E48DEC55091B8018F6705A0E29D940C3328322DAA1541C4EFB0E0618D2007E9B86DFEC8F3C653A377538EFC1A30E17227F112CB784E0EEBCA5BE9262B11ACBF168B0C2BC5B7E33B9E3F4DC31A46B6543BC0FC2F13141BDFAF3CB4616C08A8A5DA0896A45F3358D6914D6178AC77ABD877BBA87A86598728D1C0488B346976FD2A9C50E1201E26D70F117F44A782826F2F1FF265875E4F55CDD57AAA26B3D845226DBD9D8138B53C724EB3F77C89C39AC83A6EE41C0208AAC4C00235A4EE126DC34EE9F99A4A53A00C631B8CE2654D1EC610B7F8468FE71FF98A842A9CC7F7D0F5D1646419B62DE89447B302DA4171CD1560ADC328191AF95B348AE6249D38B8F2A33ECC58F6D98B9C6E97DD815E6E4AE0E44D0CE30A4DC6B7E8F0683B5D94C05BCF7C77F563D3D3C301A6134ACCF2464D')
        group=await roblox.get_group(7528791)
        member=await group.get_member_by_username(self.username)
        logs=self.client.get_channel(988555777994281070)
        try:
            await group.accept_user(member)
            success=discord.Embed(description=f"{ctx.author.mention} accepted {self.username} in the group.", color=discord.Color.green(),timestamp=datetime.datetime.now())
            await ctx.respond(embed=success,ephemeral=True)
            await logs.send(embed=success)

        except BadRequest:
            pendingError=discord.Embed(description="Join request not found for {username}",color=discord.Color.red())
            await ctx.respond(embed=pendingError)     
    
    @slash_command(guild_ids=[935566950568951838],description="Ranks a user in the group.")
    async def setrank(
        self,
        ctx,
        username:Option(str,"Roblox Username"),
        rank:Option(str,"Select a rank in the group", choices=["Tenente", "Sotto-Tenente", "Ajutante-Sottufficiale", "Ajutante", "Sergente Maggiore", "Sergente", "Caporale Foriere", "Caporale", "Soldato", "Coscritto", "Cittadino"])
    ):
        await ctx.defer()

        rankId=-1
        guild = self.client.get_guild(935566950568951838)
 
        tent=guild.get_role(935819514917031990)
        sottotent=guild.get_role(935819632533721098)
        ajutant=guild.get_role(968138702628982844)

        
        if rank=="Tenente":
            if tent not in ctx.author.roles and sottotent not in ctx.author.roles and ajutant  not in ctx.author.roles:
             rankId=110
        
        elif rank=="Sotto-Tenente":
            if sottotent not in ctx.author.roles and ajutant  not in ctx.author.roles:
             rankId=100
        elif rank=="Ajutante-Sottufficiale":
             if sottotent not in ctx.author.roles and ajutant  not in ctx.author.roles:
                rankId=90           
        elif rank=="Ajutante":
            rankId=80
        elif rank=="Sergente Maggiore":
            rankId=70
        elif rank=="Sergente":
            rankId=60
        elif rank=="Caporale Foriere":
            rankId=50
        elif rank=="Caporale":
            rankId=40
        elif rank=="Soldato":
            rankId=30
        elif rank=="Coscritto":
            rankId=20
        elif rank=="Cittadino":
            rankId=10
        
        permError=discord.Embed(description=f"{ctx.author.mention} tried ranking a user higher than or equal to his own rank.",color=discord.Color.red())
        logs=self.client.get_channel(988555777994281070)

        if rankId==-1:
            await ctx.respond(embed=permError)
            await logs.send(embed=permError)    

        roblox = Client('_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_48B91D6DEBA80E3C30E20F92D86B7C81ADFC8B0094B384D4AD56DD9F28C992E134C032E7605D37C462D5AD4D5A7236321F645FD6C10D891D3C4BCA91A5C0D335474995E42A1617C2EAE3605BF2CA5D60529179953DF7CD82803A52FEECBC106191733E1E48DEC55091B8018F6705A0E29D940C3328322DAA1541C4EFB0E0618D2007E9B86DFEC8F3C653A377538EFC1A30E17227F112CB784E0EEBCA5BE9262B11ACBF168B0C2BC5B7E33B9E3F4DC31A46B6543BC0FC2F13141BDFAF3CB4616C08A8A5DA0896A45F3358D6914D6178AC77ABD877BBA87A86598728D1C0488B346976FD2A9C50E1201E26D70F117F44A782826F2F1FF265875E4F55CDD57AAA26B3D845226DBD9D8138B53C724EB3F77C89C39AC83A6EE41C0208AAC4C00235A4EE126DC34EE9F99A4A53A00C631B8CE2654D1EC610B7F8468FE71FF98A842A9CC7F7D0F5D1646419B62DE89447B302DA4171CD1560ADC328191AF95B348AE6249D38B8F2A33ECC58F6D98B9C6E97DD815E6E4AE0E44D0CE30A4DC6B7E8F0683B5D94C05BCF7C77F563D3D3C301A6134ACCF2464D')
        group=await roblox.get_group(7528791)
        member=await group.get_member_by_username(username)
        prevRank=(next(filter(lambda role: role.group.id == int(7528791), await member.get_group_roles())).name)
        await member.set_rank(rankId)
        log=discord.Embed(description=f"{ctx.author.mention} ranked {username} to {rank} from {prevRank} in the group.",color=discord.Color.blurple(),timestamp=datetime.datetime.now())
        await logs.send(embed=log)
        await ctx.respond(embed=log)

def setup(client):
    client.add_cog(Rank(client))        

