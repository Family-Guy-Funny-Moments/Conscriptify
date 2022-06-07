
import discord
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix = '~')

#DO STUFF


@client.event 
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def k(ctx,user: discord.Member):
    nine=discord.utils.get(ctx.guild.roles, id=697403374328348733)
    Conscrit=discord.utils.get(ctx.guild.roles, id=952000109808328724)
    Deux=discord.utils.get(ctx.guild.roles, id=694278538504962099)
    grandArmee=discord.utils.get(ctx.guild.roles, id=697416262149472256)
    Chasseur=discord.utils.get(ctx.guild.roles, id=847921990375309322)
    Guest=discord.utils.get(ctx.guild.roles, id=697418185045049385)

    modRole = discord.utils.get(ctx.guild.roles, id=697405861726912533)

    if modRole in ctx.author.roles:
        await user.add_roles(nine)
        await user.add_roles(Conscrit)
        await user.add_roles(Deux)
        await user.add_roles(grandArmee)
        await user.add_roles(Chasseur)
        await user.remove_roles(Guest)
        await ctx.send(f"Done <@171850083195813889>")
    
        


#OTgyNzI4NDE3ODEwMTk4NTg5.G97G1x.JZuuM1-b5AlwQHCkUwk-u-LrC20hUoZLIGCooE
client.run('OTgzNjIwMTUwNTY3NzY4MDk0.GVLbwT.19DQYWb5wju4ICunv-PZvbjhXSRRNYLVlGz4U4',bot=False)