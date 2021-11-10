import discord
import asyncio

import urllib
import time
import json


with open("config.json") as f:
    config = json.load(f)

TOKEN = config['token']
URLS = config['urls']
CHANNEL_ID = config['channel_id']
SLEEP = config['sleep']


channel = None
client = discord.Client()


async def discord_perror(msg):
    channel = client.get_channel(CHANNEL_ID)

    msg = f"Error: {msg}"

    print(msg)
    await channel.send(msg)


async def loop():
    for url in URLS:
        code = None

        try:
            response = urllib.request.urlopen(url)
            code = response.getcode()
            print(f"code: {code}")

        except Exception as e:
            await discord_perror(f"{url}: {e}")
            continue

        if code != 200:
            await discord_perror(f"{url}: code is {code}")


@client.event
async def on_ready():
    print('loggined')

    while True:
        time.sleep(SLEEP)

        print('loop!')

        try:
            await loop()
        except Exception as e:
            discord_perror()


client.run(TOKEN)
