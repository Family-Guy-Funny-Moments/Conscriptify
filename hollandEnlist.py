
import discord
import gspread
from oauth2client.service_account import ServiceAccountCredentials
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


guard_dict={}
eight_dict={}
jew_dict={}
two_dict={}
marine_dict={}

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

    
    @slash_command(guild_ids=[967480265385603123],description="Send a request to enlist in a regiment")
    async def enlist(
        self,
        ctx,
        regiment:Option(str, "Choose a regiment", choices=["Hollandse Garde", "8de Regiment Infanterie Linie \'Van Zijpe\'","Corps Israëlieten","2nd Regiment Infanterie \'Van Maneil\'","Regiment de Marine"]),
        pending:Option(str,"A join request to both groups is MANDATORY (You will be denied if you are not pending)", choices=["Yes","Already in Group","No"]),
        timezone:Option(str,"Recruit's timezone"),
        recruiter_ping:Option(str,"@Ping your recruiter, if none just type \"None\"")
    ):  
        await ctx.defer()
     
        self.recruiter=recruiter_ping
        self.timezone=timezone
        guild = self.client.get_guild(967480265385603123)
        verified=guild.get_role(974580311499362336)
        pendingRole=guild.get_role(990008116978516060)
        
    
        if verified in ctx.author.roles and pendingRole not in ctx.author.roles:
            if pending=="Yes" or pending=="Already in Group":
                roblox = Client('_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_A19A2F398B151EE66DF4E23F313ECA98DD3ABB2DA79E381F5C6AB59F44355255004E643517CC58A0A9C0E3D98A6C9685DBC05E26A680696F0DAA7D66C940FFCC980072B574C2274066E1EECC51EDE9DF8BFA78F554CCA68E68398388BDE1D788581F6FC15BC85281E318519F1CE5774E62C4992F675270DE68EDA13B160670AB1091546F3CB31BBA5E23DDDCA1B0A37A3441FA1F8CAA6F28EDDAD60852FA68622EB8480627AADAC32DB0B34C086D38254227A1B528CC7E9AAD111F2485F9822AB22D1FD37E1102F64D3DF75F784ECDDBC98681D93DA426F410CF32CD1175D3A35B00F1E338175AF5A583FCC3030F1E5FA076B9C14876A02E32D539AB9FA858034D7D40278CF7687810177731A0A661DF7D0C80770E1A3568661755D82CAD8104242AD4F5CB6971B43A7E78FE582FC02521D5092EB614BA814D369BCECC063E5F6A4EFF110C33743AD9BCB6DB6C12F34349880EA5B9C878AEED89CFF6C6BDEC420B6887D4A4091FA90F957873448286E7E1E4E8654148175CAC4C9122B61DBC328FEEE0986E5D217CAC420764C9BE0886050FE010')                
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

                
                group=await roblox.get_group(12103367)
                

                if pending=="Yes":
                        try:
                            username = ctx.author.display_name
                            user = await roblox.get_user_by_username(username, expand=True)                           
                            await group.accept_user(user)
                            log=self.client.get_channel(990010415201284097)
                            acceptEmbed=discord.Embed(description=f"{username} was accepted into the group through the enlist command.",color=discord.Color.green(), timestamp=datetime.datetime.now())
                            await log.send(embed=acceptEmbed)
                        except BadRequest:
                            pendingError=discord.Embed(description="Pending for the group is a mandatory requirement\n\nPend here and renlist when done:\nhttps://www.roblox.com/groups/12103367/Hollandse-oningrijk \n\n**If you're already in the group, pick the option in the pending parameter.**",color=discord.Color.red())
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
                    log=self.client.get_channel(990010415201284097)

                    if regiment=="Hollandse Garde":
                        gardeChannel=self.client.get_channel(990007087666958436)
                        logMessage=await gardeChannel.send(embed=self.enlistment) 
                        newGardeDict={logMessage.id: ctx.author.id}
                        guard_dict.update(newGardeDict)
                        await logMessage.add_reaction('✅')
                        await logMessage.add_reaction('❌')
                        await gardeChannel.send("<@&990091535041318972>")
                        
                    elif regiment=="8de Regiment Infanterie Linie \'Van Zijpe\'":
                        try:
                            groupID=await roblox.get_group(14706502)
                            await groupID.accept_user(user)
                            accept=discord.Embed(description=f"{user.name} was accepted into the Erste Divisie group.",color=discord.Color.green(),timestamp=datetime.datetime.now())
                            await log.send(embed=accept)
                        except BadRequest:
                            errorEmbed=discord.Embed(description="You are not pending for the division group\nPend here: https://www.roblox.com/groups/14706502/Eerst-Divisie\n\n*If you are already in the division group; leave, repend, and renlist.*",color=discord.Color.red())
                            await ctx.respond(embed=errorEmbed)
                            self.succ=False
                        if self.succ==True:
                            eightChannel=self.client.get_channel(990016942184235059)
                            logMessage=await eightChannel.send(embed=self.enlistment)
                            newEightDict={logMessage.id: ctx.author.id}
                            eight_dict.update(newEightDict)
                            await logMessage.add_reaction('✅')
                            await logMessage.add_reaction('❌') 
                            await eightChannel.send("<@&990008338936893491>") 
                           


                           
                    elif regiment=="Corps Israëlieten":
                        try:
                            groupID=await roblox.get_group(14706502)
                            await groupID.accept_user(user)
                            accept=discord.Embed(description=f"{user.name} was accepted into the Erste Divisie group.",color=discord.Color.green(),timestamp=datetime.datetime.now())
                            await log.send(embed=accept)                            
                        except BadRequest:
                            errorEmbed=discord.Embed(description="You are not pending for the division group\nPend here: https://www.roblox.com/groups/14706502/Eerst-Divisie\n\n*If you are already in the division group; leave, repend, and renlist.*",color=discord.Color.red())
                            await ctx.respond(embed=errorEmbed)
                            self.succ=False

                        if self.succ==True:                       
                            jewChannel=self.client.get_channel(990022852856139776)
                            logMessage=await jewChannel.send(embed=self.enlistment) 
                            newJewDict={logMessage.id: ctx.author.id}
                            jew_dict.update(newJewDict)
                            await logMessage.add_reaction('✅')
                            await logMessage.add_reaction('❌')     
                            await jewChannel.send("<@&975174724143427625>") 

                       
                    elif regiment=="2nd Regiment Infanterie \'Van Maneil\'":

                        try:
                            groupID=await roblox.get_group(14706504)
                            await groupID.accept_user(user)
                            accept=discord.Embed(description=f"{user.name} was accepted into the Tweede Divisie group.",color=discord.Color.green(),timestamp=datetime.datetime.now())
                            await log.send(embed=accept)                                    
                        except BadRequest:
                            errorEmbed=discord.Embed(description="You are not pending for the division group\nPend here: https://www.roblox.com/groups/14706504/Tweede-Divisie\n\n*If you are already in the division group; leave, repend, and renlist.*",color=discord.Color.red())
                            await ctx.respond(embed=errorEmbed)
                            self.succ=False

                        if self.succ==True:                                                               
                            twoChannel=self.client.get_channel(990033058415673455)
                            logMessage=await twoChannel.send(embed=self.enlistment) 
                            newTwoDict={logMessage.id: ctx.author.id}
                            two_dict.update(newTwoDict)
                            await logMessage.add_reaction('✅')
                            await logMessage.add_reaction('❌')
                            await twoChannel.send("<@&990011215633866764>") 
                      
                    elif regiment=="Regiment de Marine":

                        try:
                            groupID=await roblox.get_group(14706504)
                            await groupID.accept_user(user)
                            accept=discord.Embed(description=f"{user.name} was accepted into the Tweede Divisie group.",color=discord.Color.green(),timestamp=datetime.datetime.now())
                            await log.send(embed=accept)
                        except BadRequest:
                            errorEmbed=discord.Embed(description="You are not pending for the division group\nPend here: https://www.roblox.com/groups/14706504/Tweede-Divisie\n\n*If you are already in the division group; leave, repend, and renlist.*",color=discord.Color.red())
                            await ctx.respond(embed=errorEmbed)
                            self.succ=False
                        if self.succ==True:
                            marineChannel=self.client.get_channel(990038374448513084)
                            logMessage=await marineChannel.send(embed=self.enlistment) 
                            newMarineDict={logMessage.id: ctx.author.id}
                            marine_dict.update(newMarineDict)
                            await logMessage.add_reaction('✅')
                            await logMessage.add_reaction('❌')
                            await marineChannel.send("<@&990009772445151272>")   
                    
                    if self.succ==True:
                        pendingEmbed=discord.Embed(description="Your request has been successfully sent. Please wait for a recruiter to approve it.", color=discord.Color.gold(), timestamp=datetime.datetime.now())
                        await ctx.respond(embed=pendingEmbed)
                        await ctx.author.add_roles(pendingRole)

                        member=await group.get_member_by_username(username)
                        prevRank=(next(filter(lambda role: role.group.id == int(12103367), await member.get_group_roles())).name)
                        if prevRank=="Inwoner":
                            await member.set_rank(25)
                            rankEmbed=discord.Embed(description=f"{username} was ranked to Milicien through the enlist command.",color=discord.Color.green(), timestamp=datetime.datetime.now())
                            await log.send(embed=rankEmbed)            

                        
      
            else:
                pendingError=discord.Embed(description="Pending for the group is a mandatory requirement\nPend here and renlist when done:https://www.roblox.com/groups/12103367/Hollandse-oningrijk",color=discord.Color.red())
                await ctx.respond(embed=pendingError)           



        if verified not in ctx.author.roles:
            verifyError=discord.Embed(description="Please verify through the /verify command before enlisting.",color=discord.Color.red())
            await ctx.respond(embed=verifyError)
        if pendingRole in ctx.author.roles:
            pendingError=discord.Embed(description="You are already pending for another regiment",color=discord.Color.red())
            await ctx.respond(embed=pendingError)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        guild = self.client.get_guild(967480265385603123)
        #GUARDIA
        if payload.channel_id == 990007087666958436:
            for payload.message_id in guard_dict:
                requests=self.client.get_channel(990007087666958436)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                    if acceptReaction.count > 1:
                        
                        
                        welcomeChannel=self.client.get_channel(990009978163183636)
                        
                        recruitMember = await guild.fetch_member(guard_dict[payload.message_id])
                        oldNick=recruitMember.display_name


                        enlistmentLogs=self.client.get_channel(990010310230429758)
                        guest=guild.get_role(973823346867314729)
                        citizen=guild.get_role(974862000591093780)
                        milicien=guild.get_role(971330857975554078)
                        hollandRole=guild.get_role(974290598917988392)  
                        pendingRole=guild.get_role(990008116978516060)

                        regRole=guild.get_role(970884742817919076)
                        companyRole=guild.get_role(970884759297351710)



                        await recruitMember.edit(nick=f"[DP] {oldNick}")
                        await recruitMember.remove_roles(citizen)
                        await recruitMember.remove_roles(guest)
                        await recruitMember.remove_roles(pendingRole)
                        await recruitMember.add_roles(milicien)
                        await recruitMember.add_roles(hollandRole)
                        await recruitMember.add_roles(regRole)
                        await recruitMember.add_roles(companyRole)
                        



                        welcomeMessage=await welcomeChannel.send(f"**Welcome to the Hollandse Garde.**\n<@{guard_dict[payload.message_id]}>\n\nYou have now entered the **Garde Pupils** as a **Kandidaten**, in order to move past this stage and become a full member of the Garde Pupils. You must attend a kandidaten training that will scheduled and shouted for in <#970870135747391489>.\n\nIt is advised that before you attend for your kandidaten training, that you take a quick look over the google doc linked below as well as the information channel under the pupils category <#967609512477466624>.\nhttps://docs.google.com/document/d/1jqTHBQnYacWpWObdZRIKSik7mrGlt_Al1XEchTHF-MI/edit?usp=sharing")
                        await welcomeMessage.add_reaction('<:FancyLukas:985327766608183296>')

                        enlistLogs=discord.Embed(description=f"<@{guard_dict[payload.message_id]}> has enlisted in Hollandse Garde", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del guard_dict[payload.message_id]
                        await message.delete()
                    
                        def next_available_row(sheet, cols_to_sample=2):
                            cols = sheet.range(1, 1, sheet.row_count, cols_to_sample)
                            return max([cell.row for cell in cols if cell.value]) + 1

                        scope = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive','https://spreadsheets.google.com/feeds']
                        credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
                        gc = gspread.authorize(credentials)
                        worksheet = gc.open("HOLLANDSE GARDE RECRUITMENT").sheet1
                        next_row = next_available_row(worksheet)

                        #Insert Row
                        now = datetime.datetime.now()
                        date = now.strftime("%m/%d/%Y")
                        worksheet.update_acell("B{}".format(next_row), self.user)
                        other=next_row
                        worksheet.update_acell("C{}".format(other), date)


                  

                elif payload.emoji.name=="❌":
                    denyReaction=get(message.reactions, emoji=payload.emoji.name)
                    if denyReaction.count > 1: 
                        pendingRole=guild.get_role(990008116978516060)
                        recruitMember = await guild.fetch_member(guard_dict[payload.message_id])
                        await recruitMember.remove_roles(pendingRole)
                        thenlistmentChannel=self.client.get_channel(967606733251964979)                  
                        await thenlistmentChannel.send(f"<@{guard_dict[payload.message_id]}> Your enlistment has been denied.")
                        del guard_dict[payload.message_id]
                        await message.delete() 

        #8de
        elif payload.channel_id == 990016942184235059:
            for payload.message_id in eight_dict:
             
                requests=self.client.get_channel(990016942184235059)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                        
                    if acceptReaction.count > 1:
                          
                        
                        welcomeChannel=self.client.get_channel(967952826082926653)
                        
                        recruitMember = await guild.fetch_member(eight_dict[payload.message_id])
                        oldNick=recruitMember.display_name
                        

                        enlistmentLogs=self.client.get_channel(990010310230429758)
                        guest=guild.get_role(973823346867314729)
                        citizen=guild.get_role(974862000591093780)
                        milicien=guild.get_role(971330857975554078)
                        hollandRole=guild.get_role(974290598917988392)  
                        pendingRole=guild.get_role(990008116978516060)

                        firstBrig=guild.get_role(972614054952718376)
                        regRole=guild.get_role(970930162143219732)
                        companyRole=guild.get_role(971542974074867764)


                        await recruitMember.edit(nick=f"[8de] {oldNick}")
                        await recruitMember.remove_roles(citizen)
                        await recruitMember.remove_roles(guest)
                        await recruitMember.remove_roles(pendingRole)
                        await recruitMember.add_roles(milicien)
                        await recruitMember.add_roles(hollandRole)
                        await recruitMember.add_roles(regRole)
                        await recruitMember.add_roles(firstBrig)
                        await recruitMember.add_roles(companyRole)
                        



                        welcomeMessage=await welcomeChannel.send(f"<:8deLion:989629954088140830> ***Welcome to 8de Regiment Infanterie Linie \'Van Zijpe\'!***\n<@{eight_dict[payload.message_id]}> ({self.timezone}) - {self.recruiter}\n\n<#967950494364475522> - To view the events this week.\n<#967950202772258847> - To view important regimental announcements.\n<#967573483125112853> - To access battle codes, links, and reminders.\n<#967573420646735882> - To view company shouts.")
                        await welcomeMessage.add_reaction('<:FancyLukas:985327766608183296>')

                        enlistLogs=discord.Embed(description=f"<@{eight_dict[payload.message_id]}> has enlisted in 8de Regiment Infanterie Linie \'Van Zijpe\'", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del eight_dict[payload.message_id]
                        await message.delete()

                elif payload.emoji.name=="❌":
                 denyReaction=get(message.reactions, emoji=payload.emoji.name)
                 if denyReaction.count > 1: 
                    pendingRole=guild.get_role(990008116978516060)
                    recruitMember = await guild.fetch_member(guard_dict[payload.message_id])
                    await recruitMember.remove_roles(pendingRole)                     
                    thenlistmentChannel=self.client.get_channel(973519416228741180)                  
                    await thenlistmentChannel.send(f"<@{eight_dict[payload.message_id]}> Your enlistment has been denied.")
                    del eight_dict[payload.message_id]
                    await message.delete() 

        #jew
        elif payload.channel_id == 990022852856139776:
            for payload.message_id in jew_dict:
                requests=self.client.get_channel(990022852856139776)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                    if acceptReaction.count > 1:
                        
                        
                        welcomeChannel=self.client.get_channel(967575094039830609)
                        
                        recruitMember = await guild.fetch_member(jew_dict[payload.message_id])
                        oldNick=recruitMember.display_name


                        enlistmentLogs=self.client.get_channel(990010310230429758)
                        guest=guild.get_role(973823346867314729)
                        citizen=guild.get_role(974862000591093780)
                        milicien=guild.get_role(971330857975554078)
                        hollandRole=guild.get_role(974290598917988392)  
                        pendingRole=guild.get_role(990008116978516060)

                        firstBrig=guild.get_role(972614054952718376)
                        regRole=guild.get_role(970930923359068220)
                        companyRole=guild.get_role(971503348484276274)


                        await recruitMember.edit(nick=f"[CI] {oldNick}")
                        await recruitMember.remove_roles(citizen)
                        await recruitMember.remove_roles(guest)
                        await recruitMember.remove_roles(pendingRole)
                        await recruitMember.add_roles(milicien)
                        await recruitMember.add_roles(hollandRole)
                        await recruitMember.add_roles(regRole)
                        await recruitMember.add_roles(firstBrig)
                        await recruitMember.add_roles(companyRole)
                        



                        welcomeMessage=await welcomeChannel.send(f"<:IsraelLion:984150799275921460> ***Welcome to Corps Israëlieten!***\n<@{jew_dict[payload.message_id]}> ({self.timezone}) - {self.recruiter}\n\n<#967575050481991781> - To view the events this week.\n<#967574939727196240> - To view important regimental announcements.\n<#967573483125112853> - To access battle codes, links, and reminders.\n<#973342982357008386> - To learn the basics of the gameplay.")
                        await welcomeMessage.add_reaction('<:FancyLukas:985327766608183296>')

                        enlistLogs=discord.Embed(description=f"<@{jew_dict[payload.message_id]}> has enlisted in Corps Israëlieten", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        await message.delete()
                        del jew_dict[payload.message_id]
                        await message.delete()
                    

                elif payload.emoji.name=="❌":
                    denyReaction=get(message.reactions, emoji=payload.emoji.name)
                    if denyReaction.count > 1: 
                        pendingRole=guild.get_role(990008116978516060)
                        recruitMember = await guild.fetch_member(jew_dict[payload.message_id])
                        await recruitMember.remove_roles(pendingRole)                                     
                        thenlistmentChannel=self.client.get_channel(967572931687370792)                  
                        await thenlistmentChannel.send(f"<@{jew_dict[payload.message_id]}> Your enlistment has been denied.")
                        del jew_dict[payload.message_id]
                        await message.delete()

        #2de
        elif payload.channel_id == 990033058415673455:
            for payload.message_id in two_dict:
                requests=self.client.get_channel(990033058415673455)
                message=await requests.fetch_message(payload.message_id)
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)
                
                    if acceptReaction.count > 1:
                      
                        recruitMember = await guild.fetch_member(two_dict[payload.message_id])
                        oldNick=recruitMember.display_name


                        enlistmentLogs=self.client.get_channel(990010310230429758)
                        guest=guild.get_role(973823346867314729)
                        citizen=guild.get_role(974862000591093780)
                        milicien=guild.get_role(971330857975554078)
                        hollandRole=guild.get_role(974290598917988392)  
                        pendingRole=guild.get_role(990008116978516060)

                        secondBrig=guild.get_role(972614092651130911)
                        regRole=guild.get_role(973528019459244032)
                        companyRole=guild.get_role(973528327946129478)


                        await recruitMember.edit(nick=f"[2de] {oldNick}")
                        await recruitMember.remove_roles(citizen)
                        await recruitMember.remove_roles(guest)
                        await recruitMember.remove_roles(pendingRole)
                        await recruitMember.add_roles(milicien)
                        await recruitMember.add_roles(hollandRole)
                        await recruitMember.add_roles(regRole)
                        await recruitMember.add_roles(secondBrig)
                        await recruitMember.add_roles(companyRole)
                        



                        

                        enlistLogs=discord.Embed(description=f"<@{two_dict[payload.message_id]}> has enlisted in 2nd Regiment Infanterie \'Van Maneil\'", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                        
                        del two_dict[payload.message_id]
                        await message.delete()
                    

                elif payload.emoji.name=="❌":
                    denyReaction=get(message.reactions, emoji=payload.emoji.name)
                    if denyReaction.count > 1: 
                        pendingRole=guild.get_role(990008116978516060)
                        recruitMember = await guild.fetch_member(two_dict[payload.message_id])
                        await recruitMember.remove_roles(pendingRole)                            
                        thenlistmentChannel=self.client.get_channel(973519416228741180)                  
                        await thenlistmentChannel.send(f"<@{two_dict[payload.message_id]}> Your enlistment has been denied.")
                        del two_dict[payload.message_id]
                        await message.delete() 
      
        #Marine
        elif payload.channel_id == 990038374448513084:
            for payload.message_id in marine_dict:
                requests=self.client.get_channel(990038374448513084)
                message=await requests.fetch_message(payload.message_id)
                           
                if payload.emoji.name=="✅":
                    acceptReaction=get(message.reactions, emoji=payload.emoji.name)

                    if acceptReaction.count > 1:
                      
                        welcomeChannel=self.client.get_channel(988268215455068160)
                        
                        recruitMember = await guild.fetch_member(marine_dict[payload.message_id])
                        oldNick=recruitMember.display_name

                        
                        enlistmentLogs=self.client.get_channel(990010310230429758)
                        guest=guild.get_role(973823346867314729)
                        citizen=guild.get_role(974862000591093780)
                        milicien=guild.get_role(971330857975554078)
                        hollandRole=guild.get_role(974290598917988392)  
                        pendingRole=guild.get_role(990008116978516060)

                        secondBrig=guild.get_role(972614092651130911)
                        regRole=guild.get_role(988173890784198736)
                        #companyRole=guild.get_role(973528327946129478)
                

                        await recruitMember.edit(nick=f"[RM] {oldNick}")
                        await recruitMember.remove_roles(citizen)
                        await recruitMember.remove_roles(guest)
                        await recruitMember.remove_roles(pendingRole)
                        await recruitMember.add_roles(milicien)
                        await recruitMember.add_roles(hollandRole)
                        await recruitMember.add_roles(regRole)
                        await recruitMember.add_roles(secondBrig)
                    # await recruitMember.add_roles(companyRole)
                        



                        welcomeMessage=await welcomeChannel.send(f"<:WarLukas:970380386104377377> ***Welcome to Regiment de Marine!***\n<@{marine_dict[payload.message_id]}> ({self.timezone}) - {self.recruiter}\n\n<#988267785626988634> - To view the events this week.\n<#988267649337274398> - To view important regimental announcements.\n<#988267728194400256> - To access battle codes, links, and reminders.\n<#989361249609461810> - To learn about your journey within the Marines.")
                        await welcomeMessage.add_reaction('<:FancyLukas:985327766608183296>')

                        enlistLogs=discord.Embed(description=f"<@{marine_dict[payload.message_id]}> has enlisted in Regiment de Marine", color=discord.Color.green(),timestamp=datetime.datetime.now())
                        enlistLogs.set_footer(text=f"Approved by {payload.member.nick}")
                        await enlistmentLogs.send(embed=enlistLogs)
                    
                        del marine_dict[payload.message_id]
                        await message.delete()

                    

                elif payload.emoji.name=="❌":
                    denyReaction=get(message.reactions, emoji=payload.emoji.name)
                    if denyReaction.count > 1: 
                        pendingRole=guild.get_role(990008116978516060)
                        recruitMember = await guild.fetch_member(marine_dict[payload.message_id])
                        await recruitMember.remove_roles(pendingRole)    
                        thenlistmentChannel=self.client.get_channel(988267426288390144)                  
                        await thenlistmentChannel.send(f"<@{marine_dict[payload.message_id]}> Your enlistment has been denied.")
                        del marine_dict[payload.message_id]
                        await message.delete() 

   

def setup(client):
    client.add_cog(Conscript(client))