import discord
import fasmga
import os
import re
from discord.ext import commands

url_regex = (
    "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
)

# you need to enable all the intents from the discord developer portal
intents = discord.Intents.all()


class MyBot(commands.Bot):
    """This is an example bot."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fasmga = fasmga.Client(
            os.getenv("FGA_TOKEN"), loop=self.loop, discord=True
        )

    def run(self, *args, **kwargs):
        self.loop.run_until_complete(self.fasmga.connect())
        return super().run(*args, **kwargs)

    async def close(self, *args, **kwargs):
        await self.fasmga.close()
        return await super().close(*args, **kwargs)


bot = MyBot(
    command_prefix="&",
    description="This is an example bot with the Fasm.ga API wrapper (fasmga.py)",
)


@bot.command()
async def shorten(ctx, url):
    is_url_re = bool(re.findall(url_regex, url))
    is_url_sm = url.startswith("http://") or url.startswith("https://")
    is_url = is_url_re and is_url_sm
    if not is_url:
        await ctx.send("The url argument must be an URL.")
        return

    shortened = await bot.fasmga.shorten(url)
    await ctx.send(f"Your shortened URL is: {shortened}")


bot.run(os.getenv("DISCORD_TOKEN"))
