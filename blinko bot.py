# imports the libs
import os
import random
from dotenv import load_dotenv
import time

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')


# Lets you know that the bot has connected
@bot.event
async def on_ready():
    print(f' {bot.user.name}  has connected to Discord!')


# doesn't work currently, but would say "touch grass", or "go touch grass".
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    grass = [
        'go touch grass',
        'touch grass',
    ]
    if message.content == 'grass':
        if random.randint(1, 10) == 1:
            response = random.choice(grass)
            await message.channel.send(response)


# Says deez nutz or suggon deez nutz when deez is said (yes i know its childish)
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    deez = [
        'sugon deez nutz',
        'deez nutz',
    ]
    if 'deez' in message.content.lower:
        if random.randint(1, 10) == 4:
            response = random.choice(deez)
            await message.channel.send(response)


# Says cringe and libplilled or cringe and bluepilled when cringe is mentioned.
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    cringe = [
        'cringe and libpilled',
        'cringe and bluepilled',
    ]
    if 'cringe' in message.content.lower():
        if random.randint(1, 10) == 4:
            response = random.choice(cringe)
            await message.reply(response)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    based = [
        'based and redpilled ',
        'OMG SO BASED '
    ]
    if 'based' in message.content.lower():
        if random.randint(1, 10) == 7:
            response = random.choice(based)
            await message.reply(response)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if '<meme firend>' in message.content.lower():
        if random.randint(1, 200) == 69:
            response = '<image meme>'
            await message.reply(response)



bot.run(TOKEN)
