
from random import randint
import discord
import roblox
import datetime
from roblox import Client
import discord.ext
from discord.ext import commands
from discord.commands import Option
from discord.ext.commands import MissingPermissions
from discord.utils import get
import roblox.utilities.exceptions
from roblox.utilities.exceptions import InternalServerError
from roblox.utilities.exceptions import BadRequest



client = commands.Bot(command_prefix = '=')



@client.event 
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="Rey de España"))

@client.slash_command(guild_ids=[894363477731328040],description="Information about Conscriptify!")
async def help(ctx):
    info=discord.Embed(
        description="Use ``/conscript`` to conscript recruits!",
        color=discord.Color(0xe91e63)
    )
    await ctx.respond(embed=info)

#PROMOTION COMMANDS

      
        





@client.slash_command(guild_ids=[894363477731328040],description="Displays bot's response time")
async def ping(ctx):
    ping=discord.Embed(description=f"Pong! {round(client.latency * 1000)}ms",color=discord.Color(0xe91e63))
    await ctx.respond(embed=ping)


@client.slash_command(guild_ids=[894363477731328040],description="Enlists recruit")
async def conscript(ctx,
regiment:Option(str,"Choose a regiment",choices=["Guardia Valona","1º Regimiento de Infantería del Rey","5º Regimiento de Línea de Corona","36º Regimiento de Infantería de Irlanda"]),
recruit:Option(discord.Member,"Recruit Discord username"),
recruiter:Option(discord.Member,"Recruiter Discord username"),
timezone:Option(str,"Recruit's timezone",required=False),
delray_company:Option(str,"[OPTIONAL] (DEL REY) Choose recruit's company", choices=["Burgos","Valencia"],required=False)
):

    #DEFAULT ROLES/VARIABLES
    await ctx.defer()
    suc=True
    oldNick=recruit.display_name


    emoji='<:Espana:897188974483898429>'

    verified=discord.utils.get(ctx.guild.roles, id=894363477752295426)
    mainSpain=discord.utils.get(ctx.guild.roles, id=894363477752295429)
    permissions=discord.utils.get(ctx.guild.roles, id=894363477865541668)
    designation=discord.utils.get(ctx.guild.roles, id=894363477865541662)
    conscript=discord.utils.get(ctx.guild.roles, id=894363477865541669)
    awards=discord.utils.get(ctx.guild.roles, id=894363477752295424)
    

    #GUARDIA CUSTOM
    
 
    #DEL RAY CUSTOM


    #Corona Custom


    #Irlanda Custom

    








    #CODE

    if verified in recruit.roles:
        if regiment=="Guardia Valona":
            
            await recruit.add_roles(awards)
            await recruit.add_roles(mainSpain)
            await recruit.add_roles(permissions)
            await recruit.add_roles(designation)
            await recruit.add_roles(conscript)

            await recruit.edit(nick=f"[GV] {oldNick}")
            guardiaRole=discord.utils.get(ctx.guild.roles,id=957079494311682058)
            guardiaChannel=client.get_channel(986762062485139516)
            centroCorps=discord.utils.get(ctx.guild.roles,id=894363477752295428)

            await recruit.add_roles(guardiaRole)
            await recruit.add_roles(centroCorps)
            guardiaMessage= await guardiaChannel.send(f"<:GuardiaValona:908072003083305071> ***Welcome to Guardia Valona!***\n{recruit.mention} ({timezone}) - {recruiter.mention}\n\n<#917209331232043049> <#957104431109898270> - To view our events this week.\n<#957104253451763732> - To view important regimental announcements,\n <#957104344115867668> - To access battle codes, links, and reminders")
            await guardiaMessage.add_reaction(emoji)
      
          


        elif regiment=="1º Regimiento de Infantería del Rey":
            delrayRole=discord.utils.get(ctx.guild.roles, id=894363477848752130)
            delrayBurgos=discord.utils.get(ctx.guild.roles, id=957421967487688766)
            delrayValencia=discord.utils.get(ctx.guild.roles, id=975573278267695155)
            delrayChannel=client.get_channel(908917275770368040)
            await recruit.add_roles(awards)
            await recruit.add_roles(mainSpain)
            await recruit.add_roles(permissions)
            await recruit.add_roles(designation)
            await recruit.add_roles(conscript)
            await recruit.add_roles(delrayRole)  
            await recruit.add_roles(centroCorps)           
            await recruit.edit(nick=f"[1°] {oldNick}")
            if delray_company=="Burgos":
                await recruit.add_roles(delrayBurgos)
                burgosMessage = await delrayChannel.send(f"<:delRey:897189076573225081> ***Welcome to 1º Regimiento de Infantería del Rey!***\n{recruit.mention} ({timezone}) - {recruiter.mention}\n\n<#917209331232043049> <#894363479144812551> - To view our events this week.\n<#894363479144812548> - To view important regimental announcements,\n <#910403655537147965> - To access battle codes, links, and reminders\n<#968295512883204167> - To view important company announcements")
                await burgosMessage.add_reaction(emoji)
            elif delray_company=="Valencia":
                await recruit.add_roles(delrayValencia)
                valenciaMessage=await delrayChannel.send(f"<:delRey:897189076573225081> ***Welcome to 1º Regimiento de Infantería del Rey!***\n{recruit.mention} ({timezone}) - {recruiter.mention}\n\n<#917209331232043049> <#894363479144812551> - To view our events this week.\n<#894363479144812548> - To view important regimental announcements,\n <#910403655537147965> - To access battle codes, links, and reminders\n<#975572570671816705> - To view important company announcements")
                await valenciaMessage.add_reaction(emoji)
        elif regiment=="5º Regimiento de Línea de Corona":
            coronaChannel=client.get_channel(983671927279341618)
            coronaDepot=discord.utils.get(ctx.guild.roles, id=983238121586049034)
            coronaRole=discord.utils.get(ctx.guild.roles, id=983237377478782977)
            coronaCorps=discord.utils.get(ctx.guild.roles,id=972700194133147649)
            roblox = Client('_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_A3EE0321C970250EF8EBF7A7F3B5A9E359E018632D1887A980FE6ABE8F00B90EC72C21BCEF6D265EF4FCC0E44E70B5E4D0ABE0D8E48F927DCE8524F0C470C84CD42857286A35689F2D9DFED65C167C36D1FF443D50CF22B6FAACAA052FAE39CD0F97B6798EF2C8A0EBB5927233328EA34B43E0FD2B4B4FD794B1DEC5327FE867E9F3B6F4BC31ACF28D448FF19A7A4FF441B330C2BE8C37ADE95E7BAE8F3BC508918AFD2A0E30BD3B525C0A201DA9B887F86A879D73F4D916A2FFF22EC544A311E68D742EDA3286A1ADB0C4322A2A3FDCDAAEE254C13332E559325BCF79B7079CA5AB39425704D6B8D712B67657DEC2573587723FC2E6E6A4CF945C69383AF0DEDE116C129B724449233BA6910C92472B4A9BD7A62D38CA344D32AC4B79D6845C2A3D3D0F537077D471D7C675CEFFC699D1BD3927BEFBE9C69362F38920942334D2C2DCE3C0FE45FF1E0FABC8948337D893EFB846FAAC2E00ACA567C3DBF8C5C49E5558445A2C5360564CDF191788E1610BCEFCE8F31FFB7A1CEFE9847ECE99569E610893E950AB6A0D5BF1D5A4F37A27F4E3CA58')
            group=await roblox.get_group(11898117)
            member=await group.get_member_by_username(oldNick)
            try:
              await group.accept_user(member)
            except BadRequest:
              invalidError=discord.Embed(description=f"No join request found for {oldNick} for the 5o Group.",color=discord.Color.red())
              await ctx.respond(embed=invalidError)
      

  
            await recruit.add_roles(awards)
            await recruit.add_roles(mainSpain)
            await recruit.add_roles(permissions)
            await recruit.add_roles(designation)
            await recruit.add_roles(conscript)
            await recruit.add_roles(coronaDepot)
            await recruit.add_roles(coronaCorps)             
            await recruit.add_roles(coronaRole)
            await recruit.edit(nick=f"[5º] {oldNick}")      

            coronaMessage=await coronaChannel.send(f"<:Corona:897189098257776692> ***Welcome to the 5º Regimiento de Línea de Corona***\n{recruit.mention} ({timezone}) - {recruiter.mention}\n\n<#972719503949578270> <#983241241573609512> - To view this week's events.\n <#983240772524589076> - To view regimental announcements.\n <#986832218141884446> - To access battle codes and links\n <#983240873070440449> - To view various other regimental shouts")          
            await coronaMessage.add_reaction(emoji)
        

        elif regiment=="36º Regimiento de Infantería de Irlanda":
            irlandaChannel=client.get_channel(974006217854816266)
            irlandaRole=discord.utils.get(ctx.guild.roles, id=972627775494189127)
            irlandaepot=discord.utils.get(ctx.guild.roles, id=972702270040977430)
            await recruit.add_roles(awards)
            await recruit.add_roles(mainSpain)
            await recruit.add_roles(permissions)
            await recruit.add_roles(designation)
            await recruit.add_roles(conscript)
            await recruit.add_roles(coronaCorps)
            await recruit.add_roles(irlandaepot)            
            await recruit.add_roles(irlandaRole)   
            await recruit.edit(nick=f"[36º] {oldNick}") 

            irlandaMessage=await irlandaChannel.send(f"<:Irlanda:972959389587742810> ***Welcome to the 36º Regimiento de Infantería de Irlanda!***\n{recruit.mention} ({timezone}) - {recruiter.mention}\n\n<#972719503949578270> <#972696483801493534> - To view this week's events.\n<#972696296123142154> - To view regimental announcements.\n<#972696401815416832> - To access battle codes and links")     
            await irlandaMessage.add_reaction(emoji)

        
    else:
        suc=False
        verifyError=discord.Embed(description=f"{recruit.mention} is not verified, make sure the recruit is verified before executing the command.",color=discord.Color.red())
        await ctx.respond(embed=verifyError)

        
 

    conscriptSuccess=discord.Embed(description=f"{recruit.mention} has successfully enlisted in the {regiment}\nGreat job {recruiter.mention}!",color=discord.Color.green())
    if suc==True:
      await ctx.respond(embed=conscriptSuccess)

