from src.twitterFetcher import main as tweet_fetcher
from src.discord import bot

import os
import time
import tweepy


# list_of_twitter_users = ["Nemesis_3d", "Noahgraphicz", "BulgingS", "strauzek", "Pantsushi3D", "RealAudiodude", "GrandCupido", "Auxtasy", "lexfox10", "hv54rdsl", "Redmoaa", "Spizzy3D", "DisckoA", "Overwatch_Haven", "shir0qq", "velocihaxor", "ForceballFx", "ExgaTWT", "cawneil", "Xordel3d", "texelnaut", "BewyxAnims", "Lvl3toaster_", "darkholestuff", "idemiliam", "arhoangel", "RedDoeArt", "Yeero3D", "HydraFXX", "B1yck", "VG_Worklog", "mavixtious", "Yokubos1", "xJunkerz", "juicyneko1", "Jul3D_NSFW", "audionoob", "Sakimianimation"]

if __name__ == "__main__":
    discord_bot_token = os.environ.get("YUNA_DISCORD_SECRET")
    bot.bot_command.run(discord_bot_token)

    auth = tweet_fetcher.TwitterAuthenicate()
    authenticate = auth.authenticate_user()
    twitter_stream_listener = tweet_fetcher.TweetListener()
    streamming = tweepy.Stream(authenticate, twitter_stream_listener)
    print ("Initializing tweet fetcher")
    streamming.filter(track=["ForceballFx"])
