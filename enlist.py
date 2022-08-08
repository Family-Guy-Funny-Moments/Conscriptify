
import discord

import roblox
import datetime
from roblox import Client
import discord.ext
from discord.ext import commands
from discord.commands import Option,slash_command

from discord.utils import get

from roblox.utilities.exceptions import BadRequest
from roblox.utilities.exceptions import UserNotFound

from roblox.thumbnails import AvatarThumbnailType



oneO_dict={}
threeO_dict={}
rrd_dict={}
istra_dict={}

class Conscript(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.regiment="None"
        self.enlistment=discord.Embed(description="none")
        self.recruiter="None"
        self.timezone="None"
        
        

        
    
    @commands.Cog.listener("on ready")
    async def on_ready(self):
        print(f"{self.bot.user} has logged in!")

    
    @slash_command(guild_ids=[935566950568951838],description="Send a request to enlist in a regiment")
    async def enlist(
        self,
        ctx,
        regiment:Option(str, "Choose a regiment", choices=["7° Reggimento Fanteria di Linea","3° Reggimento Fanteria di Leggera","Battaglione Reale d'Istria"]),
        pending:Option(str,"A group join request is MANDATORY (You will be denied if you are not pending)", choices=["Yes","Already in Group","No"]),
        timezone:Option(str,"Recruit's timezone"),
        recruiter_ping:Option(str,"@Ping your recruiter, if none just type \"None\"")
    ):  
        await ctx.defer()
        succ=True
        self.recruiter=recruiter_ping
        self.timezone=timezone
        guild = self.client.get_guild(935566950568951838)
        verified=guild.get_role(968149010504368139)
        pendingRole=guild.get_role(988581530639167518)

        
        roblox = Client('_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_48B91D6DEBA80E3C30E20F92D86B7C81ADFC8B0094B384D4AD56DD9F28C992E134C032E7605D37C462D5AD4D5A7236321F645FD6C10D891D3C4BCA91A5C0D335474995E42A1617C2EAE3605BF2CA5D60529179953DF7CD82803A52FEECBC106191733E1E48DEC55091B8018F6705A0E29D940C3328322DAA1541C4EFB0E0618D2007E9B86DFEC8F3C653A377538EFC1A30E17227F112CB784E0EEBCA5BE9262B11ACBF168B0C2BC5B7E33B9E3F4DC31A46B6543BC0FC2F13141BDFAF3CB4616C08A8A5DA0896A45F3358D6914D6178AC77ABD877BBA87A86598728D1C0488B346976FD2A9C50E1201E26D70F117F44A782826F2F1FF265875E4F55CDD57AAA26B3D845226DBD9D8138B53C724EB3F77C89C39AC83A6EE41C0208AAC4C00235A4EE126DC34EE9F99A4A53A00C631B8CE2654D1EC610B7F8468FE71FF98A842A9CC7F7D0F5D1646419B62DE89447B302DA4171CD1560ADC328191AF95B348AE6249D38B8F2A33ECC58F6D98B9C6E97DD815E6E4AE0E44D0CE30A4DC6B7E8F0683B5D94C05BCF7C77F563D3D3C301A6134ACCF2464D')
    
        if verified in ctx.author.roles and pendingRole not in ctx.author.roles:
            if pending=="Yes" or pending=="Already in Group":
                try:
                    username = ctx.author.display_name
                    user = await roblox.get_user_by_username(username, expand=True)
                except UserNotFound:
                    nickError=discord.Embed(description="Make sure your nickname is your **exact** ROBLOX user (without any tags)\n\n***Use /verify to reset your nickname***",color=discord.Color.red())
                    await ctx.respond(embed=nickError)                

                
                
                group=await roblox.get_group(7528791)
                
                

                if pending=="Yes":
                        try:
                            username = ctx.author.display_name
                            user = await roblox.get_user_by_username(username, expand=True)                           
                            await group.accept_user(user)
                        except BadRequest:
                            pendingError=discord.Embed(description="Pending for the group is a mandatory requirement\nPend here and renlist when done:https://www.roblox.com/groups/7528791/Regn-dItalia",color=discord.Color.red())
                            await ctx.respond(embed=pendingError)
                            succ=False     
                                                            
                if pending=="Already in Group":

                    try:
                        await group.get_member_by_username(username)
                    except BadRequest:
                        ctx.respond("liar you are not in the group")
                        succ=False 

                
               
                
                self.regiment=regiment
                

            
                self.enlistment=discord.Embed(title=f"{user.name}'s Enlistment Request",timestamp=datetime.datetime.now(),color=discord.Color.gold())
                
                self.enlistment.add_field(
                    name="Discord Profile",
                    value=ctx.author.mention,
                    inline=True
                )
                self.enlistment.add_field(
                    name="Timezone",
                    value="``"+timezone+"``"
                )
                self.enlistment.add_field(
                    name="Recruited by",
                    value=f"**{recruiter_ping}**"
                )
                self.enlistment.add_field(
                    name="Roblox Account Creation Date",
                    value="```"+user.created.strftime("%d %b, %Y")+"```",
                    inline=True
                )
                self.enlistment.add_field(
                    name="Discord Account Creation Date",
                    value= "```"+ctx.author.created_at.strftime("%d %b, %Y")+"```",
                    inline=True
                )
                self.enlistment.add_field(
                    name="Server Join Date",
                    value="```"+ctx.author.joined_at.strftime("%d %b, %Y")+"```",
                    inline=True
                )

                user_thumbnails = await roblox.thumbnails.get_user_avatar_thumbnails(
                    users=[user],
                    type=AvatarThumbnailType.bust,
                    size=(420, 420)
                    )
                user_thumbnails=user_thumbnails [0] .image_url

                self.enlistment.set_thumbnail(
                    url=user_thumbnails
                )
                if succ==True:
                    pendingEmbed=discord.Embed(description="Your request has been successfully sent. Please wait for a recruiter to approve it.", color=discord.Color.gold(), timestamp=datetime.datetime.now())
                    await ctx.respond(embed=pendingEmbed)
                    await ctx.author.add_roles(pendingRole)
                    
                    member=await group.get_member_by_username(username)

                    prevRank=(next(filter(lambda role: role.group.id == int(7528791), await member.get_group_roles())).name)
                    
                    if prevRank=="Cittadino":
                        await member.set_rank(20)
                    
                    if regiment=="3° Reggimento Fanteria di Leggera":
                        threeLogs=self.client.get_channel(988555001452449822)
                        logMessage=await threeLogs.send(embed=self.enlistment) 
                        newThreeDict={logMessage.id: ctx.author.id}
                        threeO_dict.update(newThreeDict)
                        await logMessage.add_reaction('✅')
                        await logMessage.add_reaction('❌')
                        
                                            
                    elif regiment=="7° Reggimento Fanteria di Linea":
                        oneLogs=self.client.get_channel(988554778952998922)
                        logMessage=await oneLogs.send(embed=self.enlistment) 
                        newOneODict={logMessage.id: ctx.author.id}
                        rrd_dict.update(newOneODict)
                        await logMessage.add_reaction('✅')
                        await logMessage.add_reaction('❌')
                    
                    elif regiment=="Battaglione Reale d'Istria":
                        istogs=self.client.get_channel(991884045837414440)
                        logMessage=await istogs.send(embed=self.enlistment) 
                        newistDict={logMessage.id: ctx.author.id}
                        istra_dict.update(newistDict)
                        await logMessage.add_reaction('✅')
                        await logMessage.add_reaction('❌')                       
                    
            else:
                pendingError=discord.Embed(description="Pending for the group is a mandatory requirement\nPend here and renlist when done:https://www.roblox.com/groups/7528791/Regn-dItalia",color=discord.Color.red())
                await ctx.respond(embed=pendingError)           



        if verified not in ctx.author.roles:
            verifyError=discord.Embed(description="Please verify through the /verify command before enlisting.",color=discord.Color.red())
            await ctx.respond(embed=verifyError)
        if pendingRole in ctx.author.roles:
            pendingError=discord.Embed(description="You are already pending for another regiment",color=discord.Color.red())
            await ctx.respond(embed=pendingError)
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        guild = self.client.get_guild(935566950568951838)
        
        if payload.channel_id == 988555001452449822:
            for payload.message_id in threeO_dict:
                requests=self.client.get_channel(988555001452449822)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                    
                    if acceptReaction.count==1:
                        ping=await requests.send("<@&972961244308967434>")      

                    if acceptReaction.count > 1:
                        welcomeChannel=self.client.get_channel(972959832443322448)
                        
                        recruitMember = await guild.fetch_member(threeO_dict[payload.message_id])
                        oldNick=recruitMember.display_name


                        enlistmentLogs=self.client.get_channel(988553078699593748)
                        citizen=guild.get_role(968138705695031346)
                        conscrit=guild.get_role(935820819735642122)
                        italyRole=guild.get_role(968135157938806855)  
                        pendingRole=guild.get_role(988581530639167518)
                        threeORole=guild.get_role(935616240360235110)
                        threeODepot=guild.get_role(967622878818349067)


                        await recruitMember.edit(nick=f"[3°] {oldNick}")
                        await recruitMember.remove_roles(citizen)
                        await recruitMember.remove_roles(pendingRole)
                        await recruitMember.add_roles(conscrit)
                        await recruitMember.add_roles(italyRole)
                        await recruitMember.add_roles(threeODepot)
                        await recruitMember.add_roles(threeORole)
                        



                        await welcomeChannel.send(embed=self.enlistment)
                        enlistLogs=discord.Embed(description=f"<@{threeO_dict[payload.message_id]}> has enlisted in {self.regiment}", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del threeO_dict[payload.message_id]
                        await message.delete()
                  

                elif payload.emoji.name=="❌":
                    denyReaction=get(message.reactions, emoji=payload.emoji.name)
                    if denyReaction.count > 1: 
                        threeEnlistmentChannel=self.client.get_channel(936696584622735360)     
                        recruitMember = await guild.fetch_member(threeO_dict[payload.message_id])
                        pendingRole=guild.get_role(988581530639167518)
                        await recruitMember.remove_roles(pendingRole)             
                        await threeEnlistmentChannel.send(f"<@{threeO_dict[payload.message_id]}> Your enlistment has been denied.")
                        del threeO_dict[payload.message_id]
                        await message.delete()
                
             
        elif payload.channel_id == 988554778952998922:
            for payload.message_id in rrd_dict:
                requests=self.client.get_channel(988554778952998922)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                    if acceptReaction.count==1:
                        ping=await requests.send("<@&973018248406769734>")
                    if acceptReaction.count > 1:
                        welcomeChannel=self.client.get_channel(986448787209867274)
                        
                        recruitMember = await guild.fetch_member(rrd_dict[payload.message_id])
                        oldNick=recruitMember.display_name


                        enlistmentLogs=self.client.get_channel(988553078699593748)
                        citizen=guild.get_role(968138705695031346)
                        conscrit=guild.get_role(935820819735642122)
                        italyRole=guild.get_role(968135157938806855)  
                        pendingRole=guild.get_role(988581530639167518)

                        regimentRole=guild.get_role(935616257082933288)
                        regimentDepot=guild.get_role(967622229783363665)


                        await recruitMember.edit(nick=f"[7°] {oldNick}")
                        await recruitMember.remove_roles(citizen)
                        await recruitMember.remove_roles(pendingRole)
                        await recruitMember.add_roles(conscrit)
                        await recruitMember.add_roles(italyRole)
                        await recruitMember.add_roles(regimentDepot)
                        await recruitMember.add_roles(regimentRole)
                        



                        await welcomeChannel.send(embed=self.enlistment)
                        enlistLogs=discord.Embed(description=f"<@{rrd_dict[payload.message_id]}> has enlisted in {self.regiment}", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del rrd_dict[payload.message_id]
                        await message.delete()
                       

                    elif payload.emoji.name=="❌":
                        denyReaction=get(message.reactions, emoji=payload.emoji.name)
                        if denyReaction.count > 1: 
                            renlistmentChannel=self.client.get_channel(967621262287458336)                  
                            await renlistmentChannel.send(f"<@{rrd_dict[payload.message_id]}> Your enlistment has been denied.")
                            recruitMember = await guild.fetch_member(rrd_dict[payload.message_id])
                            pendingRole=guild.get_role(988581530639167518)
                            await recruitMember.remove_roles(pendingRole)

                            del rrd_dict[payload.message_id]
                            await message.delete()
                            
                         

        elif payload.channel_id==991884045837414440:
            for payload.emssage_id in istra_dict:
                requests=self.client.get_channel(991884045837414440)
                message = await requests.fetch_message(payload.message_id)
                
                if payload.emoji.name=="✅":
                   
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                    if acceptReaction.count==1:
                        ping=await requests.send("<@&990835536308633612>")
                    if acceptReaction.count > 1:
                        welcomeChannel=self.client.get_channel(990798911729991691)
                        
                        recruitMember = await guild.fetch_member(istra_dict[payload.message_id])
                        oldNick=recruitMember.display_name


                        enlistmentLogs=self.client.get_channel(988553078699593748)
                        citizen=guild.get_role(968138705695031346)
                        conscrit=guild.get_role(935820819735642122)
                        italyRole=guild.get_role(968135157938806855)  
                        pendingRole=guild.get_role(988581530639167518)
                        istRole=guild.get_role(990792443693785128)
                        istDepot=guild.get_role(990891773247238144)


                        await recruitMember.edit(nick=f"[IST] {oldNick}")
                        await recruitMember.remove_roles(citizen)
                        await recruitMember.remove_roles(pendingRole)
                        await recruitMember.add_roles(conscrit)
                        await recruitMember.add_roles(italyRole)
                        await recruitMember.add_roles(istDepot)
                        await recruitMember.add_roles(istRole)
                        



                        await welcomeChannel.send(f"<a:aware:988239544572837958> ***Welcome to {self.regiment}!***\n{recruitMember.mention} ({self.timezone}) - {self.recruiter}\n\n<#988002891488976927> To view this week's events.\n<#976290795499962428> To view important regimental announcements.\n<#986619177383120956> - To access battle codes, links, and reminders!")
                        enlistLogs=discord.Embed(description=f"<@{istra_dict[payload.message_id]}> has enlisted in {self.regiment}", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del istra_dict[payload.message_id]
                        await message.delete()
                  
    

                elif payload.emoji.name=="❌":
                    denyReaction=get(message.reactions, emoji=payload.emoji.name)
                    if denyReaction.count > 1: 
                        istraEnlistmentChannel=self.client.get_channel(990587678535860264)                  
                        await istraEnlistmentChannel.send(f"<@{istra_dict[payload.message_id]}> Your enlistment has been denied.")
                        recruitMember = await guild.fetch_member(istra_dict[payload.message_id])
                        pendingRole=guild.get_role(988581530639167518)
                        await recruitMember.remove_roles(pendingRole)
                        del istra_dict[payload.message_id]
                        await message.delete()
                                              
                 





                    
        

def setup(client):
    client.add_cog(Conscript(client))   