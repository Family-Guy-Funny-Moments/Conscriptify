
import discord
import datetime
from roblox import Client
import discord.ext
from discord.ext import commands
from discord.commands import Option, slash_command
from roblox.utilities.exceptions import BadRequest
from roblox.utilities.exceptions import UserNotFound






class Accept(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.succ=False
        
    
    @slash_command(guild_ids=[967480265385603123],description="Accepts user into Dutch Groups (Divisions are role locked).")
    async def accept(self,ctx,username:Option(str,"Roblox Username"),group:Option(str,"Choose a group.", choices=["Hollandse Garde", "Eerste Divisie", "Tweede Divisie", "Main Group"])):
        roblox = Client('_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_A19A2F398B151EE66DF4E23F313ECA98DD3ABB2DA79E381F5C6AB59F44355255004E643517CC58A0A9C0E3D98A6C9685DBC05E26A680696F0DAA7D66C940FFCC980072B574C2274066E1EECC51EDE9DF8BFA78F554CCA68E68398388BDE1D788581F6FC15BC85281E318519F1CE5774E62C4992F675270DE68EDA13B160670AB1091546F3CB31BBA5E23DDDCA1B0A37A3441FA1F8CAA6F28EDDAD60852FA68622EB8480627AADAC32DB0B34C086D38254227A1B528CC7E9AAD111F2485F9822AB22D1FD37E1102F64D3DF75F784ECDDBC98681D93DA426F410CF32CD1175D3A35B00F1E338175AF5A583FCC3030F1E5FA076B9C14876A02E32D539AB9FA858034D7D40278CF7687810177731A0A661DF7D0C80770E1A3568661755D82CAD8104242AD4F5CB6971B43A7E78FE582FC02521D5092EB614BA814D369BCECC063E5F6A4EFF110C33743AD9BCB6DB6C12F34349880EA5B9C878AEED89CFF6C6BDEC420B6887D4A4091FA90F957873448286E7E1E4E8654148175CAC4C9122B61DBC328FEEE0986E5D217CAC420764C9BE0886050FE010')

        try:
            member=await roblox.get_user_by_username(username)
        except UserNotFound:
            nickError=discord.Embed(description="User not found",color=discord.Color.red())
            await ctx.respond(embed=nickError)
            self.succ=False      


        guild = self.client.get_guild(967480265385603123)
        
        if group=="Hollandse Garde":
            gardePersonnel=guild.get_role(970884750304768010)
            gardeOfficer=guild.get_role(970884752531947530)
            if gardePersonnel in ctx.author.roles or gardeOfficer in ctx.author.roles:
                self.succ=True
                groupID=await roblox.get_group(14656615)
                try:
                    await groupID.accept_user(member)
                    success=discord.Embed(description=f"{username}'s join request was accepted in {group} ", color=discord.Color.magenta(),timestamp=datetime.datetime.now())
                    success.set_footer(text=f"By {ctx.author.nick}")
                    logs=self.client.get_channel(990010415201284097)
                    await ctx.respond(embed=success)
                    await logs.send(embed=success)

                except BadRequest:
                    pendingError=discord.Embed(description=f"Join request not found for {username}",color=discord.Color.red())
                    await ctx.respond(embed=pendingError)
        
        elif group=="Eerste Divisie":

            eight1=guild.get_role(970931166104395817)
            eight2=guild.get_role(970931201927954462)
            jew1=guild.get_role(970931302633201744)
            jew2=guild.get_role(970931345436069928)

            if eight1 in ctx.author.roles or eight2 in ctx.author.roles or jew1 in ctx.author.roles or jew2 in ctx.author.roles:
                self.succ=True
                groupID=await roblox.get_group(14706502)
                try:
                    await groupID.accept_user(member)
                    success=discord.Embed(description=f"{username}'s join request was accepted in {group} ", color=discord.Color.magenta(),timestamp=datetime.datetime.now())
                    success.set_footer(text=f"By {ctx.author.nick}")
                    logs=self.client.get_channel(990010415201284097)
                    await ctx.respond(embed=success)
                    await logs.send(embed=success)

                except BadRequest:
                    pendingError=discord.Embed(description=f"Join request not found for {username}",color=discord.Color.red())
                    await ctx.respond(embed=pendingError)   
        elif group=="Tweede Divisie":

            eight1=guild.get_role(973529163665391626)
            eight2=guild.get_role(973529467475599371)
            jew1=guild.get_role(988177251663241227)
            jew2=guild.get_role(988177185783316522)

            if eight1 in ctx.author.roles or eight2 in ctx.author.roles or jew1 in ctx.author.roles or jew2 in ctx.author.roles:
                self.succ=True
                groupID=await roblox.get_group(14706504)
                try:
                    await groupID.accept_user(member)
                    success=discord.Embed(description=f"{username}'s join request was accepted in {group} ", color=discord.Color.magenta(),timestamp=datetime.datetime.now())
                    success.set_footer(text=f"By {ctx.author.nick}")
                    logs=self.client.get_channel(990010415201284097)
                    await ctx.respond(embed=success)
                    await logs.send(embed=success)  
                except BadRequest:
                    pendingError=discord.Embed(description=f"Join request not found for {username}",color=discord.Color.red())
                    await ctx.respond(embed=pendingError)
        elif group=="Main Group":
            self.succ=True
            groupID=await roblox.get_group(12103367)

            try:
                await groupID.accept_user(member)
                success=discord.Embed(description=f"{username}'s join request was accepted in the {group} ", color=discord.Color.magenta(),timestamp=datetime.datetime.now())
                success.set_footer(text=f"By {ctx.author.nick}") 
                await ctx.respond(embed=success)
                await logs.send(embed=success)          
            except BadRequest:
                pendingError=discord.Embed(description=f"Join request not found for {username}",color=discord.Color.red())
                await ctx.respond(embed=pendingError)
        
        if self.succ==False:
            error=discord.Embed(description="You must have the respective division's regimental personnel or underofficer role.",color=discord.Color.red())
            await ctx.respond(embed=error)
            

def setup(client):
    client.add_cog(Accept(client))