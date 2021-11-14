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
            await message.reply(response)


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

    if 'masher' in message.content.lower():
        if random.randint(1, 200) == 69:
            response = 'https://imgur.com/a/eFCwJHz'
            await message.reply(response)

# Replies to  the user a random gif of a dog
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    dog = [
        'https://media4.giphy.com/media/bbshzgyFQDqPHXBo4c/giphy.gif?cid=ecf05e47e6xx23euvpu2pgj9c3z4agtrzq79av7b37wy1u5s&rid=giphy.gif&ct=g',
        'https://media2.giphy.com/media/QvBoMEcQ7DQXK/giphy.gif?cid=ecf05e47e6xx23euvpu2pgj9c3z4agtrzq79av7b37wy1u5s&rid=giphy.gif&ct=g',
        'https://media3.giphy.com/media/ZNegC7wFpuQT7nurZ0/giphy.gif?cid=ecf05e47kqer71ul4d844nzhw6ls5n2lz5tllzj5rup9vnfv&rid=giphy.gif&ct=g'
    ]
    if '$dog' in message.content:
        reponse = random.choice(dog)
        await message.reply(reponse)
# Replies to the user with a gid of a cat
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    cat = [
        'https://media4.giphy.com/media/ICOgUNjpvO0PC/giphy.gif?cid=ecf05e47vxv6up870cgvbl5li8otal8r2kxkvzl36nriv8ia&rid=giphy.gif&ct=g',
        'https://giphy.com/gifs/emote-catjam-jpbnoe3UIa8TU8LM13',
        'https://media2.giphy.com/media/C9x8gX02SnMIoAClXa/giphy.gif?cid=ecf05e47vxv6up870cgvbl5li8otal8r2kxkvzl36nriv8ia&rid=giphy.gif&ct=g',
        'https://media0.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif?cid=ecf05e47vok1o5sew9rdu3y6z4axuzqbh6xr4qzyvp595ax5&rid=giphy.gif&ct=g'

    ]
    if '$cat' in message.content:
        response = random.choice(cat)
        await message.reply(response)

# Responds to a user if they say $birb or $bird with a random bird gif.
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    birb = [
        'https://media3.giphy.com/media/bUPXILnUYeSHK/giphy.gif?cid=ecf05e479e0vshxfo3weq2m66u329hk6a325gczjp4w4cqa8&rid=giphy.gif&ct=g',
        'https://media4.giphy.com/media/VF62B6qsDBNMwY0z1c/giphy.gif?cid=ecf05e479e0vshxfo3weq2m66u329hk6a325gczjp4w4cqa8&rid=giphy.gif&ct=g',
        'https://media3.giphy.com/media/dUrYGygfOa1gCIdwFV/giphy.gif?cid=ecf05e4706hw1k7k0icx8963r9i1poz7hvdr215vzoqefiw0&rid=giphy.gif&ct=g',
        'https://media3.giphy.com/media/FO4lgeCgKkC2I/giphy.gif?cid=ecf05e47l2q575pc8jlr1yx09s2vaofux38ow1dm08cwa7yr&rid=giphy.gif&ct=g'
    ]
    if '$bird' in message.content:
        reponse = random.choice(birb)
        await message.reply(reponse)
    elif '$birb' in message.content:
        reponse = random.choice(birb)
        await message.reply(reponse)

bot.run(TOKEN)
