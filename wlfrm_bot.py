# wlfm_bot.py
import os
import random
import wolframalpha

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN') # keep token in .ENV file for security
APP_ID = os.getenv('APP_ID') # keep wolfram alpha app id in .ENV for security

client = wolframalpha.Client(APP_ID)
bot = commands.Bot(command_prefix='!') # prefix command to call bot

@bot.command(name='wolfram', help='solves an equation in Wolfram Alpha')
async def wlfrm(ctx, *message): # use tuple as parameter to read line
    question = ' '.join(message)# join tuple so that Wolfram Alpha API get sentence as input
    res = client.query(question)
    answer = next(res.results).text # recieve only text result 
    await ctx.send(answer) # send result into chat

bot.run(TOKEN)
