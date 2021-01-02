# Discord Bot
This was inspired by me for having a knack for trying to combine things that I do together. Luckily, Discord a popular platform has a developer side which allows others to create useful bots to make our lives easier.

The commands that I've chosen to add was inspired by the idea that I would use them most often. 

## Installation 

```
# Linux/MacOS
git clone https://github.com/KevinLu19/Discord_Bot.git

# Windows
# It is recommened to install Git but following command works on command prompt as well

On Command Prompt: 
git clone https://github.com/KevinLu19/Discord_Bot.git
```

# Usages
Assuming you've created a discord bot from their website (Discord developer portal) and have Python 3.5 or above installed.

Take the created discord token and add that onto following file path directory

```
src/discord/bot.py
```

Add your discord token onto line 16.

## To Run The Bot

Currently the only way to run the bot is to execute 

```
# change directory onto src/discord/
python bot.py
```


## Example

Let's say you want to use the command YouTube to pull your searched video onto Discord. The first thing you would do is type in your command starter (in my case, mine is set to '->>' you're free to change it on line 17)

```
->>youtube <vido name here>
```

You will get your searched video pasted onto Discord via your bot. 


## Currently Supported Commands 
* YouTube
* Restart / Shutdown
* Anime / Manga search
* Storing twitter username handlers 

## Technology Used
This project also uses sqlite3 which creates a local database onto the project directory. This allows cretain commands to be "saved" such as the twitter usernames command.

* [Python 3.8](https://www.python.org/)
* [sqlite3](https://docs.python.org/3/library/sqlite3.html)
* [Selenium](https://selenium-python.readthedocs.io/)

## Credits 
Special thanks to these people

* darenliang [Manga and Anime Search Module](https://github.com/darenliang/mal-api) 
* Rapptz [Python Discord Module](https://github.com/Rapptz/discord.py)


