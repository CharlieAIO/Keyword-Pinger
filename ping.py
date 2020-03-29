import discord
from discord.ext import commands
import json
client = discord.Client()

with open("config.json") as f:
    js_data = json.loads(f.read())

TOKEN = (js_data["token"])
print(f"TOKEN LOAD -- {TOKEN}")

keywords = (js_data["keywords"])
print(f"KEYWORDS LOADED -- {keywords}")


@client.event
async def on_ready():
    print('Logged in as %s' %client.user.name)

@client.event
async def on_message(message):
    if message.author.bot: return
    for keyword in keywords:
       if keyword.lower() in message.content.lower() and message.channel.name == "mr-porter"or "supreme" or "mesh":
         await client.send_message(message.channel,f"```Keyword Matched --> {keyword.lower()} <--```")
         break

client.run(TOKEN)
