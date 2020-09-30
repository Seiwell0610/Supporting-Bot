import discord
from discord.ext import commands

print("guild_logsの読み込み完了")

class school(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def owner(self, ctx):
        if ctx.anthor.guild.id == 732573466439450704:
            if ctx.anthor.id == 343956207754805251:
                role = ctx.guild.get_role(732739886150451260)
                if role in ctx.author.roles:
                    await ctx.author.remove_roles(role)
                    await ctx.send(f"{ctx.author.mention}-> `{role}`を剥奪しました。")

                else:
                    await ctx.author.add_roles(role)
                    await ctx.send(f"{ctx.author.mention}-> `{role}`を付与しました。")
            else:ßßß
                await ctx.send(f"{ctx.author.mention}-> あなたには、このコマンドを使用する権限がありません。")

def setup(bot):
    bot.add_cog(school(bot))