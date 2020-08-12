import discord
from discord.ext import commands
from datetime import datetime
import libneko

print("helpの読み込み完了")


def default_buttons():
    from libneko.pag.reactionbuttons import (
        first_page,
        back_10_pages,
        previous_page,
        next_page,
        forward_10_pages,
        last_page
    )

    return (
        first_page(),
        back_10_pages(),
        previous_page(),
        next_page(),
        forward_10_pages(),
        last_page()
    )
buttons = default_buttons()

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        timestamp = datetime.utcfromtimestamp(int(self.bot.user.created_at.timestamp()))
        pages = [(discord.Embed(title="このBOTのヘルプ:", description=f">>> ```ここのサーバーの専属BOT。\n必要に応じて、機能を追加します。```", timestamp=timestamp, color=0x009193)),
                 (discord.Embed(title="基本コマンド", color=discord.Color.blue())),
                 (discord.Embed(title="オート機能", color=discord.Color.blue()))
                 ]

        pages[0].set_thumbnail(url=self.bot.user.avatar_url)
        pages[0].add_field(name="導入サーバー数", value=f"`{len(self.bot.guilds)}`")
        pages[0].add_field(name='\u200b', value='\u200b')
        pages[0].add_field(name="総ユーザー数", value=f"`{len(set(self.bot.get_all_members()))}`")
        pages[0].add_field(name="開発言語", value="`discord.py`")
        pages[0].add_field(name='\u200b', value='\u200b')
        pages[0].add_field(name="応答速度", value=f'`{self.bot.ws.latency * 1000:.0f}ms`')
        pages[0].set_footer(text="このBOTの作成日")

        pages[1].add_field(name=";help", value="ヘルプを表示します。")

        pages[2].add_field(name="メンバーの参加・脱退通知", value="メンバーが参加・脱退した際に、welcomeに通知を送るだけです。")

        nav = libneko.pag.navigator.EmbedNavigator(ctx, pages, buttons=default_buttons(), timeout=20)
        nav.start()
        await ctx.send(nav)

def setup(bot):
    bot.add_cog(Help(bot))
