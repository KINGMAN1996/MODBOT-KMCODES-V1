from main import *
import discord
from discord.ext import commands
from discord import File
from discord import Embed
from dotenv import load_dotenv
 
############
############
class active(commands.Cog):
    def __int__(self, bot):
        self.bot = bot
    @commands.command(aliase=['ميوت'])
    @commands.has_role(support_role)
    async def mute(self, ctx, member: discord.Member):
        muters = ctx.guild.get_role(mute)
        if muters in member.roles:
            await ctx.send("This User already muted")

        else:
            await member.add_roles(muters)
            await ctx.send(f"**{member.mention} has been muted**")
    @commands.command(aliase=['فك الميوت'])
    @commands.has_role(support_role)
    async def unmute(self, ctx, member: discord.Member):
        muters = ctx.guild.get_role(mute)
        if muters in member.roles:
            await member.remove_roles(muters)
            await ctx.send("f**{member.mention} has been unmuted**")
        else:
            await ctx.send("This User already un active")

def setup(bot):
    bot.add_cog(active(bot))
