import disnake
import os
import json

from disnake.ext import commands

bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all(), test_guilds=[1099389415169720431])
channelToAnswer = bot.get_channel(1099389415677247551)

def addLog(message):
    with open('data.json') as f:
        output_data = json.load(f)
        print(output_data)
        output_data['output'] = output_data["output"], message
        with open('data.json', 'w') as f:
            json.dump(output_data, f)


@bot.event 
async def on_ready():
    print(f"Bot {bot.user} is online!")
    addLog("testing message")

    await bot.change_presence(status=disnake.Status.online, activity=disnake.Game("Defeat Some Rake!!211!"))

@bot.event
async def on_member_join(member: disnake.Member):
    role = disnake.utils.get(member.guild.roles, id=1100105165756973057)
    channel = bot.get_channel(1099389415677247551) #member.guild.system_channel

    embed = disnake.Embed(
        title=f"hello noob {member.mention}",
        description="this is a test ##############, so you are amogus",
    )
    
    await member.add_roles(role)
    await channel.send(f"welcome {member.name}, could you say: вау")

    await channel.send(embed=embed)

@bot.event
async def on_message(message):
    await bot.process_commands(message=message)

    for msg in message.content.split():
        if msg.lower() == "вау":
            await message.channel.send(f"даа согласен с тобой {message.author.mention}"),
        elif msg.lower() == "нахуй":
            await message.channel.send(f"{message.author.mention} сама")


@bot.event
async def on_command_error(ctx, error):
    print(error)

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author}, You do not have permission to do this command")        


@bot.event
async def on_member_leave(member):
    channelToAnswer.send(f"{member.name} покинул  этот сервак")


# COMMANDS


@bot.slash_command(name="clear", description="Очистить чат от сообщений, по умолчанию 10 сообщений")
async def clear(ctx, amount: int=10):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Was deleted {amount} messages...")


@bot.slash_command(name="kick", description="кикнуть кого-нибудь")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: disnake.Member, *, reason=None, delete_message: bool=False):
    message = f"Succefuly kicked Member {member.mention}. Reason: {reason}"
    if delete_message==True:
        await ctx.send(message, delete_after=10)
    elif delete_message==False:
        await ctx.send(message)
    await member.kick(reason=reason)


@bot.slash_command(name="mute", description="замьютить кого-нибудь")
@commands.has_permissions(mute_members=True)
async def mute(ctx, member: disnake.Member, *, reason=None, delete_message: bool=False):
    message = f"Succefuly muted Member {member.mention}. Reason: {reason}"
    if delete_message==True:
        await ctx.send(message, delete_after=10)
    elif delete_message==False:
        await ctx.send(message)
    role = disnake.utils.get(member.guild.roles, id=1136982828731617395)  
    await member.add_roles(role)


@bot.slash_command(name="unmute", description="размьютить кого-нибудь")
@commands.has_permissions(mute_members=True)
async def unmute(ctx, member: disnake.Member, delete_message: bool=False):
    message = f"Succefuly unmuted Member {member.mention}"
    if delete_message==True:
        await ctx.send(message, delete_after=10)
    elif delete_message==False:
        await ctx.send(message)
    role = disnake.utils.get(member.guild.roles, id=1136982828731617395)  
    await member.remove_roles(role)


@bot.slash_command(name="math", description="считать не умеешь?")
async def math(inter, number_1: int, operation: str="+", number_2: int=None):
    if operation == "+":
        result = number_1 + number_2,
    elif operation == "-":
        result = number_1 + number_2,
    await inter.send(str(result))


# LOGIN

bot.login(os.environ.get("TOKEN"))

#bot.run(dotenv.get_key(dotenv_path=".env", key_to_get="TOKEN", encoding=None))