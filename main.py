#KMCODES SYSTEM ----------- DEV:MUHAMMAD KR
#GITHUB : KINGMAN1996
import discord
from discord.ext import commands
from discord import File
from discord import Embed
from dotenv import load_dotenv
import os
load_dotenv()
prefix = "."
km = commands.Bot(command_prefix=prefix , case_insensitive=True , owner_id=1)
TOKEN = os.getenv('TOKEN')
ssupport_role = os.getenv('SUPPORT_ROLE')
smember_role_id = os.getenv('MEMBER_ROLE')
sadmine_role = os.getenv('ADMINE_ROLE')
sbanlogchannel = os.getenv('BAN_LOG')
sblacklistmanager = os.getenv('BLACK_LIST_MANAGER')
sblack_list_role = os.getenv('BLACK_LIST_ROLE')
sblackllog = os.getenv('BLACK_LIST_LOG')
skikelogchannel = os.getenv('KICK_LOG')
smute = os.getenv('MUTE_ROLE')
srolelogchannel = os.getenv('ADD_REMOVE_ROLES_LOG')
swarnlogchannelid = os.getenv('WARN_LOG')
smutelog = os.getenv('MUTELOG')
#########
mutelog = int(smutelog)
support_role = int(ssupport_role)
member_role_id = int(smember_role_id)
admine_role = int(sadmine_role)
banlogchannel = int(sbanlogchannel)
blacklistmanager = int(sblacklistmanager)
black_list_role = int(sblack_list_role)
blackllog = int(sblackllog)
kikelogchannel = int(skikelogchannel)
mute = int(smute)
rolelogchannel = int(srolelogchannel)
warnlogchannelid = int(swarnlogchannelid)
km.remove_command('help')
game = "BOT STATUS"

kmbanner = """
KMCODES 
"""
@km.event
async def on_ready():
    await km.change_presence(activity=discord.Streaming(name=f"{game}", url = "https://www.twitch.tv/kingman4hack"))
    print("KM SYSTEM log in as ")
    print(km.user.name)
    print(km.user.id)
    print(discord.__version__)
    print("---------")
    print(kmbanner)
    print("Server Connect to")
    for guild in km.guilds:
        print(guild.name)
        print(guild.id)
        print("----------")


@km.command()
async def help(ctx):
    embed=discord.Embed(title="HELP", url="https://github.com/KINGMAN1996", description=f"<@&{admine_role}>\n `{prefix}ban` : ban members \n `{prefix}kick` : kick members \n `{prefix}addrole` : addrole to members \n `{prefix}removerole ` : remove role from members\n  <@&{support_role}> \n `{prefix}active` : active members\n`{prefix}unactive` : unactive members\n`{prefix}clear `: clear chat\n`{prefix}lock` : lock channels\n`{prefix}unlock `: unlock channels\n`{prefix}mute` : mute members\n`{prefix}setnick` : setnick name\n`{prefix}warn` : warn members \n\n <@&{blacklistmanager}>\n `{prefix}blacklist` \n {prefix}unblacklist", color=0x237bf5)
    embed.set_author(name="</> KM SYSTEM", url="https://github.com/KINGMAN1996")
    embed.set_footer(text="</> Power By KMCodes")
    await ctx.send(embed=embed)


km.load_extension("kmmoderation.active")
km.load_extension("kmmoderation.ban")
km.load_extension("kmmoderation.blacklist")
km.load_extension("kmmoderation.clear")
km.load_extension("kmmoderation.kick")
km.load_extension("kmmoderation.lock")
km.load_extension("kmmoderation.mute")
km.load_extension("kmmoderation.role")
km.load_extension("kmmoderation.setnick")
km.load_extension("kmmoderation.warn")
km.load_extension("kmmoderation.error")


km.run(TOKEN)
