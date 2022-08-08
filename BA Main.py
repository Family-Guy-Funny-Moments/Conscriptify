

import discord
import discord.ext
from discord.ext import commands
from discord.commands import Option



client = commands.Bot(command_prefix = '=')



@client.event 
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="Dieu et mon droit"))

@client.slash_command(description="Information about Conscriptify!")
async def help(ctx):
    info=discord.Embed(
        description="Use ``/conscript`` to conscript recruits!",
        color=discord.Color(0xe91e63)
    )
    await ctx.respond(embed=info)


@client.slash_command(description="Displays bot's response time")
async def ping(ctx):
    ping=discord.Embed(description=f"Pong! {round(client.latency * 1000)}ms",color=discord.Color(0xe91e63))
    await ctx.respond(embed=ping)


@client.slash_command(guild_ids=[641329842058428416],description="Enlists recruit")
@commands.cooldown(1,10,commands.BucketType.user)
async def conscript(ctx,
regiment:Option(str,"Choose a regiment",choices=["19th Green Howards","King's German Legion","50th Queen's Own", "42nd Black Watch","23rd Royal Goats", "Black Brunswickers"]),
recruit:Option(discord.Member,"Recruit Discord username"),
recruiter:Option(discord.Member,"Recruiter Discord username"),
kgloptions:Option(str,"[OPTIONAL](KGL ONLY) Choose the KGL regiment: ",choices=["Thai Regiment","English Regiment"],required=False)
):

    #ROLES
    await ctx.defer()
    oldNick=recruit.display_name

    suc=True
    recruitRole=discord.utils.get(ctx.guild.roles, id=811623854426161184)
    britishArmy = discord.utils.get(ctx.guild.roles, id=863760593785323530)
    permissions=discord.utils.get(ctx.guild.roles,id=829055473008902185)
    classification=discord.utils.get(ctx.guild.roles,id=811627216383115264)
    honors=discord.utils.get(ctx.guild.roles,id=708374869448065155)
    others=discord.utils.get(ctx.guild.roles,id=728759552203554836)
    emoji='<:BA:734311462809632829>'
    """
    DEFAULT ADD ROLES
            await recruit.add_roles(classification)
            await recruit.add_roles(honors)
            await recruit.add_roles(others)
            await recruit.add_roles(permissions)
            await recruit.add_roles(britishArmy)
            await recruit.add_roles(recruitRole)    
    
    """

    #19th Green Howards Custom
    secondBrig=discord.utils.get(ctx.guild.roles, id=938845984274907216)
    nteenStaff = discord.utils.get(ctx.guild.roles, id=885856695853645864)
    

    #King's German Legion Custom
    kglStaff=discord.utils.get(ctx.guild.roles, id=942376143229706281)


    #50th Queen's Own Custom

    fifStaff=discord.utils.get(ctx.guild.roles, id=923213597365137428)
 

    #23rd Royal Goats Custom
 
    twenStaff=discord.utils.get(ctx.guild.roles, id=890575277569216544)



    #Brunswick Custom
    brunStaff=discord.utils.get(ctx.guild.roles, id=971507390027563069)
    firBrig=discord.utils.get(ctx.guild.roles, id=938505035057360966)
    

    #42nd Black Watch Custom
    blacStaff=discord.utils.get(ctx.guild.roles,id=900413632012234843)



    if regiment=='19th Green Howards':
        if nteenStaff in ctx.author.roles:
            nteenRole=discord.utils.get(ctx.guild.roles, id=862704039334641704)
            nteenDepot=discord.utils.get(ctx.guild.roles, id=862787244233588736)
            nteenChannel=client.get_channel(862732931389849640)
            await recruit.edit(nick=f"[19th] {oldNick}")

            await recruit.add_roles(classification)
            await recruit.add_roles(honors)
            await recruit.add_roles(others)
            await recruit.add_roles(permissions)
            await recruit.add_roles(britishArmy)
            await recruit.add_roles(recruitRole)
            await recruit.add_roles(secondBrig)
            await recruit.add_roles(nteenRole)
            await recruit.add_roles(nteenDepot)
        

            nteenMessage = await nteenChannel.send(f"<:19thRegimentofFoot:819130675806470154>***Welcome to the 19th Regiment of Foot (The Green Howard's)***\n{recruit.mention} - {recruiter.mention}\n\n<#924369878452940840> <#862755878699794465> ‣ To view the events this week.\n<#862736054075260948> <#980196271732179004> ‣ To view important shouts.\n<#862737593974915083> ‣ To view promotions and various other shouts.\n<#979721301453320192> ‣ Before battle reminder and rally shout (codes).")
            await nteenMessage.add_reaction(emoji)
            
        else:
            suc=False
            error=discord.Embed(description=f"{ctx.author.mention} has insufficient permissions",color=discord.Color(0xe91e63))
            await ctx.respond(embed=error)

    elif regiment=="King's German Legion":
        if kglStaff in ctx.author.roles:
            

            kglRole=discord.utils.get(ctx.guild.roles, id=808737528638996540)
            

            await recruit.edit(nick=f"[KGL] {oldNick}")
            
            kglRole=discord.utils.get(ctx.guild.roles, id=808737528638996540)
            await recruit.add_roles(classification)
            await recruit.add_roles(honors)
            await recruit.add_roles(others)
            await recruit.add_roles(permissions)    
            await recruit.add_roles(britishArmy)
            await recruit.add_roles(recruitRole)    
            await recruit.add_roles(kglRole)      

            if kgloptions=="Thai Regiment":
                kgl2ndRegiment=discord.utils.get(ctx.guild.roles, id=956890686765019146)
                kgl2ndDepot=discord.utils.get(ctx.guild.roles, id=958585595280633866)
                await recruit.add_roles(kgl2ndDepot)
                await recruit.add_roles(kgl2ndRegiment)
                kglChannel2=client.get_channel(956900139765727343)
                await kglChannel2.send(f"<:KingKGL:763763133357228052> - {recruit.mention}")
            elif kgloptions=="English Regiment":
                kglChannel=client.get_channel(935835116423483402)
                kgl1stRegiment=discord.utils.get(ctx.guild.roles, id=863634856591753227)
                kgl1stDepot=discord.utils.get(ctx.guild.roles,id=867367295813419008)
                await recruit.add_roles(kgl1stDepot)
                await recruit.add_roles(kgl1stRegiment)
                kglMessage= await kglChannel.send(f"<:KingKGL:763763133357228052>***Welcome to the KGL! (King's German Legion)***\n{recruit.mention} - {recruiter.mention}\n\n<#809663928024039425> - Announcements regarding important stuff!\n<#809663973355421696> - A schedule for our events. Updated weekly.\n<#890915390690058241> - Event reminders and rallies will be posted here.\n<#978508287106490418> - General information about our Legion.\n<#867369166671314984> - Game codes for depot will be posted here.")
                await kglMessage.add_reaction(emoji)
            


        else:
            suc=False
            error=discord.Embed(description=f"{ctx.author.mention} has insufficient permissions",color=discord.Color(0xe91e63))
            await ctx.respond(embed=error)



    elif regiment =="50th Queen's Own":
        if fifStaff in ctx.author.roles:
            fifRole=discord.utils.get(ctx.guild.roles, id=922469333983182878)
            fifDepot=discord.utils.get(ctx.guild.roles, id=922475417728843817)
            await recruit.edit(nick=f"[50th] {oldNick}")
            await recruit.add_roles(classification)
            await recruit.add_roles(honors)
            await recruit.add_roles(others)
            await recruit.add_roles(permissions)
            await recruit.add_roles(britishArmy)
            await recruit.add_roles(recruitRole)       
            await recruit.add_roles(secondBrig)    
            await recruit.add_roles(fifDepot)    
            await recruit.add_roles(fifRole)
            fifChannel=client.get_channel(922265637068357632)
            fifMessage = await fifChannel.send(f"<:50thRegimentofFoot:819130742754902036> ***Welcome to the \"Queens Own\" 50th Regiment of Foot! ***\n{recruit.mention} - {recruiter.mention}\n\n<#924369878452940840> <#922263353412419604> ‣ To view our events this week.\n<#922257331176243260> ‣ To view important shouts about battles (codes).\n<#922258595503013938> ‣ To view important announcements.")
            await fifMessage.add_reaction(emoji)


        else:
            suc=False
            error=discord.Embed(description=f"{ctx.author.mention} has insufficient permissions",color=discord.Color(0xe91e63))
            await ctx.respond(embed=error)

    elif regiment=="23rd Royal Goats":
        if twenStaff in ctx.author.roles:
            twenDepot=discord.utils.get(ctx.guild.roles, id=884054182884167720)
            twenChannel=client.get_channel(862961583914483742)
            twenRole=discord.utils.get(ctx.guild.roles, id=862704036348035093)
            await recruit.edit(nick=f"[23rd] {oldNick}")
            await recruit.add_roles(classification)
            await recruit.add_roles(honors)
            await recruit.add_roles(others)
            await recruit.add_roles(permissions)
            await recruit.add_roles(britishArmy)
            await recruit.add_roles(recruitRole)       
            await recruit.add_roles(secondBrig)
            await recruit.add_roles(twenRole)
            await recruit.add_roles(twenDepot)

            twenMessage=await twenChannel.send(f"<:23rd:819130686254219265>***Welcome to the 23rd Regiment of Foot \"The Royal Goats\"!***\n{recruit.mention} - {recruiter.mention}\n\n<#924369878452940840> <#862960347145306112> - To view our events this week\n<#862970805679292436> - To view important shouts about the regiment and battle reminders\n<#862975513505300480> - To access the code and link for attending battles.\n")
            await twenMessage.add_reaction(emoji)
        else:
            suc=False
            error=discord.Embed(description=f"{ctx.author.mention} has insufficient permissions",color=discord.Color(0xe91e63))
            await ctx.respond(embed=error)

    
    elif regiment=="Black Brunswickers":
        if brunStaff in ctx.author.roles:
            brunRole=discord.utils.get(ctx.guild.roles, id=969662215290490940)
            brunInfan=discord.utils.get(ctx.guild.roles, id=878558871839453194)
            await recruit.edit(nick=f"[B.] {oldNick}")
            await recruit.add_roles(classification)
            await recruit.add_roles(honors)
            await recruit.add_roles(others)
            await recruit.add_roles(permissions)
            await recruit.add_roles(britishArmy)
            await recruit.add_roles(recruitRole)    
            await recruit.add_roles(firBrig) 
            await recruit.add_roles(brunInfan) 
            await recruit.add_roles(brunRole)
            brunChannel=client.get_channel(969711430393794631)
            brunMessage= await brunChannel.send(f"<:Brunswick:830583132817850408> ***Welcome to the Black Brunswickers!***\n{recruit.mention} - {recruiter.mention}\n\n<#924369763138953276> <#969711015531016212> - To view our events this week.\n<#969711154576388206> - To view important regimental announcements.\n<#997471466394243103> - To access battle links and codes.") 
            await brunMessage.add_reaction(emoji)

        else:
            suc=False
            error=discord.Embed(description=f"{ctx.author.mention} has insufficient permissions",color=discord.Color(0xe91e63))
            await ctx.respond(embed=error)


    elif regiment=="42nd Black Watch":
        if blacStaff in ctx.author.roles:
            await recruit.edit(nick=f"[42nd] {oldNick}")
            await recruit.add_roles(classification)
            await recruit.add_roles(honors)
            await recruit.add_roles(others)
            await recruit.add_roles(permissions)
            await recruit.add_roles(britishArmy)
            await recruit.add_roles(recruitRole)    
            await recruit.add_roles(firBrig)  
            blacDepot=discord.utils.get(ctx.guild.roles,id=862919560243838987)
            blacRole=discord.utils.get(ctx.guild.roles,id=862704025576013904)
            blacChannel=client.get_channel(862773879261102090)         
            await recruit.add_roles(blacDepot)           
            await recruit.add_roles(blacRole)

            blacMessage=await blacChannel.send(f"<:42ndRegimentofFoot:819130726435389461> <:BA:734311462809632829> ***Welcome to the 42nd Regiment of Foot! (Royal Highlanders)***<:BA:734311462809632829><:42ndRegimentofFoot:819130726435389461>\n{recruit.mention} - {recruiter.mention}\n\n<#862771755633344543> - To view the events this week.\n<#915014222801432586> - To view important shouts!\n<#922557721604132874> - To view promotions and various other shouts.\n<#969961528260440085> - Before Battle Reminder & Rally shout!\n")
            await blacMessage.add_reaction(emoji)

        else:
            suc=False
            error=discord.Embed(description=f"{ctx.author.mention} has insufficient permissions",color=discord.Color(0xe91e63))
            await ctx.respond(embed=error)           




    conscriptSuccess=discord.Embed(description=f"{recruit.mention} has successfully enlisted in the {regiment}\nGreat job {recruiter.mention}!",color=discord.Color.green())
    if suc==True:
      await ctx.respond(embed=conscriptSuccess)

