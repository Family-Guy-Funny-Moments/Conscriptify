
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



six_dict={}
seven_dict={}
eight_dict={}
corso_dict={}
guardia_dict={}
interna_dict={}

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

    
    @slash_command(guild_ids=[723941184476676107],description="Send a request to enlist in a regiment")
    async def enlist(
        self,
        ctx,
        regiment:Option(str, "Choose a regiment", choices=["Guardia Reale", "Guardia Interna della Città","6° Reggimento Fanteria di Linea","7° Reggimento d'Oriente","8° Reggimento di Linea","Reggimento Real Corso"]),
        pending:Option(str,"A join request to both groups is MANDATORY (You will be denied if you are not pending)", choices=["Yes","Already in Group","No"]),
        timezone:Option(str,"Recruit's timezone"),
        recruiter_ping:Option(str,"@Ping your recruiter, if none just type \"None\"")
    ):  
        await ctx.defer()
     
        self.recruiter=recruiter_ping
        self.timezone=timezone
        guild = self.client.get_guild(723941184476676107)
        verified=guild.get_role(903374982049058918)
        pendingRole=guild.get_role(988990792662122506)
        
    
        if verified in ctx.author.roles and pendingRole not in ctx.author.roles:
            if pending=="Yes" or pending=="Already in Group":
                roblox = Client('_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_EE8D90B3781472B486F756475A8C70D57FBB7239564B8C0F277C193EE7B65D280632E90BBD02B2B60D2E1FACA7E75CD31F40F0B648CFD5C8051131D8B72BF437D6B72B2B7322F03B4A458A3099925BE9011D2B5978428E5AC95A9CDD3D47524FA4BD9E8338B682F3BF3C29976A637B417DDA562DD18F98FDEFC63AC875D509919B7CA5D485892296A2719E8E6E06024FAFC5AC0D828C243A000AD8A67E267AE6F27131CC9A684BF4027EDB9AD60DBFBEE5263378AB1E94426C2F19275484E072BB17276C560A125F03494966E2C4D9D48E6996DDA082DF1FC480E08249E8B4BF0FAC7896291E0737533E585AFAB328BAA9F96DA686D1A25F918607A246C4E86E72D5DE5800B96AE565FB2EAFFEC1DC7F2B2127AB50295C5EEA4C95B1DBB94F042A477171C86C6F3A76469A651A83BA52880B7FC3B5A8C289BE31598F18F3A1503479913D467C9B8FC70CCBD8B087975E25FF3BA5AB195B638D7DC641AEEA4B5893CD2ACF3749576F484E6DE9B08A11C1C4211FBDD1BCCA459DEA2081D210888F3C67F2C851698936CD5024BFCC48773BFD195D5A')                
                succ=True
                username = ctx.author.display_name
                self.regiment=regiment
                
                try:
                    user = await roblox.get_user_by_username(username, expand=True)
                except UserNotFound:
                    nickError=discord.Embed(description="Make sure your nickname is your **exact** ROBLOX user (without any tags)\n\n***Use /verify to reset your nickname***",color=discord.Color.red())
                    await ctx.respond(embed=nickError)
                    succ=False

                group=await roblox.get_group(6764583)

                if pending=="Yes":
                        try:
                            username = ctx.author.display_name
                            user = await roblox.get_user_by_username(username, expand=True)                           
                            await group.accept_user(user)
                        except BadRequest:
                            pendingError=discord.Embed(description="Pending for the group is a mandatory requirement\n\nPend here and renlist when done:\nhttps://www.roblox.com/groups/6764583/Esercito-NapoIetano",color=discord.Color.red())
                            await ctx.respond(embed=pendingError)
                            succ=False

                if pending=="Already in Group":

                    try:
                        await group.get_member_by_username(username)
                    except BadRequest:
                        ctx.respond("liar you are not in the group")
                        succ=False                 
                             


                self.enlistment=discord.Embed(title=f"{user.display_name}'s Enlistment Request",timestamp=datetime.datetime.now(),color=discord.Color.gold())
                
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

                    if regiment=="Guardia Reale":
                        requestChannel=self.client.get_channel(988920299221315614)
                        logMessage=await requestChannel.send(embed=self.enlistment) 
                        newDict={logMessage.id: ctx.author.id}
                        guardia_dict.update(newDict)
                        await logMessage.add_reaction('✅')
                        await logMessage.add_reaction('❌')
                        await requestChannel.send("<@&903390329317781605>")

                    elif regiment=="Guardia Interna della Città":
                        requestChannel=self.client.get_channel(989339257036497006)
                        logMessage=await requestChannel.send(embed=self.enlistment) 
                        newDict={logMessage.id: ctx.author.id}
                        interna_dict.update(newDict)
                        await logMessage.add_reaction('✅')
                        await logMessage.add_reaction('❌')   
                        await requestChannel.send("<@&966826899202531392>")          
                    elif regiment=="6° Reggimento Fanteria di Linea":      
                        requestChannel=self.client.get_channel(989354746550825031)
                        logMessage=await requestChannel.send(embed=self.enlistment) 
                        newDict={logMessage.id: ctx.author.id}
                        six_dict.update(newDict)
                        await logMessage.add_reaction('✅')
                        await logMessage.add_reaction('❌') 
                        await requestChannel.send("<@&976572331726098472>")
                    elif regiment=="7° Reggimento d'Oriente":
                        requestChannel=self.client.get_channel(989358417284067348)
                        logMessage=await requestChannel.send(embed=self.enlistment) 
                        newDict={logMessage.id: ctx.author.id}
                        seven_dict.update(newDict)
                        await logMessage.add_reaction('✅')
                        await logMessage.add_reaction('❌')    
                        await requestChannel.send("<@&933365012964212798>") 
                    elif regiment=="8° Reggimento di Linea":
                        requestChannel=self.client.get_channel(989361834253500526)
                        logMessage=await requestChannel.send(embed=self.enlistment) 
                        newDict={logMessage.id: ctx.author.id}
                        eight_dict.update(newDict)
                        await logMessage.add_reaction('✅')
                        await logMessage.add_reaction('❌')  
                        await requestChannel.send("<@&988564112541904938>")             
                    elif regiment=="Reggimento Real Corso":
                        requestChannel=self.client.get_channel(989365608980299796)
                        logMessage=await requestChannel.send(embed=self.enlistment) 
                        newDict={logMessage.id: ctx.author.id}
                        corso_dict.update(newDict)
                        await logMessage.add_reaction('✅')
                        await logMessage.add_reaction('❌')    
                        await requestChannel.send("<@&971177418691854396>")                                                                
                        
      
            else:
                pendingError=discord.Embed(description="Pending for the group is a mandatory requirement\nPend here and renlist when done:https://www.roblox.com/groups/6764583/Esercito-NapoIetano",color=discord.Color.red())
                await ctx.respond(embed=pendingError)           



        if verified not in ctx.author.roles:
            verifyError=discord.Embed(description="Please verify through the /verify command before enlisting.",color=discord.Color.red())
            await ctx.respond(embed=verifyError)
        if pendingRole in ctx.author.roles:
            pendingError=discord.Embed(description="You are already pending for another regiment",color=discord.Color.red())
            await ctx.respond(embed=pendingError)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        guild = self.client.get_guild(723941184476676107)
        #GUARDIA
        if payload.channel_id == 988920299221315614:
            for payload.message_id in guardia_dict:
                requests=self.client.get_channel(988920299221315614)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                    if acceptReaction.count > 1:
                        welcomeChannel=self.client.get_channel(893494250195550298)
                        
                        recruitMember = await guild.fetch_member(guardia_dict[payload.message_id])
                        oldNick=recruitMember.display_name


                        enlistmentLogs=self.client.get_channel(988922262893789235)
                        citizen=guild.get_role(903381796643823666)
                        conscrit=guild.get_role(903375521667239977)
                        naplesRole=guild.get_role(903389394826838077)  
                        pendingRole=guild.get_role(988990792662122506)

                        regRole=guild.get_role(903390329317781605)
                        companyRole=guild.get_role(947524798072889344)


                        await recruitMember.edit(nick=f"[MG] {oldNick}")
                        await recruitMember.remove_roles(citizen)
                        await recruitMember.remove_roles(pendingRole)
                        await recruitMember.add_roles(conscrit)
                        await recruitMember.add_roles(naplesRole)
                        await recruitMember.add_roles(regRole)
                        await recruitMember.add_roles(companyRole)
                        



                        welcomeMessage=await welcomeChannel.send(f"<:Guardia:830632425079439380> ***Welcome to Guardia Reale!***\n<@{guardia_dict[payload.message_id]}> ({self.timezone}) - {self.recruiter}\n\n<#903632019655888916> - To view this week's events.\n<#947525562434482216> <#910199433021497394> - To view important regimental and company announcements\n<#970803395575308338> - To access event codes, links!")
                        await welcomeMessage.add_reaction('<:Esercito:798662212780556349>')

                        enlistLogs=discord.Embed(description=f"<@{guardia_dict[payload.message_id]}> has enlisted in {self.regiment}", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del guardia_dict[payload.message_id]
                        await message.delete()
                    

                elif payload.emoji.name=="❌":
                    denyReaction=get(message.reactions, emoji=payload.emoji.name)
                    if denyReaction.count > 1: 
                        guardiaEnlistmentChannel=self.client.get_channel(940636539971596298)                  
                        await guardiaEnlistmentChannel.send(f"<@{guardia_dict[payload.message_id]}> Your enlistment has been denied.")
                        del guardia_dict[payload.message_id]
                        await message.delete() 

        if payload.channel_id==989339257036497006:
            for payload.message_id in interna_dict:
                requests=self.client.get_channel(989339257036497006)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                    if acceptReaction.count > 1:
                        welcomeChannel=self.client.get_channel(975573103293915186)
                        
                        recruitMember = await guild.fetch_member(interna_dict[payload.message_id])
                        oldNick=recruitMember.display_name


                        enlistmentLogs=self.client.get_channel(988922262893789235)
                        citizen=guild.get_role(903381796643823666)
                        conscrit=guild.get_role(903375521667239977)
                        naplesRole=guild.get_role(903389394826838077)  
                        pendingRole=guild.get_role(988990792662122506)

                        regRole=guild.get_role(966826899202531392)
                        companyRole=guild.get_role(966827782816530493)


                        await recruitMember.edit(nick=f"[SI] {oldNick}")
                        await recruitMember.remove_roles(citizen)
                        await recruitMember.remove_roles(pendingRole)
                        await recruitMember.add_roles(conscrit)
                        await recruitMember.add_roles(naplesRole)
                        await recruitMember.add_roles(regRole)
                        await recruitMember.add_roles(companyRole)
                        



                        welcomeMessage=await welcomeChannel.send(f"<:Guardia:830632425079439380> ***Welcome to {self.regiment}!***\n<@{interna_dict[payload.message_id]}> ({self.timezone}) - {self.recruiter}\n\n<#966837453367439431> - To view this week's events.\n<#966837000349048902> - To view important regimental announcements\n<#966837392977829898> - To access event reminders, codes, links!")
                        await welcomeMessage.add_reaction('<:Esercito:798662212780556349>')

                        enlistLogs=discord.Embed(description=f"<@{interna_dict[payload.message_id]}> has enlisted in {self.regiment}", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del interna_dict[payload.message_id]
                        await message.delete()
                    

                elif payload.emoji.name=="❌":
                    denyReaction=get(message.reactions, emoji=payload.emoji.name)
                    if denyReaction.count > 1: 
                        theEnlistmentChannel=self.client.get_channel(966877886327971840)                  
                        await theEnlistmentChannel.send(f"<@{interna_dict[payload.message_id]}> Your enlistment has been denied.")
                        del interna_dict[payload.message_id]
                        await message.delete() 

        if payload.channel_id==989354746550825031:
            for payload.message_id in six_dict:
                requests=self.client.get_channel(989354746550825031)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                    if acceptReaction.count > 1:
                        welcomeChannel=self.client.get_channel(975430064541954048)
                        
                        recruitMember = await guild.fetch_member(six_dict[payload.message_id])
                        oldNick=recruitMember.display_name


                        enlistmentLogs=self.client.get_channel(988922262893789235)
                        citizen=guild.get_role(903381796643823666)
                        conscrit=guild.get_role(903375521667239977)
                        naplesRole=guild.get_role(903389394826838077)  
                        pendingRole=guild.get_role(988990792662122506)

                        regRole=guild.get_role(975588363790876732)
                        companyRole=guild.get_role(975430808229789776)
                        sixRole=guild.get_role(975483748621619232)


                        await recruitMember.edit(nick=f"[6°] {oldNick}")
                        await recruitMember.remove_roles(citizen)
                        await recruitMember.remove_roles(pendingRole)
                        await recruitMember.add_roles(conscrit)
                        await recruitMember.add_roles(naplesRole)
                        await recruitMember.add_roles(regRole)
                        await recruitMember.add_roles(companyRole)
                        await recruitMember.add_roles(sixRole)
                        



                        welcomeMessage=await welcomeChannel.send(f"<:6o:798660504213651496> ***Welcome to {self.regiment}!***\n<@{six_dict[payload.message_id]}> ({self.timezone}) - {self.recruiter}\n\n<#975430104014553158> - To view this week's events.\n<#980985446165274654> - To view important regimental announcements\n<#975557383101231114> - To access event reminders, codes, links!\n<#975430018182307910> To view various other regimental notices")
                        await welcomeMessage.add_reaction('<:Esercito:798662212780556349>')

                        enlistLogs=discord.Embed(description=f"<@{six_dict[payload.message_id]}> has enlisted in {self.regiment}", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del six_dict[payload.message_id]
                        await message.delete()
                    

                elif payload.emoji.name=="❌":
                    denyReaction=get(message.reactions, emoji=payload.emoji.name)
                    if denyReaction.count > 1: 
                        theEnlistmentChannel=self.client.get_channel(975429967754174514)                  
                        await theEnlistmentChannel.send(f"<@{six_dict[payload.message_id]}> Your enlistment has been denied.")
                        del six_dict[payload.message_id]
                        await message.delete() 

        if payload.channel_id==989361834253500526:
            for payload.message_id in eight_dict:
                requests=self.client.get_channel(989361834253500526)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                    if acceptReaction.count > 1:
                        welcomeChannel=self.client.get_channel(988555858956939366)
                        
                        recruitMember = await guild.fetch_member(eight_dict[payload.message_id])
                        oldNick=recruitMember.display_name


                        enlistmentLogs=self.client.get_channel(988922262893789235)
                        citizen=guild.get_role(903381796643823666)
                        conscrit=guild.get_role(903375521667239977)
                        naplesRole=guild.get_role(903389394826838077)  
                        pendingRole=guild.get_role(988990792662122506)

                        regRole=guild.get_role(988541116724965443)
                        companyRole=guild.get_role(988564130220896256)


                        await recruitMember.edit(nick=f"[8°] {oldNick}")
                        await recruitMember.remove_roles(citizen)
                        await recruitMember.remove_roles(pendingRole)
                        await recruitMember.add_roles(conscrit)
                        await recruitMember.add_roles(naplesRole)
                        await recruitMember.add_roles(regRole)
                        await recruitMember.add_roles(companyRole)
                        



                        welcomeMessage=await welcomeChannel.send(f"<:Esercito:798662212780556349> ***Welcome to {self.regiment}!***\n<@{eight_dict[payload.message_id]}> ({self.timezone}) - {self.recruiter}\n\n<#988555782599618630> - To view this week's events.\n<#988543927630069790> - To view important regimental announcements\n<#988555603964223608> - To access event reminders, codes, links!")
                        await welcomeMessage.add_reaction('<:Esercito:798662212780556349>')

                        enlistLogs=discord.Embed(description=f"<@{eight_dict[payload.message_id]}> has enlisted in {self.regiment}", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del eight_dict[payload.message_id]
                        await message.delete()
                    

                elif payload.emoji.name=="❌":
                    denyReaction=get(message.reactions, emoji=payload.emoji.name)
                    if denyReaction.count > 1: 
                        theEnlistmentChannel=self.client.get_channel(988543659047800903)                  
                        await theEnlistmentChannel.send(f"<@{eight_dict[payload.message_id]}> Your enlistment has been denied.")
                        del eight_dict[payload.message_id]
                        await message.delete() 

        if payload.channel_id==989365608980299796:
            for payload.message_id in corso_dict:
                requests=self.client.get_channel(989365608980299796)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                    if acceptReaction.count > 1:
                        welcomeChannel=self.client.get_channel(989367198793469972)
                        
                        recruitMember = await guild.fetch_member(corso_dict[payload.message_id])
                        oldNick=recruitMember.display_name


                        enlistmentLogs=self.client.get_channel(988922262893789235)
                        citizen=guild.get_role(903381796643823666)
                        conscrit=guild.get_role(903375521667239977)
                        naplesRole=guild.get_role(903389394826838077)  
                        pendingRole=guild.get_role(988990792662122506)

                        regRole=guild.get_role(903388543357947944)
                        corsoRole=guild.get_role(919643975005122670)


                        await recruitMember.edit(nick=f"[RC] {oldNick}")
                        await recruitMember.remove_roles(citizen)
                        await recruitMember.remove_roles(pendingRole)
                        await recruitMember.add_roles(conscrit)
                        await recruitMember.add_roles(naplesRole)
                        await recruitMember.add_roles(regRole)

                        await recruitMember.add_roles(corsoRole)
                        



                        welcomeMessage=await welcomeChannel.send(f"<:Corso:798662183176241162> ***Welcome to {self.regiment}!***\n<@{corso_dict[payload.message_id]}> ({self.timezone}) - {self.recruiter}\n\n<#903407951140761601> - To view this week's events.\n<#903405097919348756> - To view important regimental announcements\n<#903408514960064542> - To access event reminders, codes, links!")
                        await welcomeMessage.add_reaction('<:Esercito:798662212780556349>')

                        enlistLogs=discord.Embed(description=f"<@{corso_dict[payload.message_id]}> has enlisted in {self.regiment}", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del corso_dict[payload.message_id]
                        await message.delete()
                    

                elif payload.emoji.name=="❌":
                    denyReaction=get(message.reactions, emoji=payload.emoji.name)
                    if denyReaction.count > 1: 
                        theEnlistmentChannel=self.client.get_channel(903404395981578321)                  
                        await theEnlistmentChannel.send(f"<@{corso_dict[payload.message_id]}> Your enlistment has been denied.")
                        del corso_dict[payload.message_id]
                        await message.delete()  

        if payload.channel_id==989358417284067348:
            for payload.message_id in seven_dict:
                requests=self.client.get_channel(989358417284067348)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                    if acceptReaction.count > 1:
                        welcomeChannel=self.client.get_channel(903458386585214986)
                        
                        recruitMember = await guild.fetch_member(seven_dict[payload.message_id])
                        oldNick=recruitMember.display_name


                        enlistmentLogs=self.client.get_channel(988922262893789235)
                        citizen=guild.get_role(903381796643823666)
                        conscrit=guild.get_role(903375521667239977)
                        naplesRole=guild.get_role(903389394826838077)  
                        pendingRole=guild.get_role(988990792662122506)

                        regRole=guild.get_role(903405285824163860)
                        companyRole=guild.get_role(903405887471906836)
           


                        await recruitMember.edit(nick=f"[7°] {oldNick}")
                        await recruitMember.remove_roles(citizen)
                        await recruitMember.remove_roles(pendingRole)
                        await recruitMember.add_roles(conscrit)
                        await recruitMember.add_roles(naplesRole)
                        await recruitMember.add_roles(regRole)
                        await recruitMember.add_roles(companyRole)
                        



                        welcomeMessage=await welcomeChannel.send(f"<:7o:804776868459970560> ***Welcome to {self.regiment}!***\n<@{seven_dict[payload.message_id]}> ({self.timezone}) - {self.recruiter}\n\n<#903436975296643163> - To view this week's events.\n<#954181593415708772> - To view important regimental announcements\n<#903436419744301056> - To access event reminders, codes, links!")
                        await welcomeMessage.add_reaction('<:Esercito:798662212780556349>')

                        enlistLogs=discord.Embed(description=f"<@{seven_dict[payload.message_id]}> has enlisted in {self.regiment}", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del seven_dict[payload.message_id]
                        await message.delete()
                    

                elif payload.emoji.name=="❌":
                    denyReaction=get(message.reactions, emoji=payload.emoji.name)
                    if denyReaction.count > 1: 
                        theEnlistmentChannel=self.client.get_channel(903436192832425984)                  
                        await theEnlistmentChannel.send(f"<@{seven_dict[payload.message_id]}> Your enlistment has been denied.")
                        del seven_dict[payload.message_id]
                        await message.delete()     

def setup(client):
    client.add_cog(Conscript(client))