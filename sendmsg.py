import sys
import random
import json
import requests
import discord

if len(sys.argv) >= 2:
    DISCORD_TOKEN = sys.argv[1]
else:
    print("No discord bot token provided!")
    sys.exit()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

        requestHeaders = {
            'User-Agent': 'Plateauschuhe-bot 0.1'
        }
        imgSearchResults = requests.get("https://api.qwant.com/api/search/images?count=100&q=plateauschuhe&t=images&safesearch=1&locale=fr_FR&uiv=4", headers=requestHeaders).json()
        imgDict = imgSearchResults["data"]["result"]["items"]
        imgObj = random.choice(imgDict)
        imgUrl = "https:" + imgObj["media_fullsize"]
        channel = self.get_channel(677885779267289092)
        await channel.send('@everyone Voici une nouvelle plateauschuhe jaaaaa \n' + imgUrl)
        await channel.send('_Fonctionne avec Qwant images. Problème ou question DM Locness#0031_')
        sys.exit()

client = MyClient()
client.run(DISCORD_TOKEN)
