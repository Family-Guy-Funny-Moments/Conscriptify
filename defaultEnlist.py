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
from roblox.utilities.exceptions import InternalServerError
from roblox import InternalServerError
import roblox.thumbnails
from roblox.thumbnails import AvatarThumbnailType
import os
from discord.utils import get


messageRecruitIDs_dict={}

class Conscript(commands.Cog):
    def __init__(self, client):
        self.client = client

        
    
    @commands.Cog.listener("on ready")
    async def on_ready(self):
        print(f"{self.bot.user} has logged in!")

    
    @slash_command(guild_ids=[987242853749129226],description="Send a request to enlist in a regiment")
    async def enlist(
        self,
        ctx,
        regiment:Option(str, "Choose a regiment", choices=["9e Régiment d'Infanterie Légère","18e Regiment d'Infanterie de Ligne","Légion Irlandaise"]),
        timezone:Option(str,"Recruit's timezone"),
        pending:Option(str,"A join request to both groups is MANDATORY (You will be denied if you are not pending)", choices=["Yes","No"]),
        recruiter:Option(discord.Member,"Enter your recruiter", required=False)
    ):  
        roblox = Client('_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_AF7D02633BE22C753EAD213D4582636F977C8CF088209A3F42F1E61AA45BEDF884207A9C925B075C0798C0E8FABFFD419EDBF0CC596B49C5C2194202DFB987208FA7A2C93C8554AB10A1246139B585032E648309026002C64EEAC7B03FA967061DB99EB055E0D38EC51C0E4C9D475E4EA8F7B71CA0B6599E5F8A443830A851E86275E51DA985F5A562D5F4F983DB86DA226D7550C0B563B1E2FDE03B8597553A514C1EEB469992ECCB785EA18773FA057C8C96738D8615970FFC218DF60EBD7E612A31DEDD46058170D2D7CD71E73A083A02CF7E9F7441567F9F6A0D8AE68012D26574C3E999075F96456C2F9F38D3C5FE493233332B18172F36662F0761CCB0D54854E4B83A35E9AC5FAA705434C384334153DBA276B6315B675940281E7B1F1FE0F39ADA6BFC8D7946C7ABF06AE45BDD348AC23133FBF20C67B6511ABD45549D6630B9424993745BFC5B623A4FF31C6E51F2AB7DDE60DE0342736B8B3D274392AD14030AF3E8B0A54AFB360E3236E76C74D23A8E24E6CAC2C5F9DC22B8B11FBF5A4AE9')
        username = ctx.author.display_name
        recruitmentLogs=self.client.get_channel(987424570006978570)
        user = await roblox.get_user_by_username(username, expand=True)
    
        enlistment=discord.Embed(title=f"{user.display_name} Enlistment Request",timestamp=datetime.datetime.now(),color=discord.Color.gold())
        
        enlistment.add_field(
            name="Discord Profile",
            value=ctx.author.mention,
            inline=True
        )
        enlistment.add_field(
            name="Timezone",
            value="``"+timezone+"``"
        )
        enlistment.add_field(
            name="Recruited by",
            value=f"**{recruiter}**"
        )
        enlistment.add_field(
            name="Roblox Account Creation Date",
            value="```"+user.created.strftime("%d %b, %Y")+"```",
            inline=True
        )
        enlistment.add_field(
            name="Discord Account Creation Date",
            value= "```"+ctx.author.created_at.strftime("%d %b, %Y")+"```",
            inline=True
        )
        enlistment.add_field(
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

        enlistment.set_thumbnail(
            url=user_thumbnails
        )
        pendingEmbed=discord.Embed(description="Your request has been successfully sent. Please wait for a recruiter to approve it.", color=discord.Color.gold(), timestamp=datetime.datetime.now())
        await ctx.respond(embed=pendingEmbed)
        logMessage=await recruitmentLogs.send(embed=enlistment)
        new_message_recruit_dict={logMessage.id: ctx.author.id}
        messageRecruitIDs_dict.update(new_message_recruit_dict)
        await logMessage.add_reaction('✅')
        await logMessage.add_reaction('❌')
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        enlistmentChannel=self.client.get_channel(987404828324020354)
        recruitmentLogs=self.client.get_channel(987424570006978570)
        enlistmentLogs=self.client.get_channel(987783253954002995)
        if payload.channel_id == 987424570006978570:
            for payload.message_id in messageRecruitIDs_dict:
                message=await recruitmentLogs.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                    if acceptReaction.count > 1:
                        welcomeChannel=self.client.get_channel(987424802560180334)
                        guild = self.client.get_guild(987242853749129226)
                        recruitMember = await guild.fetch_member(messageRecruitIDs_dict[payload.message_id])

                        #roles
                        conscrit = guild.get_role(987418731439345734)
                        chasseur = guild.get_role(987418921361637457)
                        deux= guild.get_role(987418808534847539)
                        grand = guild.get_role(987419249335205969)

                        await recruitMember.add_roles(conscrit)
                        await recruitMember.add_roles(chasseur)
                        await recruitMember.add_roles(deux)
                        await recruitMember.add_roles(grand)

                        await welcomeChannel.send("Insert Welcome Message Here LUL")
                        await enlistmentLogs.send(f"<@{messageRecruitIDs_dict[payload.message_id]}> has enlisted in 9e - Approved by {payload.member.mention}")
                        
                        del messageRecruitIDs_dict[payload.message_id]
                        await message.delete()
                elif payload.emoji.name=="❌":
                    denyReaction=get(message.reactions, emoji=payload.emoji.name)
                    if denyReaction.count > 1:                   
                        await enlistmentChannel.send(f"<@{messageRecruitIDs_dict[payload.message_id]}> Your enlistment has been denied.")
                        del messageRecruitIDs_dict[payload.message_id]
                        await message.delete()
                


                    
        



def setup(client):
    client.add_cog(Conscript(client))