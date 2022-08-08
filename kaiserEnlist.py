
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


bechDict={}
artDict={}

class Kaiser(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.regiment="None"
        self.enlistment=discord.Embed(description="none")
        self.recruiter="None"
        self.timezone="None"
        self.user=None
        self.succ=None

        
    
    @slash_command(guild_ids=[939020447591317544],description="Send a request to enlist in a regiment")
    async def enlist(
        self,
        ctx,
        regiment:Option(str, "Choose a regiment", choices=["Kaiserliche Bewachen","Kaiserliche Artillerie"]),
        pending:Option(str,"A join request to both groups is MANDATORY (You will be denied if else)", choices=["Yes","No"]),
        timezone:Option(str,"Recruit's timezone"),
        recruiter_ping:Option(str,"@Ping your recruiter, if none just type \"None\"")
    ):  
        await ctx.defer()

        self.recruiter=recruiter_ping
        self.timezone=timezone
        guild = self.client.get_guild(939020447591317544)
        verified=guild.get_role(939036198238846976)
        pendingRole=guild.get_role(997509107420508361)
        
  



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

                
                group=await roblox.get_group(11067538)
                inGroup=True
                try:
                    member=await group.get_member_by_username(username)
                except:
                    venusError=discord.Embed(description="Being in the group is a mandatory requirement",color=discord.Color.red())
                    await ctx.respond(embed=venusError)
                    inGroup=False

                if inGroup==True:
                    prevRank=(next(filter(lambda role: role.group.id == int(11067538), await member.get_group_roles())).name)
                    if prevRank=="Ausländer":
                        await member.set_rank(5)
                        rankEmbed=discord.Embed(description=f"{username} was ranked to Kadett through the enlist command.",color=discord.Color.green(), timestamp=datetime.datetime.now())
                        log=guild.get_channel(997510218248368149)
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


                        
                if regiment=="Kaiserliche Bewachen":
                        bechChannel=self.client.get_channel(997529913122898001)
                        logMessage=await bechChannel.send(embed=self.enlistment)
                        newbechDict={logMessage.id: ctx.author.id}
                        bechDict.update(newbechDict)
                        await logMessage.add_reaction('✅')
                        await logMessage.add_reaction('❌') 
                        await bechChannel.send("<@&939645993589305415>") 
                elif regiment=="Kaiserliche Artillerie":
                        bechChannel=self.client.get_channel(998038721691656212)
                        logMessage=await bechChannel.send(embed=self.enlistment)
                        newartDict={logMessage.id: ctx.author.id}
                        artDict.update(newartDict)
                        await logMessage.add_reaction('✅')
                        await logMessage.add_reaction('❌') 
                        await bechChannel.send("<@&939390982905024512>")                     




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
        guild = self.client.get_guild(939020447591317544)

        #bech
        if payload.channel_id == 997529913122898001:
            for payload.message_id in bechDict:

                requests=self.client.get_channel(997529913122898001)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                        
                    if acceptReaction.count > 1:

                        
                        welcomeChannel=self.client.get_channel(996068483139915776)
                        
                        recruitMember = await guild.fetch_member(bechDict[payload.message_id])
                        oldNick=recruitMember.display_name
                        

                        enlistmentLogs=self.client.get_channel(997510287034945556)
                        kadet=guild.get_role(939036544214401025)
                        armyRole=guild.get_role(939034387692011520)  
                        pendingRole=guild.get_role(997509107420508361)

                        regRole=guild.get_role(939646068721864756)


                        await recruitMember.edit(nick=f"[KB] {oldNick}")

                        await recruitMember.remove_roles(pendingRole)
                        await recruitMember.add_roles(kadet)
                        await recruitMember.add_roles(armyRole)
                        await recruitMember.add_roles(regRole)

                        



                        welcomeMessage=await welcomeChannel.send(f"Enter Welcome Message Here")
                        await welcomeMessage.add_reaction('<:Nixey:996424149520089158>')

                        enlistLogs=discord.Embed(description=f"<@{bechDict[payload.message_id]}> has enlisted in the Kaiserliche Bewachen", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del bechDict[payload.message_id]
                        await message.delete()

                elif payload.emoji.name=="❌":
                 denyReaction=get(message.reactions, emoji=payload.emoji.name)
                 if denyReaction.count > 1: 
                    pendingRole=guild.get_role(997509107420508361)
                    recruitMember = await guild.fetch_member(bechDict[payload.message_id])
                    await recruitMember.remove_roles(pendingRole)                     
                    thenlistmentChannel=self.client.get_channel(939372613988405298)                  
                    await thenlistmentChannel.send(f"<@{bechDict[payload.message_id]}> Your enlistment has to the Kaiserliche Bewachen been denied.")
                    del bechDict[payload.message_id]
                    await message.delete() 

        if payload.channel_id == 998038721691656212:
            for payload.message_id in artDict:

                requests=self.client.get_channel(998038721691656212)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                        
                    if acceptReaction.count > 1:

                        
                        welcomeChannel=self.client.get_channel(996068463611220060)
                        
                        recruitMember = await guild.fetch_member(artDict[payload.message_id])
                        oldNick=recruitMember.display_name
                        

                        enlistmentLogs=self.client.get_channel(997510287034945556)
                        kadet=guild.get_role(939036544214401025)
                        armyRole=guild.get_role(939034387692011520)  
                        pendingRole=guild.get_role(997509107420508361)

                        regRole=guild.get_role(939284513014579200)


                        await recruitMember.edit(nick=f"[IA] {oldNick}")

                        await recruitMember.remove_roles(pendingRole)
                        await recruitMember.add_roles(kadet)
                        await recruitMember.add_roles(armyRole)
                        await recruitMember.add_roles(regRole)

                        



                        welcomeMessage=await welcomeChannel.send(f"Enter Welcome Message Here")
                        await welcomeMessage.add_reaction('<:Nixey:996424149520089158>')

                        enlistLogs=discord.Embed(description=f"<@{artDict[payload.message_id]}> has enlisted in the Kaiserliche Artillerie", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del artDict[payload.message_id]
                        await message.delete()

                elif payload.emoji.name=="❌":
                 denyReaction=get(message.reactions, emoji=payload.emoji.name)
                 if denyReaction.count > 1: 
                    pendingRole=guild.get_role(997509107420508361)
                    recruitMember = await guild.fetch_member(artDict[payload.message_id])
                    await recruitMember.remove_roles(pendingRole)                     
                    thenlistmentChannel=self.client.get_channel(939372613988405298)                  
                    await thenlistmentChannel.send(f"<@{artDict[payload.message_id]}> Your enlistment has to the Kaiserliche Artillerie been denied.")
                    del artDict[payload.message_id]
                    await message.delete() 

def setup(client):
    client.add_cog(Kaiser(client))