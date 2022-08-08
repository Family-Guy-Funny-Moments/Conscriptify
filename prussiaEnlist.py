
import discord
import datetime
from roblox import Client
import discord.ext
from discord.ext import commands
from discord.commands import Option,slash_command

from discord.utils import get

from roblox.utilities.exceptions import BadRequest
from roblox.utilities.exceptions import UserNotFound

from roblox.thumbnails import AvatarThumbnailType



guard_dict={}
fvl_dict={}
twen_dict={}
fif_dict={}
pak_dict={}

class Conscript(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.regiment="None"
        self.enlistment=discord.Embed(description="none")
        self.recruiter="None"
        self.timezone="None"
        self.user=None
        self.succ=None

        
    
    @commands.Cog.listener("on ready")
    async def on_ready(self):
        print(f"{self.bot.user} has logged in!")

    
    @slash_command(guild_ids=[724022042483228722],description="Send a request to enlist in a regiment")
    async def enlist(
        self,
        ctx,
        regiment:Option(str, "Choose a regiment", choices=["1. Garde-Regiment zu Fuß","Freikorps von Lützow (FVL)","Nr. 29 \"Rhein\" Infanterie","Nr.5 \"Ost-Preußen\" Infanterie","Preußisches Asiatisches Korps"]),
        pending:Option(str,"A join request to both groups is MANDATORY (You will be denied if you are not pending)", choices=["Yes","Already in Group","No"]),
        timezone:Option(str,"Recruit's timezone"),
        recruiter_ping:Option(str,"@Ping your recruiter, if none just type \"None\"")
    ):  
        await ctx.defer()
     
        self.recruiter=recruiter_ping
        self.timezone=timezone
        guild = self.client.get_guild(724022042483228722)
        verified=guild.get_role(830942092422283284)
        pendingRole=guild.get_role(1000217822565257326)
        
    
        if verified in ctx.author.roles and pendingRole not in ctx.author.roles:
            if pending=="Yes" or pending=="Already in Group":
                roblox = Client('_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_968E5F6A12CA09BA8B31A4291EDC029746715D4BAC6CE27BA89F0DEF36EA870A03721854840777678D99374661B56BB4FBA69BABFA2263570DC93108CB56031D1CCFEC273AD7DD1EE49A988AFE7B0E936ABA8BC44E834379CDFC076A8BDF99B2796A73B2B0C712EEC8AB99F3054789678E185D5281E62703F7BB11E8CBF8752BE5931E738221E88D1DE2DA4AEBF0CA83DDFA4D4C336EDBDCDD431B75BA73A486B117CDCC4697899B2E4E0D3E52E4F5C3EDAA26E56711B45CBFDE30E138EE0F4A3720DAE7F6C62BF0C5E02111864B8F7851F3327911A8CD50D6449A8F933989573B49D954A4D31BC32FB4BDA18EDF2CB067E8D16B734423FC49A3EEA16610EE067EE8928DECF71A2E32A37EE5062E1325F694C7CBFD3E7D08FB76A2FDD86D6152538E891A72EF48EE4480C2F42251524C6DD5C2C67CED5972B08EB8DE2ACFEAA51447D89020490265288DD4EF8B04386F3558142A19607CDB67F23E4204D9B0E68C9CC7D084BEE9365B0FD98ECFE21657ADB76E00')
                self.succ=True
                username = ctx.author.display_name
                self.regiment=regiment
                
                try:
                    user = await roblox.get_user_by_username(username, expand=True)
                    self.user=user.name

                except UserNotFound:
                    nickError=discord.Embed(description="Make sure your nickname is your **exact** ROBLOX user (without any tags)\n\n***Use /verify to reset your nickname***",color=discord.Color.red())
                    await ctx.respond(embed=nickError)
                    self.succ=False

                
                group=await roblox.get_group(6909357)
                

                if pending=="Yes":
                        try:
                            username = ctx.author.display_name
                            user = await roblox.get_user_by_username(username, expand=True)                           
                            await group.accept_user(user)
                            log=self.client.get_channel(985401579853213796)
                            acceptEmbed=discord.Embed(description=f"{username} was accepted into the group through the enlist command.",color=discord.Color.green(), timestamp=datetime.datetime.now())
                            await log.send(embed=acceptEmbed)
                        except BadRequest:
                            pendingError=discord.Embed(description="Pending for the group is a mandatory requirement\n\nPend here and renlist when done:\nhttps://www.roblox.com/groups/6909357/Das-K-nigreich-reu-en\n\n**If you're already in the group, pick the option in the pending parameter.**",color=discord.Color.red())
                            await ctx.respond(embed=pendingError)
                            self.succ=False

                if pending=="Already in Group":

                    try:
                        await group.get_member_by_username(username)
                    except BadRequest:
                        ctx.respond("liar you are not in the group")
                        self.succ=False 

                    

                   
                    
                    

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
                self.enlistment.add_field(
                    name="Roblox Profile Link",
                    value=f"https://www.roblox.com/users/{user.id}/profile"
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
                if self.succ==True:
                    log=self.client.get_channel(985401579853213796)

                    if regiment=="1. Garde-Regiment zu Fuß":
                        gardeChannel=self.client.get_channel(998482469386977351)
                        logMessage=await gardeChannel.send(embed=self.enlistment) 
                        newGardeDict={logMessage.id: ctx.author.id}
                        guard_dict.update(newGardeDict)
                        await logMessage.add_reaction('✅')
                        await logMessage.add_reaction('❌')
                        await gardeChannel.send("<@&975513850977873940>")
                    elif regiment=="Freikorps von Lützow (FVL)":
                        fvlChannel=self.client.get_channel(998482704595169351)
                        logMessage=await fvlChannel.send(embed=self.enlistment) 
                        newFvlDict={logMessage.id: ctx.author.id}
                        fvl_dict.update(newFvlDict)
                        await logMessage.add_reaction('✅')
                        await logMessage.add_reaction('❌')
                        await fvlChannel.send("<@&992161194628616192>")
                    elif regiment=="Nr. 29 \"Rhein\" Infanterie":
                        twenChannel=self.client.get_channel(999538040991137822)
                        logMessage=await twenChannel.send(embed=self.enlistment) 
                        newTwenDict={logMessage.id: ctx.author.id}
                        twen_dict.update(newTwenDict)
                        await logMessage.add_reaction('✅')
                        await logMessage.add_reaction('❌')
                        await twenChannel.send("<@&935329485140680704>")
                    elif regiment=="Nr.5 \"Ost-Preußen\" Infanterie":
                        fifChannel=self.client.get_channel(998484702795141170)
                        logMessage=await fifChannel.send(embed=self.enlistment) 
                        newFifDict={logMessage.id: ctx.author.id}
                        fif_dict.update(newFifDict)
                        await logMessage.add_reaction('✅')
                        await logMessage.add_reaction('❌')
                        await fifChannel.send("<@&994306191729635468>")   
                    elif regiment=="Preußisches Asiatisches Korps":
                        pakChannel=self.client.get_channel(999544685586546822)
                        logMessage=await fifChannel.send(embed=self.enlistment) 
                        newPakDict={logMessage.id: ctx.author.id}
                        pak_dict.update(newPakDict)
                        await logMessage.add_reaction('✅')
                        await logMessage.add_reaction('❌') 
                        await pakChannel.send("<@914898791688196126>")      

                        

                    
                    if self.succ==True:
                        pendingEmbed=discord.Embed(description="Your request has been successfully sent. Please wait for a recruiter to approve it.", color=discord.Color.gold(), timestamp=datetime.datetime.now())
                        await ctx.respond(embed=pendingEmbed)
                        await ctx.author.add_roles(pendingRole)

                        member=await group.get_member_by_username(username)
                        prevRank=(next(filter(lambda role: role.group.id == int(6909357), await member.get_group_roles())).name)
                        if prevRank=="Bürger":
                            await member.set_rank(2)
                            rankEmbed=discord.Embed(description=f"{username} was ranked to Landwehr through the enlist command.",color=discord.Color.green(), timestamp=datetime.datetime.now())
                            await log.send(embed=rankEmbed)            

                        
      
            else:
                pendingError=discord.Embed(description="Pending for the group is a mandatory requirement\nPend here and renlist when done:https://www.roblox.com/groups/6909357/Das-K-nigreich-reu-en",color=discord.Color.red())
                await ctx.respond(embed=pendingError)           



        if verified not in ctx.author.roles:
            verifyError=discord.Embed(description="Please verify through the /verify command before enlisting.",color=discord.Color.red())
            await ctx.respond(embed=verifyError)
        if pendingRole in ctx.author.roles:
            pendingError=discord.Embed(description="You are already pending for another regiment",color=discord.Color.red())
            await ctx.respond(embed=pendingError)


    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        guild = self.client.get_guild(724022042483228722)
        #GUARDIA
        if payload.channel_id == 998482469386977351:
            for payload.message_id in guard_dict:
                requests=self.client.get_channel(998482469386977351)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                    if acceptReaction.count > 1:
                        
                        
                        welcomeChannel=self.client.get_channel(975470815179059262)
                        
                        recruitMember = await guild.fetch_member(guard_dict[payload.message_id])
                        oldNick=recruitMember.display_name


                        enlistmentLogs=self.client.get_channel(998488705155207258)
                        army=guild.get_role(830956246751248405)
                        pending=guild.get_role(1000217822565257326)
                        land=guild.get_role(975195566155915335)
                        burger=guild.get_role(830954299449802783)
                        gardeRole=guild.get_role(975440251357130782)
                        gardeDepot=guild.get_role(975453749449457705)





                        
            
                        await recruitMember.add_roles(army)
                        await recruitMember.add_roles(land)
                        await recruitMember.remove_roles(pending)
                        await recruitMember.remove_roles(burger)  
                        await recruitMember.add_roles(gardeDepot)               
                        await recruitMember.add_roles(gardeRole)

                        await recruitMember.edit(nick=f"[♔] {oldNick}")
                        otherPending=guild.get_role(953367714519474187)
                        await recruitMember.remove_roles(otherPending)

                        welcomeMessage=await welcomeChannel.send(f"<:GardeSquare:993625623576727573> ***Welcome to the 1. Garde-Regiment zu Fuß!***\n{recruitMember.mention} ({self.timezone}) - {self.recruiter}\n\n<#985734787736162364> - To view the events this week\n<#998159800338751548> - To view important regimental announcements.\n<#975656551937343498> - To access battle codes and links.\n<#975656551937343498> - To view various other regimental notices.")
                        await welcomeMessage.add_reaction('<:Franz:731229520824238111>')

                        enlistLogs=discord.Embed(description=f"<@{guard_dict[payload.message_id]}> has enlisted in the 1. Garde-Regiment zu Fuß", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del guard_dict[payload.message_id]
                        await message.delete()
                    


                  

                elif payload.emoji.name=="❌":
                    denyReaction=get(message.reactions, emoji=payload.emoji.name)
                    if denyReaction.count > 1: 
                        pendingRole=guild.get_role(1000217822565257326)
                        recruitMember = await guild.fetch_member(guard_dict[payload.message_id])
                        await recruitMember.remove_roles(pendingRole)
                        thenlistmentChannel=self.client.get_channel(985596547725164674)                  
                        await thenlistmentChannel.send(f"<@{guard_dict[payload.message_id]}> Your enlistment has been denied.")
                        del guard_dict[payload.message_id]
                        await message.delete() 
        #FVL
        elif payload.channel_id == 998482704595169351:
            for payload.message_id in fvl_dict:
                requests=self.client.get_channel(998482704595169351)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                    if acceptReaction.count > 1:
                        
                        
                        welcomeChannel=self.client.get_channel(999534404466651257)
                        
                        recruitMember = await guild.fetch_member(fvl_dict[payload.message_id])
                        oldNick=recruitMember.display_name


                        enlistmentLogs=self.client.get_channel(998488705155207258)
                        army=guild.get_role(830956246751248405)
                        pending=guild.get_role(1000217822565257326)
                        land=guild.get_role(975195566155915335)
                        burger=guild.get_role(830954299449802783)
                        otherPending=guild.get_role(953367714519474187)
                        await recruitMember.remove_roles(otherPending)

                        regRole=guild.get_role(861122498355658782)




                        await recruitMember.edit(nick=f"[FVL] {oldNick}")
            
                        await recruitMember.add_roles(army)
                        await recruitMember.add_roles(land)
                        await recruitMember.remove_roles(pending)
                        await recruitMember.remove_roles(burger)      
                        await recruitMember.add_roles(regRole)



                        welcomeMessage=await welcomeChannel.send(f"<:FreikorpSquare:994369054649356389> ***Welcome to the Freikorps von Lützow!***\n{recruitMember.mention} ({self.timezone}) - {self.recruiter}\n\n<#991434408122916874> - To view our events this week\n<#804151740752068738> - To view important regimental announcements.\n<#728754280848425092> - To view various other regimental notices.\n")
                        await welcomeMessage.add_reaction('<:Franz:731229520824238111>')

                        enlistLogs=discord.Embed(description=f"<@{fvl_dict[payload.message_id]}> has enlisted in the Freikorps von Lützow", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del fvl_dict[payload.message_id]
                        await message.delete()
                    
                elif payload.emoji.name=="❌":
                    denyReaction=get(message.reactions, emoji=payload.emoji.name)
                    if denyReaction.count > 1: 
                        pendingRole=guild.get_role(1000217822565257326)
                        recruitMember = await guild.fetch_member(fvl_dict[payload.message_id])
                        await recruitMember.remove_roles(pendingRole)
                        thenlistmentChannel=self.client.get_channel(991400148011864164)                  
                        await thenlistmentChannel.send(f"<@{fvl_dict[payload.message_id]}> Your enlistment has been denied.")
                        del fvl_dict[payload.message_id]
                        await message.delete() 

        elif payload.channel_id == 999538040991137822:
            for payload.message_id in twen_dict:
                requests=self.client.get_channel(999538040991137822)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                    if acceptReaction.count > 1:
                        
                        
                        welcomeChannel=self.client.get_channel(935266546975145994)
                        
                        recruitMember = await guild.fetch_member(twen_dict[payload.message_id])
                        oldNick=recruitMember.display_name


                        enlistmentLogs=self.client.get_channel(998488705155207258)
                        army=guild.get_role(830956246751248405)
                        pending=guild.get_role(1000217822565257326)
                        land=guild.get_role(975195566155915335)
                        burger=guild.get_role(830954299449802783)


                        regRole=guild.get_role(935226546304725064)
                        companyRole=guild.get_role(989277023056834583)

                        otherPending=guild.get_role(953367714519474187)
                        await recruitMember.remove_roles(otherPending)


                        await recruitMember.edit(nick=f"[29.] {oldNick}")
            
                        await recruitMember.add_roles(army)
                        await recruitMember.add_roles(land)
                        await recruitMember.remove_roles(pending)
                        await recruitMember.remove_roles(burger)      
                        await recruitMember.add_roles(regRole)
                        await recruitMember.add_roles(companyRole)



                        welcomeMessage=await welcomeChannel.send(f"<:29thSquare:993626944002330664> ***Welcome to the Infanterie-Regiment Nr. 29 \"Rhein\"!***\n{recruitMember.mention} ({self.timezone}) - {self.recruiter}\n\n<#935232433283039232> - To view our events this week.\n<#935346157159317604> - To view important regimental announcements.\n<#935232385052708884> - To access battle codes and links.\n<#935231962875048037> - To view various other announcements.\n")
                        await welcomeMessage.add_reaction('<:Franz:731229520824238111>')

                        enlistLogs=discord.Embed(description=f"<@{twen_dict[payload.message_id]}> has enlisted in the Welcome to the Infanterie-Regiment Nr. 29 \"Rhein\"", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del twen_dict[payload.message_id]
                        await message.delete()
                    
                elif payload.emoji.name=="❌":
                    denyReaction=get(message.reactions, emoji=payload.emoji.name)
                    if denyReaction.count > 1: 
                        pendingRole=guild.get_role(1000217822565257326)
                        recruitMember = await guild.fetch_member(twen_dict[payload.message_id])
                        await recruitMember.remove_roles(pendingRole)
                        thenlistmentChannel=self.client.get_channel(995280615186382938)                  
                        await thenlistmentChannel.send(f"<@{twen_dict[payload.message_id]}> Your enlistment has been denied.")
                        del twen_dict[payload.message_id]
                        await message.delete() 

        elif payload.channel_id == 998484702795141170:
            for payload.message_id in fif_dict:
                requests=self.client.get_channel(998484702795141170)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                    if acceptReaction.count > 1:
                        
                        
                        welcomeChannel=self.client.get_channel(994019034796396564)
                        
                        recruitMember = await guild.fetch_member(fif_dict[payload.message_id])
                        oldNick=recruitMember.display_name


                        enlistmentLogs=self.client.get_channel(998488705155207258)
                        army=guild.get_role(830956246751248405)
                        pending=guild.get_role(1000217822565257326)
                        land=guild.get_role(975195566155915335)
                        burger=guild.get_role(830954299449802783)


                        regRole=guild.get_role(994012534979952750)
                        companyRole=guild.get_role(994013290751594587)
                        otherPending=guild.get_role(953367714519474187)
                        await recruitMember.remove_roles(otherPending)



                        await recruitMember.edit(nick=f"[5.] {oldNick}")
            
                        await recruitMember.add_roles(army)
                        await recruitMember.add_roles(land)
                        await recruitMember.remove_roles(pending)
                        await recruitMember.remove_roles(burger)      
                        await recruitMember.add_roles(regRole)
                        await recruitMember.add_roles(companyRole)



                        welcomeMessage=await welcomeChannel.send(f"<:FifthSquare:994754912795774986> ***Welcome to the Nr.5 \"Ost-Preußen\" Infanterie!***\n{recruitMember.mention} ({self.timezone}) - {self.recruiter}\n\n<#994018979582574633> - To view our events this week.\n<#994018855938695188> - To view important regimental announcements.\n<#994018924494594148> - To access battle codes and links.\n<#994018890524930130> - To view various other announcements.\n")
                        await welcomeMessage.add_reaction('<:Franz:731229520824238111>')

                        enlistLogs=discord.Embed(description=f"<@{fif_dict[payload.message_id]}> has enlisted in the Welcome to the Nr.5 \"Ost-Preußen\" Infanterie", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del fif_dict[payload.message_id]
                        await message.delete()
                    
                elif payload.emoji.name=="❌":
                    denyReaction=get(message.reactions, emoji=payload.emoji.name)
                    if denyReaction.count > 1: 
                        pendingRole=guild.get_role(1000217822565257326)
                        recruitMember = await guild.fetch_member(fif_dict[payload.message_id])
                        await recruitMember.remove_roles(pendingRole)
                        thenlistmentChannel=self.client.get_channel(994017065654554644)                  
                        await thenlistmentChannel.send(f"<@{fif_dict[payload.message_id]}> Your enlistment has been denied.")
                        del fif_dict[payload.message_id]
                        await message.delete() 


        elif payload.channel_id == 999544685586546822:
            for payload.message_id in pak_dict:
                requests=self.client.get_channel(999544685586546822)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                    if acceptReaction.count > 1:
                        
                        
                        welcomeChannel=self.client.get_channel(985377022169731082)
                        
                        recruitMember = await guild.fetch_member(pak_dict[payload.message_id])
                        oldNick=recruitMember.display_name


                        enlistmentLogs=self.client.get_channel(999538040991137822)
                        army=guild.get_role(830956246751248405)
                        pending=guild.get_role(1000217822565257326)
                        land=guild.get_role(975195566155915335)
                        burger=guild.get_role(830954299449802783)


                        regRole=guild.get_role(921862789264449536)
                        companyRole=guild.get_role(954342989231169617)

                        otherPending=guild.get_role(953367714519474187)
                        await recruitMember.remove_roles(otherPending)


                        await recruitMember.edit(nick=f"[PAK] {oldNick}")
            
                        await recruitMember.add_roles(army)
                        await recruitMember.add_roles(land)
                        await recruitMember.remove_roles(pending)
                        await recruitMember.remove_roles(burger)      
                        await recruitMember.add_roles(regRole)
                        await recruitMember.add_roles(companyRole)



                        welcomeMessage=await welcomeChannel.send(f"<:PAK:972580305686900736> ***Welcome to the Preußisches Asiatisches Korps!***\n{recruitMember.mention} ({self.timezone}) - {self.recruiter}\n\n<#914902686221094942> - To view our events this week.\n<#914876271408861184> - To view and access important corps announcements, battle codes, and links.\n<#982079872925057095> - To view company shouts.\n")
                        await welcomeMessage.add_reaction('<:Franz:731229520824238111>')

                        enlistLogs=discord.Embed(description=f"<@{pak_dict[payload.message_id]}> has enlisted in the Preußisches Asiatisches Korps", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del pak_dict[payload.message_id]
                        await message.delete()
                    
                elif payload.emoji.name=="❌":
                    denyReaction=get(message.reactions, emoji=payload.emoji.name)
                    if denyReaction.count > 1: 
                        pendingRole=guild.get_role(1000217822565257326)
                        recruitMember = await guild.fetch_member(pak_dict[payload.message_id])
                        await recruitMember.remove_roles(pendingRole)
                        thenlistmentChannel=self.client.get_channel(941541211406209154)                  
                        await thenlistmentChannel.send(f"<@{pak_dict[payload.message_id]}> Your enlistment has been denied.")
                        del pak_dict[payload.message_id]
                        await message.delete() 

   

def setup(client):
    client.add_cog(Conscript(client))