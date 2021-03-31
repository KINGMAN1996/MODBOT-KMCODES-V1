from main import *
import discord
from discord.ext import commands
from discord import File
from discord import Embed
from dotenv import load_dotenv

class kick(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command(aliases=['انقلع برى'])
  @commands.has_any_role(admine_role)
  async def kick(self, ctx, member : discord.Member = None, *, reason=None):
    if member == None:
      await ctx.send("حدد شخص عشان اطرده")
    if reason == None:
      reason = "بدون سبب"
    if black_list_role in [role.id for role in ctx.author.roles] or ctx.author.top_role <= member.top_role:
      await ctx.send("متقدر تطرد شخص رتبتة اكبر منك او انت معك بلاكليست")
    else:
      kicklog = self.bot.get_channel(kikelogchannel)

      embed=discord.Embed(title="KICK LOG", url="https://github.com/KINGMAN1996", description="تم طرد شخص من السيرفر", color=0x0467da)
      embed.set_author(name="</>KMCodes", url="https://github.com/KINGMAN1996")
      embed.add_field(name="اسم الاداري", value=f"{ctx.author.mention}", inline=True)
      embed.add_field(name="اي دي الاداري", value=f"{ctx.author.id}", inline=True)
      embed.add_field(name="اسم العضو", value=f"{member.mention}", inline=True)
      embed.add_field(name="اي دي العضو", value=f"{member.id}", inline=True)
      embed.add_field(name="السبب", value=f"{reason}", inline=True)
      embed.set_footer(text="</>KMCodes KINGMAN")
      await ctx.send(f"تم طرد {member.mention}")

      await member.kick(reason=reason)
      await kicklog.send(embed=embed)











def setup(bot):
  bot.add_cog(kick(bot))