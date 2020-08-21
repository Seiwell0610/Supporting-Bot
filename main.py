import json
import discord
import asyncio
import traceback
from discord.ext import commands
import os

token = os.environ.get("TOKEN")
prefix = "!"
loop = asyncio.new_event_loop()

async def run():
    bot = MyBot()
    try:
        await bot.start(token)
    except KeyboardInterrupt:
        await bot.logout()


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or(prefix), loop=loop)
        self.remove_command('help')

    async def on_ready(self):
        for extension in ["guild_logs", "help", "admin"]:
            try:
                self.load_extension(f"cogs.{extension}")
            except commands.ExtensionAlreadyLoaded:
                self.reload_extension(f"cogs.{extension}")


    async def on_command_error(self, ctx, error1):
        if isinstance(error1, (commands.CommandNotFound, commands.CommandInvokeError)):
            return

if __name__ == '__main__':
    try:
        print("Logged in as")

        main_task = loop.create_task(run())
        loop.run_until_complete(main_task)
        loop.close()

    except Exception as error:
        print("エラー情報\n" + traceback.format_exc())
