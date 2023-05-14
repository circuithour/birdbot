from discord.ext import commands
import discord
import time
from datetime import datetime
import requests
import asyncio

url = "http://shibe.online/api/birds?count=1&urls=true&httpsUrls=true"

channel_ids = []

BOT_TOKEN = "MTAwNDg3NTI0MzAzMjE1ODI4OQ.Gygouk.z4st32cmQACYpXHBAXG4wxW3AxF0KL3rlZwLnM"

bot = commands.Bot(command_prefix="&", intents=discord.Intents.all())

hours = ["0:0", "1:0", "2:0", "3:0", "4:0", "5:0", "6:0", "7:0", "8:0", "9:0", "10:0", "11:0", "12:0", "13:0", "14:0", "15:0", "16:0", "17:0", "18:0", "19:0", "20:0", "21:0", "22:0", "23:0"]

@bot.event
async def on_ready():
    print("Obama Initialized")

async def bird(channel_id):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        channel = bot.get_channel(channel_id)
        await channel.send(data[0])
    else:
        print("An error occurred:", response.status_code)

@bot.command()
async def birdy(ctx):
    channel_id = ctx.channel.id
    if channel_id not in channel_ids:
        channel_ids.append(channel_id)
        await ctx.send('Added channel ID to the list!')
    else:
        await ctx.send('Channel ID is already in the list!')

@bot.command()
async def unbirdy(ctx):
    channel_id = ctx.channel.id
    if channel_id in channel_ids:
        channel_ids.remove(channel_id)
        await ctx.send('You have been removed from bird  daily')
    else:
        await ctx.send('You are not subsrcribed to bird daily!!!')
         

@bot.command()
async def test(ctx):
    print(channel_ids)
    for channel_id in channel_ids:
                await bird(channel_id)



@bot.event
async def send_bird_images():
    await bot.wait_until_ready()
    while not bot.is_closed():
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        if current_time in hours:
            for channel_id in channel_ids:
                await bird(channel_id)
        await asyncio.sleep(60)

bot.loop.create_task(send_bird_images())
bot.run(BOT_TOKEN)