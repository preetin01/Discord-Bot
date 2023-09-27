# get the responses from the bot, such as text, image, audio, video, and pdf files. 

import discord
from discord.ext import commands


#to get discord online
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents = intents)
bot = commands.Bot(command_prefix='!', intents=intents)


# to create Clients event
@client.event    #event
async def on_ready():    #function
    print("We have logged in as {0.user}".format(client))
 
    
@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))
   
# Command to add two numbers
@bot.command()
async def add(ctx, num1: float, num2: float):
    result = num1 + num2
    await ctx.send(f"The sum of {num1} and {num2} is {result}")   
    
    
@client.event    #event 
async def on_message(message):      #function
    if message.author == client.user:
        return
    if message.content.startswith("hi"):
        await message.channel.send("Hey There!")
    
    
    if message.content.startswith("ping"):
        await message.channel.send("pong")    
        
        
    if message.content.startswith("image"):
        await message.channel.send(file = discord.File("download.jpeg"))  
        
        
    # command for video
    if message.content.startswith("video"):
        await message.channel.send(file = discord.File("ImGroot.mp4")) 
    
    
    #command for audio 
    if message.content.startswith("audio"):
        await message.channel.send(file = discord.File("iraaday.mp3")) 
    
    
    #command for pdf file
    if message.content.startswith("file"):
        await message.channel.send(file = discord.File("course.pdf"))     
        
        
        
client.run("Your Token")       
