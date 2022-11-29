import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN=os.getenv('TOKEN')
intents=discord.Intents.all()
intents.members=True
client=commands.Bot(command_prefix='!',intents=intents)



@client.event
async def on_message(message):
	username = str(message.author).split("#")[0]
	channel = str(message.channel.name)
	user_message = str(message.content)

	print(f'Message {user_message} by {username} on {channel}')

	if message.author == client.user:
		return

	if channel == "general":
		if user_message.lower() == "hello" or user_message.lower() == "hi":
			await message.channel.send(f'Hello {username}')
			return
		elif user_message.lower() == "bye":
			await message.channel.send(f'Bye {username}')

@client.command(name='ping')
async def ping(ctx):
        await ctx.channel.send('Pong!')

    

client.run(TOKEN)
