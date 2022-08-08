
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

from roblox import UserNotFound
import roblox.thumbnails
from roblox.thumbnails import AvatarThumbnailType
import os
from discord.utils import get

class Rank(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    
    @slash_command(guild_ids=[723941184476676107],description="Accepts user into group.")
    async def accept(self,ctx,username:Option(str,"Roblox Username")):
        roblox = Client('_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_48B91D6DEBA80E3C30E20F92D86B7C81ADFC8B0094B384D4AD56DD9F28C992E134C032E7605D37C462D5AD4D5A7236321F645FD6C10D891D3C4BCA91A5C0D335474995E42A1617C2EAE3605BF2CA5D60529179953DF7CD82803A52FEECBC106191733E1E48DEC55091B8018F6705A0E29D940C3328322DAA1541C4EFB0E0618D2007E9B86DFEC8F3C653A377538EFC1A30E17227F112CB784E0EEBCA5BE9262B11ACBF168B0C2BC5B7E33B9E3F4DC31A46B6543BC0FC2F13141BDFAF3CB4616C08A8A5DA0896A45F3358D6914D6178AC77ABD877BBA87A86598728D1C0488B346976FD2A9C50E1201E26D70F117F44A782826F2F1FF265875E4F55CDD57AAA26B3D845226DBD9D8138B53C724EB3F77C89C39AC83A6EE41C0208AAC4C00235A4EE126DC34EE9F99A4A53A00C631B8CE2654D1EC610B7F8468FE71FF98A842A9CC7F7D0F5D1646419B62DE89447B302DA4171CD1560ADC328191AF95B348AE6249D38B8F2A33ECC58F6D98B9C6E97DD815E6E4AE0E44D0CE30A4DC6B7E8F0683B5D94C05BCF7C77F563D3D3C301A6134ACCF2464D')
        group=await roblox.get_group(6764583)
        member=await group.get_member_by_username(username)
        logs=self.client.get_channel(988922177820704938)
        try:
            await group.accept_user(member)
            success=discord.Embed(description=f"{ctx.author.mention} accepted {username} in the group.", color=discord.Color.green(),timestamp=datetime.datetime.now())
            await ctx.respond(embed=success)
            await logs.send(embed=success)

        except BadRequest:
            pendingError=discord.Embed(description="Join request not found for {username}",color=discord.Color.red())
            await ctx.respond(embed=pendingError)     
    
    @slash_command(guild_ids=[723941184476676107],description="Ranks a user in the group.")
    async def setrank(
        self,
        ctx,
        username:Option(str,"Roblox Username"),
        rank:Option(str,"Select a rank in the group", choices=["Colonnello","Sotto-Colonnello","Maggiore","Capo-Battaglione","Capitano","Tenente","Sotto-Tenente","Ajutante-Sottufficiale","Ajutante","Sergente-Maggiore","Sergente","Caporale-Foriere","Caporale", "Soldata", "Conscritto"])
    ):
        await ctx.defer()

        rankId=-1
        guild = self.client.get_guild(723941184476676107)
 
      

        
        if rank=="Colonello":
            ajutante=guild.get_role(903380943212019754)
            ajutanteSecond=guild.get_role(903381070303600660)
            sottoTen=guild.get_role(903381275388297266)
            tentete=guild.get_role(903375478960816229)
            capitano=guild.get_role(852158143790186527)
            chief=guild.get_role(810029600704430151)
            major=guild.get_role(724074105803898981)
            ltcol=guild.get_role(953777277794144256)
            colonel=guild.get_role(723958358809378887)

            if ajutante not in ctx.author.roles and ajutanteSecond not in ctx.author.roles and sottoTen not in ctx.author.roles and tentete not in ctx.author.roles and capitano not in ctx.author.roles and chief not in ctx.author.roles and major not in ctx.author.roles and ltcol not in ctx.author.roles and colonel not in ctx.author.roles:
             rankId=245
        
        elif rank=="Sotto-Colonnello":
            ajutante=guild.get_role(903380943212019754)
            ajutanteSecond=guild.get_role(903381070303600660)
            sottoTen=guild.get_role(903381275388297266)
            tentete=guild.get_role(903375478960816229)
            capitano=guild.get_role(852158143790186527)
            chief=guild.get_role(810029600704430151)
            major=guild.get_role(724074105803898981)
            ltcol=guild.get_role(953777277794144256)
            if ajutante not in ctx.author.roles and ajutanteSecond not in ctx.author.roles and sottoTen not in ctx.author.roles and tentete not in ctx.author.roles and capitano not in ctx.author.roles and chief not in ctx.author.roles and major not in ctx.author.roles and ltcol not in ctx.author.roles:
             rankId=244       
        elif rank=="Maggiore":
            ajutante=guild.get_role(903380943212019754)
            ajutanteSecond=guild.get_role(903381070303600660)
            sottoTen=guild.get_role(903381275388297266)
            tentete=guild.get_role(903375478960816229)
            major=guild.get_role(724074105803898981)
            capitano=guild.get_role(852158143790186527)
            chief=guild.get_role(810029600704430151)
            if ajutante not in ctx.author.roles and ajutanteSecond not in ctx.author.roles and sottoTen not in ctx.author.roles and tentete not in ctx.author.roles and capitano not in ctx.author.roles and chief not in ctx.author.roles and major not in ctx.author.roles:
                rankId=243
        elif rank=="Capo-Battaglione":
            ajutante=guild.get_role(903380943212019754)
            ajutanteSecond=guild.get_role(903381070303600660)
            sottoTen=guild.get_role(903381275388297266)
            tentete=guild.get_role(903375478960816229)
            capitano=guild.get_role(852158143790186527)
            chief=guild.get_role(810029600704430151)
            if ajutante not in ctx.author.roles and ajutanteSecond not in ctx.author.roles and sottoTen not in ctx.author.roles and tentete not in ctx.author.roles and capitano not in ctx.author.roles and chief not in ctx.author.roles:
                rankId=241
        elif rank=="Capitano":
            ajutante=guild.get_role(903380943212019754)
            ajutanteSecond=guild.get_role(903381070303600660)
            sottoTen=guild.get_role(903381275388297266)
            tentete=guild.get_role(903375478960816229)
            capitano=guild.get_role(852158143790186527)
            if ajutante not in ctx.author.roles and ajutanteSecond not in ctx.author.roles and sottoTen not in ctx.author.roles and tentete not in ctx.author.roles and capitano not in ctx.author.roles:
                rankId=239
        elif rank=="Tenente":
            ajutante=guild.get_role(903380943212019754)
            ajutanteSecond=guild.get_role(903381070303600660)
            sottoTen=guild.get_role(903381275388297266)
            tentete=guild.get_role(903375478960816229)
            if ajutante not in ctx.author.roles and ajutanteSecond not in ctx.author.roles and sottoTen not in ctx.author.roles and tentete not in ctx.author.roles:
                rankId=237
        elif rank=="Sotto-Tenente":
            ajutante=guild.get_role(903380943212019754)
            ajutanteSecond=guild.get_role(903381070303600660)
            sottoTen=guild.get_role(903381275388297266)
            if ajutante not in ctx.author.roles and ajutanteSecond not in ctx.author.roles and sottoTen not in ctx.author.roles:
                rankId=235
        elif rank=="Ajutante-Sottufficiale":
            
            ajutanteSecond=guild.get_role(903381070303600660)
            if ajutante not in ctx.author.roles and ajutanteSecond not in ctx.author.roles:
                rankId=233
        elif rank=="Ajutante":
            ajutante=guild.get_role(903380943212019754)
            if ajutante not in ctx.author.roles:
                rankId=231
        elif rank=="Sergente-Maggiore":
            rankId=229
        elif rank=="Sergente":
            rankId=227
        elif rank=="Caporale-Foriere":
            rankId=225
        elif rank=="Caporale":
            rankId=223
        elif rank=="Soldata":
            rankId=221
        elif rank=="Coscritto":
            rankId=219
     
        
        permError=discord.Embed(description=f"{ctx.author.mention} tried ranking a user higher than or equal to his own rank.",color=discord.Color.red())
        logs=self.client.get_channel(988922177820704938)

        if rankId==-1:
            await ctx.respond(embed=permError)
            await logs.send(embed=permError)    

        roblox = Client('_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_168F3290FDB97AC996F6535D48847D8E674A58CC44569B0D48372C0F4854BE3255ED17AD82A03882259F885DF693BF2CD0ED4EADABC8CD7BE958CDEB31E6E77CC4BEEF2273581A905410CCCDE868968E62652C0EABE1601AD75EE767E6ED75ED5AE7CD528F67EDF940504CE25A7C3CF85D1CA91916E3F769BC1B8340DC9254FDE6B7A01FA1FF2A5F82BB810FC62763AF2197D09806A16B17278E6DA2A393E18F97283E07D9C0589D5296449F32ABF031F726E0BDE5820348CD9CADCAB0182CB509DAF9C1541940F653983D3131A30E51A2DB04949681DA776891998B58397FF0DCE7075559A8B3192264341079E3ABE2CC0C172BBB3B9894BA6BB874CC42E466A76354DCB0DDFD8500AF509CF34A92B74FEC3C219216A2C657C1E9E51295B9F94F2A9613E594CE10C8A8633DB76554394EDF154330BA1AE4EA934F4F0099A2E9081AF498BBAD14DE2ADA9A3E0219538075FBDB7BB939B769F7B3EE45311DDD39A2033D2C10D36D8573EE00F9A19E13D1DF53517E0C0653F195BBBDCDAD7ED5991D9F498CE45068C68DDB3128F5C871E48A0E0F5D')
        group=await roblox.get_group(6764583)
        member=await group.get_member_by_username(username)
        prevRank=(next(filter(lambda role: role.group.id == int(6764583), await member.get_group_roles())).name)
        try:
            await member.set_rank(rankId)
        except UserNotFound:
            await ctx.respond("User not found.")
        log=discord.Embed(description=f"{ctx.author.mention} ranked {username} to {rank} from {prevRank} in the group.",color=discord.Color.blurple(),timestamp=datetime.datetime.now())
        await logs.send(embed=log)
        await ctx.respond(embed=log)

def setup(client):
    client.add_cog(Rank(client))        

