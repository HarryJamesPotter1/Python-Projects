import discord
from bot import PollBot
import sys
import json

with open('config.json') as config_file:
    config = json.load(config_file)

bot = PollBot(config)
bot.run()