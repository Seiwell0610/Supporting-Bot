import discord
from discord.ext import commands

print("guild_logsの読み込み完了")

class log(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == 740787731130482778:

            channel = self.bot.get_channel(741125440126844939)

            embed = discord.Embed(title="メンバー参加", color=discord.Color.blue())
            embed.add_field(name=f"ユーザー名", value=f"`{member}`", inline=True)
            embed.add_field(name='\u200b', value='\u200b')
            embed.add_field(name="ユーザーID", value=f"`{member.id}`", inline=True)
            await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if member.guild.id == 740787731130482778:
            channel = self.bot.get_channel(741125440126844939)

            embed = discord.Embed(title="メンバー脱退", color=discord.Color.purple())
            embed.add_field(name=f"ユーザー名", value=f"`{member}`", inline=True)
            embed.add_field(name='\u200b', value='\u200b')
            embed.add_field(name="ユーザーID", value=f"`{member.id}`", inline=True)
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(log(bot))