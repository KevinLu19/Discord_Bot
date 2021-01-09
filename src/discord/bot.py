from discord.ext.commands.core import command
from discord.ext import commands
# from . import mal_anime
# from . import mal_manga

import discord
import os
import platform
import subprocess
import src.maplestory.maple as maple
import src.youtube.youtube as yt
import src.twitterFetcher.main as twitter_sniffer
import src.discord.mal_anime as mal_anime
import src.discord.mal_manga as mal_manga
import src.twitter_user_storage.user_storage as user_storage
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

@bot_command.command(name="twitter_add", help = "Stores the usernames for Twitter")
async def add_twitter_username(ctx, twitter_usernames):
    if len(twitter_usernames) > 0:
        result = user_storage.insert(twitter_usernames)
        await ctx.send(result)
    else:
        await ctx.send("Twitter Username cannot be 0.")

@bot_command.command(name = "list", help = "Returns all of the stored usernames from database")
async def print_twitter_usernames(ctx):
    results = user_storage.print_all_entries()

    # Converted tuple into a list.
    twitter_usernames_list = list(results)

    # Using List Comprehension to remove tuple from list.
    # We loop through twice to first get rid of the list and the second loop to go into the tuple.
    twitter_list_output = [twitter_names for item in twitter_usernames_list for twitter_names in item]

    await ctx.send(twitter_list_output)

@bot_command.command(name = "twitter_update", help = "Updates an entry in database. Format <old> <new>")
@commands.is_owner()
async def update_twitter_name(ctx, old_username, new_username):
    if len(old_username) and len(new_username) > 0:
        result = user_storage.update_entry_from_table(old_username, new_username)

        await ctx.send(result)
    else:
        await ctx.send("Old username or new username cannot be empty.")

@bot_command.command(name = "twitter_remove", help = "Removes desired username from database.")
@commands.is_owner()
async def remove_twitter_username(ctx, twitter_name):
    if len(twitter_name) > 0:
        result = user_storage.delete_entry_from_table(twitter_name)

        await ctx.send(result)
    else:
        await ctx.send("Twitter name cannot be empty.")

@bot_command.command(name = "twitter_clear", help = "Permanently removes everything from database! Proceed with caution")
@commands.is_owner()
async def clear_twitter_database(ctx):
    user_storage.clear_database()
    await ctx.send("**I've erased everything from database. If that was a mistake, then looks like you have to repopulate the table -Get fucked KEKW-.**")

@bot_command.command(name="twitter", help = "Retrevie latest tweet from set user")
async def twitter(ctx, twitter_user):
    # twitter_sniffer

    # await ctx.send()
    pass