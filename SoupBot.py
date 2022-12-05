import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands
from discord import FFmpegPCMAudio

load_dotenv()
TOKEN=os.getenv('TOKEN')
intents=discord.Intents.all()
bot=commands.Bot(command_prefix='!',intents=intents)


@bot.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        messages=["is your refrigerator running?", "i just told ur mom what u did", "hey have you tried the poop command", "i know the answers to your security questions", "i just uploaded your search history to linkedin", "the cake is a lie", "ratio", "wanna have a snowball fight denji?", "i am literally in your walls", "hi!", "beep boop", "i just sold your information to the US government"]
        response=random.choice(messages)
        await message.author.send(response)
    await bot.process_commands(message)

 
@bot.command(name='poop', help='poopfart!')
async def poop(ctx):
        await ctx.send('fart')

@bot.command(name='intro', help='Gets you started!')
async def intro(ctx):
        await ctx.send('Welcome to SoupBot!\nUse !join to get SoupBot to join your current voice channel, and !leave for SoupBot to leave.\nUse !list for a full list of sound effects and their commands!')
        
@bot.command(name='join',help='Tells SoupBot to join the voice channel you are currently in')
async def join(ctx):
        if not ctx.message.author.voice:
                await ctx.send(f'hey {ctx.message.author.name}, connect to a channel first!')
                return
        else:
                try:
                        channel=ctx.message.author.voice.channel
                        bot_channel=ctx.guild.voice_client
                        await channel.connect()
                except:
                        if ctx.author.voice.channel==ctx.voice_client.channel:
                            await ctx.send('Cannot join, SoupBot is already in channel')
                        else:
                            await ctx.send('Use !leave first before joining a new channel')

@bot.command(name='leave', help='Tells SoupBot to leave the voice channel')
async def leave(ctx):
        voice_client=ctx.message.guild.voice_client
        try:
                await voice_client.disconnect()
        except:
                await ctx.send('Cannot leave, SoupBot is not connected to a voice channel')

@bot.command(name='list',help='Lists all possible sound effects')
async def list(ctx):
        sounds=("bruh (!bruh)\nvine boom (!boom)\nanime wow (!wow)\noutro music (!outro)\noh brother this guy stinks!!! (!stinks)\nminecraft steve taking damage (!steve)\nminecraft villager hurr (!villager)\nWHAT IS THAT MELODY?? (!melody)")
        await ctx.send(f'all sound effects and their commands: \n{sounds}')


@bot.command(name='bruh')
async def bruh(ctx):
        voice_client=ctx.message.guild.voice_client
        try:
                server=ctx.message.guild
                voice_channel=server.voice_client
                async with ctx.typing():
                        voice_channel.play(discord.FFmpegPCMAudio(executable='ffmpeg.exe',source='bruh.mp3'))
        except:
                if voice_client==None:
                    await ctx.send('SoupBot is not connected to a voice channel')
                else:
                    return

@bot.command(name='boom')
async def boom(ctx):
        voice_client=ctx.message.guild.voice_client
        try:
                server=ctx.message.guild
                voice_channel=server.voice_client
                async with ctx.typing():
                        voice_channel.play(discord.FFmpegPCMAudio(executable='ffmpeg.exe',source='vineboom.mp3'))
        except:
                if voice_client==None:
                    await ctx.send('SoupBot is not connected to a voice channel')
                else:
                    return
                
@bot.command(name='wow')
async def wow(ctx):
        voice_client=ctx.message.guild.voice_client
        try:
                server=ctx.message.guild
                voice_channel=server.voice_client
                async with ctx.typing():
                        voice_channel.play(discord.FFmpegPCMAudio(executable='ffmpeg.exe',source='wow.mp3'))
        except:
                if voice_client==None:
                    await ctx.send('SoupBot is not connected to a voice channel')
                else:
                    return
                
@bot.command(name='outro')
async def outro(ctx):
        voice_client=ctx.message.guild.voice_client
        try:
                server=ctx.message.guild
                voice_channel=server.voice_client
                async with ctx.typing():
                        voice_channel.play(discord.FFmpegPCMAudio(executable='ffmpeg.exe',source='outro.mp3'))
        except:
                if voice_client==None:
                    await ctx.send('SoupBot is not connected to a voice channel')
                else:
                    return

@bot.command(name='stinks')
async def stinks(ctx):
        voice_client=ctx.message.guild.voice_client
        try:
                server=ctx.message.guild
                voice_channel=server.voice_client
                async with ctx.typing():
                        voice_channel.play(discord.FFmpegPCMAudio(executable='ffmpeg.exe',source='stinks.mp3'))
        except:
                if voice_client==None:
                    await ctx.send('SoupBot is not connected to a voice channel')
                else:
                    return

@bot.command(name='villager')
async def villager(ctx):
        voice_client=ctx.message.guild.voice_client
        try:
                server=ctx.message.guild
                voice_channel=server.voice_client
                async with ctx.typing():
                        voice_channel.play(discord.FFmpegPCMAudio(executable='ffmpeg.exe',source='villager.mp3'))
        except:
                if voice_client==None:
                    await ctx.send('SoupBot is not connected to a voice channel')
                else:
                    return

@bot.command(name='steve')
async def steve(ctx):
        voice_client=ctx.message.guild.voice_client
        try:
                server=ctx.message.guild
                voice_channel=server.voice_client
                async with ctx.typing():
                        voice_channel.play(discord.FFmpegPCMAudio(executable='ffmpeg.exe',source='steve.mp3'))
        except:
                if voice_client==None:
                    await ctx.send('SoupBot is not connected to a voice channel')
                else:
                    return

@bot.command(name='melody')
async def melody(ctx):
        voice_client=ctx.message.guild.voice_client
        try:
                server=ctx.message.guild
                voice_channel=server.voice_client
                async with ctx.typing():
                        voice_channel.play(discord.FFmpegPCMAudio(executable='ffmpeg.exe',source='melody.mp3'))
        except:
                if voice_client==None:
                    await ctx.send('SoupBot is not connected to a voice channel')
                else:
                    return
                
bot.run(TOKEN)
