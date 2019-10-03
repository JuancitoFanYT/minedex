import discord
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
TOKEN = 'NjI4MDMxODg4NDA5NDkzNTE1.XZKfVQ.pdP6rJEG_qfDjd0_pl_xU4jgrDc'
bot_prefix= "!!"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    activity = discord.Game(name="www.minedex.us")
    await client.change_presence(status=discord.Status.online, activity=activity)
    client.remove_command('help')
    print('Helouda')

@client.command()
async def test(ctx):
    await ctx.send('1 2 3 Probando')

@client.command()
async def twitter(ctx):
    await ctx.send('https://twitter.com/minedexnt')

@client.command()
async def shop(ctx):
    await ctx.send('http://minedexshop.buycraft.net/')

@client.command()
async def web(ctx):
    await ctx.send('http://minedex.us/')

@client.command()
async def invite(ctx):
    await ctx.send('https://invite.gg/MinedexNT')


@client.command()
async def say(ctx):
        channel = ctx.message.channel
        args = ctx.message.content.split(" ")
        await channel.send("%s" % (" ".join(args[1:])), tts=False)



@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("*Por favor especifique el miembro*")
        return
    await member.kick()
    await ctx.send(f"**{member.mention} ha sido kickeado**")


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("*Por favor especifique el miembro*")
        return
    await member.ban()
    await ctx.send(f"**{member.mention} ha sido baneado**")

@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("*Por favor especifique el miembro*")
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.add_roles(role)
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("No se te permite mutear a la gente.")


@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("*Por favor especifique el miembro*")
        return
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)
@mute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("No se te permite el unmute a la gente.")

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f' Ha sido unbaneado {user.mention}')

@client.command()
@commands.has_permissions(manage_guild=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"**{amount} mensajes eliminados**")

@client.command()
async def ip(ctx):
    embed=discord.Embed(title="Minedex Bot - Prefix = !! - Ayuda y Confort", color=0xff0000)
    embed.add_field(name="➡️ | Dirección IP: Minedex.us", value=":pushpin: | Recuerda que puedes invitar a tus amigos a MineDex Network, donde la pasarás de lo mejor con Nosotros !", inline=False)

    await ctx.send(embed=embed)


@client.command()
async def ayuda(ctx):
    embed=discord.Embed(title="Minedex Bot - Prefix = !! - Ayuda y Confort", description="**Se esta mejorando todo**", color=0xff8000)
    embed.add_field(name="!!ayuda", value="Muestra este mensajes", inline=False)
    embed.add_field(name="!!ip", value="Muestra la direccion de ip", inline=False)
    embed.add_field(name="!!invite", value="Invitacion del server", inline=False)
    embed.add_field(name="!!twitter", value="Mustra pagina de twitter (mejorando)", inline=False)
    embed.add_field(name="!!shop", value="Muestra la tienda esta en mejora", inline=False)
    embed.add_field(name="!!web", value="Te muestra la pagina web", inline=False)
    embed.add_field(name="!!test", value="Muestra si el bot esta en funcionamiento, o no", inline=False)
    embed.add_field(name="!!say", value="Repite un mensaje", inline=False)
    embed.add_field(name="--- **STAFF** ---", value="Dedicacion y Compromiso", inline=False)
    embed.add_field(name="!!kick", value="Kickea a usuarios que incumplan las reglas", inline=False)
    embed.add_field(name="!!ban", value="Banea a usuarios de forma permanente", inline=False)
    embed.add_field(name="!!unban", value="Unbanea o quita ban a alguien", inline=False)
    embed.add_field(name="!!mute", value="Mutea o silencia al jugador de forma permamente", inline=False)
    embed.add_field(name="!!unmute", value="Unmutea o saca el muteo a alguien", inline=False)

    await ctx.send(embed=embed)

client.run(os.environ['DISCORD_TOKEN'])
