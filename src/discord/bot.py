from discord.ext.commands.core import command
from discord.ext import commands
from . import mal_anime
from . import mal_manga

import discord
import tweepy
import os
import platform
import subprocess
import src.maplestory.maple as maple
import src.youtube.youtube as yt
import src.twitterFetcher.main as twitter_sniffer
import asyncio

discord_bot_token = os.environ.get ("YUNA_DISCORD_SECRET")
bot_command = commands.Bot (command_prefix="->>")

@bot_command.event
async def on_ready ():
    print ("Logging in as ", bot_command.user.name)
    print ("id is ", bot_command.user.id)
    print ("--------")

@bot_command.command (name = "restart", alias = ["r"], help = "Restarts the bot. Only the owner can do this.")
@commands.is_owner()
async def restart (ctx):
    await ctx.send ("Restarting my internal brain chemistry...")

    current_os_platform = platform.system()

    if current_os_platform == "Windows":
        print ("Current directory is: ", str(os.getcwd()))
        subprocess.run(["Start.bat"], shell = True)
    else:
        subprocess.run(["Start.sh"])

@bot_command.command (name = "shutdown", help = "Shuts down bot. Only the owner can do this.")
@commands.is_owner()
async def shutdown (ctx):
    await ctx.send ("I'm going to take a nap now.")
    await bot_command.logout()

@bot_command.command (name = "anime", help = "Search the given anime on MyAnimeList")
async def anime (ctx, anime_name):
    anime_query = mal_anime.AnimeQuery (anime_name)

    await ctx.send (f"**The anime you're looking for is: {anime_query.search_anime_title()} **")
    await ctx.send (anime_query.search_anime_url())
    await ctx.send (f"**Anime score is:  {anime_query.search_anime_score ()} **")

@bot_command.command (name = "manga", help = "Searches the given manga on MyAnimeList")
async def manga (ctx, manga_name):
    manga_query = mal_manga.MangaQuery (manga_name)

    await ctx.send (f"**The manga you're looking for is: {manga_query.search_manga_title()} **")
    await ctx.send (manga_query.serach_manga_url())
    await ctx.send (f"**Manga score is: {manga_query.search_manga_score()} **")

@bot_command.command(name = "maple", help = "Returns the update from Maplestory.", alias = ["maplestory"])
async def maplestory(ctx):
    maple_news = maple.get_latest_maple_news()

    await ctx.send(f"**Here's the update from Maplestory.** {maple_news}")

@bot_command.command(name="youtube", alias = ["yt"], help = "Returns the video requested.")
async def youtube(ctx, *,video_title):
    discord_id = os.environ.get("MY_DISCORD_ID")

    try:
        entire_message = "".join(video_title)
        youtube_video = yt.get_requested_video(entire_message)

        await ctx.send(youtube_video)
        await asyncio.sleep(10)
    except Exception as e:
        print (e)

        await ctx.send(f"<@!{discord_id}> Uh-oh some moron tried to break the command. SMH")

@bot_command.command(name="twitter", help = "Retrevie latest tweet from set user")
async def twitter(ctx, twitter_user):
    # twitter_sniffer

    await ctx.send()