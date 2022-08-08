
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


firstDict={}
secondDict={}
thirdDict={}
fourthDict={}

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

    
    @slash_command(guild_ids=[847942721754759178],description="Send a request to enlist in a regiment")
    async def enlist(
        self,
        ctx,
        regiment:Option(str, "Choose a regiment", choices=["1. Regiment Kaiserliche Garde","2. Kaiserliche Infanterieregiment","3. Kaiserliche Scharmützlerregiment","4. Kaiserliche Infanterieregiment"]),
        pending:Option(str,"A join request to both groups is MANDATORY (You will be denied if else)", choices=["Yes","No"]),
        timezone:Option(str,"Recruit's timezone"),
        recruiter_ping:Option(str,"@Ping your recruiter, if none just type \"None\"")
    ):  
        await ctx.defer()

        self.recruiter=recruiter_ping
        self.timezone=timezone
        guild = self.client.get_guild(847942721754759178)
        verified=guild.get_role(849750635360157696)
        pendingRole=guild.get_role(996984616277782609)
        
  



        if verified in ctx.author.roles and pendingRole not in ctx.author.roles:
            if pending=="Yes":
                roblox = Client('_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_0B355CB4129DCBA338DF8A9E247EC28C237D74AC444F2B36503D2EB4CEC33F4494CB29AE5C6B0E40D452A9E1146470AE5FDBAC0F48696F0295E8EA85BEDB2266233D7B9F5C1651C28CE2B11C5321D996E4A67F20FFB309D00D1C7065C513C5624483B9B961DBF92687077769A2FCC479E9CB375A5DAFDC689275AA6A3C7B60B6A6DACDB5AF48B8FCF2FDE7748B7A6A36B199161779FD786EA3C8A52070A0FBB5A567205ED7A80DF94767B061545F3B970926139017D09EDC8A77DEA6FCD34199FC9EC661D2CF29CD6BE70A28E9FD1F2451DB5D6B5EE6654363498294858C58A670D3E87DC1C9AD3BA1132CC9CFA4B151CA300FB4EA3E422A01BDEC2353483A1471C144C2894926C1CAC52401B0EDC4BAFE3180F350EC473BD9814D6622A7F51436C0122C47E9A7B1A5952E2EFE02B7A59D9B1467901E87FB11C8CD18C8BCDE8A79F830A410AEACB9BD7A0009B90F6A86D136CA893131CCBFC7A41C2F17F4A776FCB719DA5552E24AAA6FAB6137CB0721886D6E436EE0F3078539B12F6E1CD1A9464F1209')                
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

                
                group=await roblox.get_group(13950045)
                inGroup=True
                try:
                    member=await group.get_member_by_username(username)
                except:
                    venusError=discord.Embed(description="Being in the group is a mandatory requirement",color=discord.Color.red())
                    await ctx.respond(embed=venusError)
                    inGroup=False

                if inGroup==True:
                    prevRank=(next(filter(lambda role: role.group.id == int(13950045), await member.get_group_roles())).name)
                    if prevRank=="Ausländer":
                        await member.set_rank(5)
                        rankEmbed=discord.Embed(description=f"{username} was ranked to Kadett through the enlist command.",color=discord.Color.green(), timestamp=datetime.datetime.now())
                        log=guild.get_channel(996985362620633150)
                        await log.send(embed=rankEmbed)                     
                
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


                        
                if regiment=="1. Regiment Kaiserliche Garde":
                        firChannel=self.client.get_channel(996988098720309258)
                        logMessage=await firChannel.send(embed=self.enlistment)
                        newFirstDict={logMessage.id: ctx.author.id}
                        firstDict.update(newFirstDict)
                        await logMessage.add_reaction('✅')
                        await logMessage.add_reaction('❌') 
                        await firChannel.send("<@&851926238725013554>") 

                elif regiment=="2. Kaiserliche Infanterieregiment":
                        secChannel=self.client.get_channel(996995119792275527)
                        logMessage=await secChannel.send(embed=self.enlistment)
                        newSecondDict={logMessage.id: ctx.author.id}
                        secondDict.update(newSecondDict)
                        await logMessage.add_reaction('✅')
                        await logMessage.add_reaction('❌') 
                        await secChannel.send("<@&851926259637420122>")     

                elif regiment=="3. Kaiserliche Scharmützlerregiment":
                        thirChannel=self.client.get_channel(996997626652282931)
                        logMessage=await thirChannel.send(embed=self.enlistment)
                        newThirdDict={logMessage.id: ctx.author.id}
                        thirdDict.update(newThirdDict)
                        await logMessage.add_reaction('✅')
                        await logMessage.add_reaction('❌') 
                        await thirChannel.send("<@&851926279070548019>")      

                elif regiment=="4. Kaiserliche Infanterieregiment":
                        fourChannel=self.client.get_channel(997000057415020574)
                        logMessage=await fourChannel.send(embed=self.enlistment)
                        newFourDict={logMessage.id: ctx.author.id}
                        fourthDict.update(newFourDict)
                        await logMessage.add_reaction('✅')
                        await logMessage.add_reaction('❌') 
                        await thirChannel.send("<@&931413026131808286>")                          



                pendingEmbed=discord.Embed(description="Your request has been successfully sent. Please wait for a recruiter to approve it.", color=discord.Color.gold(), timestamp=datetime.datetime.now())
                await ctx.respond(embed=pendingEmbed)
                await ctx.author.add_roles(pendingRole)


        if verified not in ctx.author.roles:
            verifyError=discord.Embed(description="Please verify through the /verify command before enlisting.",color=discord.Color.red())
            await ctx.respond(embed=verifyError)
        if pendingRole in ctx.author.roles:
            pendingError=discord.Embed(description="You are already pending for another regiment",color=discord.Color.red())
            await ctx.respond(embed=pendingError)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        guild = self.client.get_guild(847942721754759178)

        #1st
        if payload.channel_id == 996988098720309258:
            for payload.message_id in firstDict:

                requests=self.client.get_channel(996988098720309258)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                        
                    if acceptReaction.count > 1:

                        
                        welcomeChannel=self.client.get_channel(996067937452564490)
                        
                        recruitMember = await guild.fetch_member(firstDict[payload.message_id])
                        oldNick=recruitMember.display_name
                        

                        enlistmentLogs=self.client.get_channel(996986228186566686)
                        kadet=guild.get_role(848628008596406323)
                        armyRole=guild.get_role(848627443081936927)  
                        pendingRole=guild.get_role(996984616277782609)

                        regRole=guild.get_role(851924157515038720)


                        await recruitMember.edit(nick=f"[1.] {oldNick}")

                        await recruitMember.remove_roles(pendingRole)
                        await recruitMember.add_roles(kadet)
                        await recruitMember.add_roles(armyRole)
                        await recruitMember.add_roles(regRole)

                        



                        welcomeMessage=await welcomeChannel.send(f"Enter Welcome Message Here")
                        await welcomeMessage.add_reaction('<:Maverick:996424357863751721>')

                        enlistLogs=discord.Embed(description=f"<@{firstDict[payload.message_id]}> has enlisted in the 1. Regiment Kaiserliche Garde", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del firstDict[payload.message_id]
                        await message.delete()

                elif payload.emoji.name=="❌":
                 denyReaction=get(message.reactions, emoji=payload.emoji.name)
                 if denyReaction.count > 1: 
                    pendingRole=guild.get_role(996984616277782609)
                    recruitMember = await guild.fetch_member(firstDict[payload.message_id])
                    await recruitMember.remove_roles(pendingRole)                     
                    thenlistmentChannel=self.client.get_channel(931357693644525568)                  
                    await thenlistmentChannel.send(f"<@{firstDict[payload.message_id]}> Your enlistment has to the 1. Regiment Kaiserliche Garde been denied.")
                    del firstDict[payload.message_id]
                    await message.delete() 
        #2nd
        elif payload.channel_id == 996995119792275527:
            for payload.message_id in secondDict:

                requests=self.client.get_channel(996995119792275527)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                        
                    if acceptReaction.count > 1:

                        
                        welcomeChannel=self.client.get_channel(996067953076359208)
                        
                        recruitMember = await guild.fetch_member(secondDict[payload.message_id])
                        oldNick=recruitMember.display_name
                        

                        enlistmentLogs=self.client.get_channel(996986228186566686)
                        kadet=guild.get_role(848628008596406323)
                        armyRole=guild.get_role(848627443081936927)  
                        pendingRole=guild.get_role(996984616277782609)

                        regRole=guild.get_role(851924217909608478)


                        await recruitMember.edit(nick=f"[2.] {oldNick}")

                        await recruitMember.remove_roles(pendingRole)
                        await recruitMember.add_roles(kadet)
                        await recruitMember.add_roles(armyRole)
                        await recruitMember.add_roles(regRole)

                        



                        welcomeMessage=await welcomeChannel.send(f"Enter Welcome Message Here")
                        await welcomeMessage.add_reaction('<:Maverick:996424357863751721>')

                        enlistLogs=discord.Embed(description=f"<@{secondDict[payload.message_id]}> has enlisted in the 2. Kaiserliche Infanterieregiment", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del secondDict[payload.message_id]
                        await message.delete()

                elif payload.emoji.name=="❌":
                 denyReaction=get(message.reactions, emoji=payload.emoji.name)
                 if denyReaction.count > 1: 
                    pendingRole=guild.get_role(996984616277782609)
                    recruitMember = await guild.fetch_member(secondDict[payload.message_id])
                    await recruitMember.remove_roles(pendingRole)                     
                    thenlistmentChannel=self.client.get_channel(931357693644525568)                  
                    await thenlistmentChannel.send(f"<@{secondDict[payload.message_id]}> Your enlistment has to the 2. Kaiserliche Infanterieregiment been denied.")
                    del secondDict[payload.message_id]
                    await message.delete() 
        #3rd
        elif payload.channel_id == 996997626652282931:
            for payload.message_id in thirdDict:

                requests=self.client.get_channel(997000057415020574)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                        
                    if acceptReaction.count > 1:

                        
                        welcomeChannel=self.client.get_channel(996067975083864144)
                        
                        recruitMember = await guild.fetch_member(thirdDict[payload.message_id])
                        oldNick=recruitMember.display_name
                        

                        enlistmentLogs=self.client.get_channel(996986228186566686)
                        kadet=guild.get_role(848628008596406323)
                        armyRole=guild.get_role(848627443081936927)  
                        pendingRole=guild.get_role(996984616277782609)

                        regRole=guild.get_role(851924292849500179)


                        await recruitMember.edit(nick=f"[3.] {oldNick}")

                        await recruitMember.remove_roles(pendingRole)
                        await recruitMember.add_roles(kadet)
                        await recruitMember.add_roles(armyRole)
                        await recruitMember.add_roles(regRole)

                        



                        welcomeMessage=await welcomeChannel.send(f"Enter Welcome Message Here")
                        await welcomeMessage.add_reaction('<:Maverick:996424357863751721>')

                        enlistLogs=discord.Embed(description=f"<@{thirdDict[payload.message_id]}> has enlisted in the 3. Kaiserliche Scharmützler regiment", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del thirdDict[payload.message_id]
                        await message.delete()

                elif payload.emoji.name=="❌":
                 denyReaction=get(message.reactions, emoji=payload.emoji.name)
                 if denyReaction.count > 1: 
                    pendingRole=guild.get_role(996984616277782609)
                    recruitMember = await guild.fetch_member(thirdDict[payload.message_id])
                    await recruitMember.remove_roles(pendingRole)                     
                    thenlistmentChannel=self.client.get_channel(931357693644525568)                  
                    await thenlistmentChannel.send(f"<@{thirdDict[payload.message_id]}> Your enlistment has to the 3. Kaiserliche Scharmützler regiment been denied.")
                    del thirdDict[payload.message_id]
                    await message.delete() 
        #4. Kaiserliche Infanterieregiment

        elif payload.channel_id == 997000057415020574:
            for payload.message_id in fourthDict:

                requests=self.client.get_channel(997000057415020574)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                        
                    if acceptReaction.count > 1:

                        
                        welcomeChannel=self.client.get_channel(996067990565040228)
                        
                        recruitMember = await guild.fetch_member(fourthDict[payload.message_id])
                        oldNick=recruitMember.display_name
                        

                        enlistmentLogs=self.client.get_channel(996986228186566686)
                        kadet=guild.get_role(848628008596406323)
                        armyRole=guild.get_role(848627443081936927)  
                        pendingRole=guild.get_role(996984616277782609)

                        regRole=guild.get_role(931413026979057754)


                        await recruitMember.edit(nick=f"[4.] {oldNick}")

                        await recruitMember.remove_roles(pendingRole)
                        await recruitMember.add_roles(kadet)
                        await recruitMember.add_roles(armyRole)
                        await recruitMember.add_roles(regRole)

                        



                        welcomeMessage=await welcomeChannel.send(f"Enter Welcome Message Here")
                        await welcomeMessage.add_reaction('<:Maverick:996424357863751721>')

                        enlistLogs=discord.Embed(description=f"<@{fourthDict[payload.message_id]}> has enlisted in the 4. Kaiserliche Infanterieregiment regiment", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del fourthDict[payload.message_id]
                        await message.delete()

                elif payload.emoji.name=="❌":
                 denyReaction=get(message.reactions, emoji=payload.emoji.name)
                 if denyReaction.count > 1: 
                    pendingRole=guild.get_role(996984616277782609)
                    recruitMember = await guild.fetch_member(fourthDict[payload.message_id])
                    await recruitMember.remove_roles(pendingRole)                     
                    thenlistmentChannel=self.client.get_channel(931357693644525568)                  
                    await thenlistmentChannel.send(f"<@{fourthDict[payload.message_id]}> Your enlistment has to the 4. Kaiserliche Infanterieregiment regiment been denied.")
                    del fourthDict[payload.message_id]
                    await message.delete() 


def setup(client):
    client.add_cog(Conscript(client))