import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in")

@client.event
async def on_message(message):
    emojis = ["👍", "👎"]

    react_num = random.randint(0, len(emojis) - 1)
    await client.add_reaction(message, emojis[react_num])

# test
@client.event
async def on_message(message):
     if message.content.startswith("こんにちは"):
          if client.user != message.author:
              await client.send_message(message.channel, "こんにちは,#{message.author.name}さん")

    
    
if __name__ == "__main__":
    client.run("")