@client.slash_command(guild_ids=[894363477731328040],description="Promotes user")
async def setrank(ctx,
username:Option(str,"Roblox Username"),
rank:Option(str,"Select a rank in the group",choices=["Soldado","Soldado de Primera","Caboa","Cabo Primero","Sargento Segundo","Sargento Primero","Sargento Mayor","Alferez","Subteniente"])):
    rankId=0
    if rank=="Soldado":
        rankId=2
    elif rank=="Soldado de Primera":
        rankId=3
    elif rank=="Caboa":
        rankId=4
    elif rank=="Cabo Primero":
        rankId=6
    elif rank=="Sargento Segundo":
        rankId=7
    elif rank=="Sargento Primero":
        rankId==8
    elif rank=="Sargento Mayor":
        rankId=9
    elif rank=="Alferez":
        rankId=10
    elif rank=="Subteniente":
        rankId=246

    roblox=Client('_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_A3EE0321C970250EF8EBF7A7F3B5A9E359E018632D1887A980FE6ABE8F00B90EC72C21BCEF6D265EF4FCC0E44E70B5E4D0ABE0D8E48F927DCE8524F0C470C84CD42857286A35689F2D9DFED65C167C36D1FF443D50CF22B6FAACAA052FAE39CD0F97B6798EF2C8A0EBB5927233328EA34B43E0FD2B4B4FD794B1DEC5327FE867E9F3B6F4BC31ACF28D448FF19A7A4FF441B330C2BE8C37ADE95E7BAE8F3BC508918AFD2A0E30BD3B525C0A201DA9B887F86A879D73F4D916A2FFF22EC544A311E68D742EDA3286A1ADB0C4322A2A3FDCDAAEE254C13332E559325BCF79B7079CA5AB39425704D6B8D712B67657DEC2573587723FC2E6E6A4CF945C69383AF0DEDE116C129B724449233BA6910C92472B4A9BD7A62D38CA344D32AC4B79D6845C2A3D3D0F537077D471D7C675CEFFC699D1BD3927BEFBE9C69362F38920942334D2C2DCE3C0FE45FF1E0FABC8948337D893EFB846FAAC2E00ACA567C3DBF8C5C49E5558445A2C5360564CDF191788E1610BCEFCE8F31FFB7A1CEFE9847ECE99569E610893E950AB6A0D5BF1D5A4F37A27F4E3CA58')
    group=await roblox.get_group(11639829)
    member=await group.get_member_by_username(username)
    prevRank=(next(filter(lambda role: role.group.id == int(11639829), await member.get_group_roles())).name)    
    await member.set_rank(rankId)
    log=discord.Embed(description=f"{ctx.author.mention} ranked {username} to {rank} from {prevRank} in the group.",color=discord.Color.green(),timestamp=datetime.datetime.now())
    await ctx.respond(embed=log)
    logChannel=client.get_channel(986757750451232849)
    await logChannel.send(embed=log)
        
client.run('OTg2NzQ5NTAyNjQ2MDA1NzYw.GpuKdo.h7kZ1mCfuQBl96B03puO8N-mrRZ1bYuoc5ZRX4')
