import discord
from discord.ext.commands import Bot
from discord.ext import commands, tasks
from discord import Game
from ctypes.util import find_library
import random
from discord import opus
import asyncio
from discord import Game
from discord.ext.commands import Bot
import os
from random import randint 
import wikipedia
import youtube_dl,string
from discord.utils import get
from discord.voice_client import VoiceClient
from os import system
from googleapiclient.discovery import build
import googletrans
from googletrans import Translator
from dotenv import load_dotenv

load_dotenv()




def get_prefix(bot, msg):
    """A callable Prefix for our bot. This could be edited to allow per server prefixes."""

    prefixes = ['.'] #Your bot prefix(s)

    return commands.when_mentioned_or(*prefixes)(bot, msg)

bot=commands.Bot(command_prefix=get_prefix,description='Multipurpose Discord Bot')




exts=['music'] #Add your Cog extensions here




@bot.event
async def on_ready():
    song_name='Thinking about america' 
    activity_type=discord.ActivityType.listening
    await bot.change_presence(activity=discord.Activity(type=activity_type,name=song_name))
    print(bot.user.name)

@bot.command()
async def credits(ctx):
    await ctx.send('Made by `Adnan Encoding Org`')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Ping! {round(bot.latency * 1000)}ms')

@bot.command(aliases=['ques' , 'test'])
async def _ques(ctx,*, question):
    responses =['It is certain.',
                'It is decidedly so.',
                'Without a doubt',
                'Yes - definitely',
                'Ask again later.',
                'better not tell you now.',
                'My reply is no.',
                'Very doubtful.',]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@bot.command()
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)


def wiki_summary(arg):
    definition = wikipedia.summary(arg, sentences=3, chars=1000,auto_suggest= True , redirect= True)
    return definition

@bot.command()
async def wiki(ctx):
    words = ctx.message.content.split()
    important_words = words[1:]
    search = discord.Embed(title="Demins search...", description=wiki_summary(important_words),colour=discord.Colour.purple())
    await ctx.channel.send(content=None, embed = search)

@bot.command()
async def trans(ctx,lang,*,args):
    t = Translator()
    a = t.translate(args, dest=lang)
    await ctx.send(a.text)



for i in exts:
    bot.load_extension(i)


bot.run(os.environ['TOKEN'])