@client.slash_command(guild_ids=[877304415319638057])
@commands.cooldown(1,10,commands.BucketType.user)
async def conscript(ctx, recruit:Option(discord.Member,"Recruit Discord username"),
recruiter:Option(discord.Member,"Recruiter Discord username"),timezone:Option(str,"Recruit's timezone")):
    #ROLES
    await ctx.defer()
    oldNick=recruit.display_name


    recruitRole1=discord.utils.get(ctx.guild.roles, id=901626116299702302)
    britishArmy1 = discord.utils.get(ctx.guild.roles, id=951934865018847282)
    permissions1=discord.utils.get(ctx.guild.roles,id=986013384694702200)

    await recruit.add_roles(recruitRole1)
    await recruit.add_roles(permissions1)
    await recruit.add_roles(britishArmy1)
    await recruit.edit(nick=f"[CSG] {oldNick}")

    welcome=client.get_channel(934009607846756382)

    message1=await welcome.send(f"{recruit.mention} ({timezone}) - {recruiter.mention}")
    await message1.add_reaction('✅')
    hi=discord.Embed(description=f"{recruit.mention} has been successfully enlisted", color=discord.Color.green())
    await ctx.respond(embed=hi)


@client.event
async def on_application_command_error(ctx,error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.respond(error)
  else:
    raise error


    
        
client.run('OTgyNzI4NDE3ODEwMTk4NTg5.GleB_F.ZAoVgAaNKxD7wxg13JBCR1nZNl-acxcxs9QEVY')
