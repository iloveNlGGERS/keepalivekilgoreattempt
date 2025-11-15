from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel  # Add this import
from clarifai_grpc.grpc.api import service_pb2_grpc, service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2
import discord
import discord.ext
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions, MissingPermissions
import os
import json
import random
import time
import asyncio
import datetime
import re
import aiohttp
import base64
from discord.ui import text_input
import requests
from discord import FFmpegAudio
from discord import FFmpegPCMAudio
import logging
import PIL
from PIL import Image, ImageFilter

logging.getLogger('discord').setLevel(logging.CRITICAL)
logging.getLogger('discord.http').setLevel(logging.CRITICAL)
logging.getLogger('discord.gateway').setLevel(logging.CRITICAL)
logging.getLogger('discord.client').setLevel(logging.CRITICAL)

token = input('Enter token : ')
partsimagepath = "Parts/Parts"
mainpath = input("Go in your file explorer and go inside the folder of this app then right click base.jpg and copy as path and paste it here Ctrl + Shift + V : ")
bot = Bot(command_prefix='~', description="nothing", help_command=None, intents=discord.Intents.all())
imagecalls = {
    #table made by Brok as always gideon on top? (kilgore)
   # -----------------HAIR------------------------#

   "reohair" : f"{partsimagepath + "/Reo hair.png"}",
   "bachirahair" : f"{partsimagepath + "/Bachira hair.png"}",
   "barouhair" : f"{partsimagepath + "/Barou hair.png"}",
   "nagihair" : f"{partsimagepath + "/Nagi hair.png"}",
   "isagihair" : f"{partsimagepath + "/Isagi hair.png"}",
   "nikohair" : f"{partsimagepath + "/Niko hair.png"}",
   "aikuhair" : f"{partsimagepath + "/Aiku hair.png"}",
   "chigirihair" : f"{partsimagepath + "/Chigiri hair.png"}",
   "shidouhair" : f"{partsimagepath + "/Shidou hair.png"}",
   "kunigamihair" : f"{partsimagepath + "/Kunigami hair.png"}",
   # -----------------EYES------------------------#
   "reoeyes" : f"{partsimagepath + "/Reo eyes.png"}",
   "isagieyes" : f"{partsimagepath + "/Isagi eyes.png"}",
   "shidoueyes" : f"{partsimagepath + "/Shidou eyes.png"}",
   "baroueyes" : f"{partsimagepath + "/Barou eyes.png"}",
   "kunigamieyes" : f"{partsimagepath + "/Kunigami eyes.png"}",
   "aikueyes" : f"{partsimagepath + "/Aiku eyes.png"}",
   "nagieyes" : f"{partsimagepath + "/Nagi eyes.png"}",
   "chigirieyes" : f"{partsimagepath + "/Chigiri eyes.png"}",
   # -----------------MOUTH------------------------#
   "reomouth" : f"{partsimagepath + "/Reo mouth.png"}",
   "baroumouth" : f"{partsimagepath + "/Barou mouth.png"}",
   "kunigamimouth" : f"{partsimagepath + "/Kunigami mouth.png"}",
   "shidoumouth" : f"{partsimagepath + "/Shidou mouth.png"}",
   "chigirimouth" : f"{partsimagepath + "/Chigiri mouth.png"}",
   "isagimouth" : f"{partsimagepath + "/Isagi mouth.png"}",
   "aikumouth" : f"{partsimagepath + "/Aiku mouth.png"}",
   "nagimouth" : f"{partsimagepath + "/Nagi mouth.png"}",
   # -----------------the end of the dictionary YPIEEEEEE------------------------#



}

@bot.event
async def on_ready():
  await bot.change_presence(activity= discord.Game("GideonAPI by Brok"), status=discord.Status.dnd)
  os.system("title Gideon image modifier by kilgore")
  os.system("cls")


@bot.event
async def on_guild_join(guild):
    embed = discord.Embed(
        title="Gideon",
        description="Gideon API or kilgore is a application hosted on any device if own the exe file",
        color=0x00ff00  
    )
    embed.add_field(name="~imagemodifier", value="asks you a combination of sentences and u have to respond afterwards (You can use the dictionary keys or the parts folder) Recommended to use keys", inline=False)
    embed.add_field(name="Keys available", value="""   "reohair" : f"
   "bachirahair" 
   "barouhair" 
   "nagihair" 
   "isagihair
   "nikohair" 
   "aikuhair" 
   "chigirihair"
   "shidouhair" 
    it goes on till mouth-eyes-hair                 """, inline=False)
    
    await guild.text_channels[0].send(embed=embed)


@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Gideon",
        description="Gideon API or kilgore is a application hosted on any device if own the exe file",
        color=0x00ff00  
    )
    embed.add_field(name="~imagemodifier", value="asks you a combination of sentences and u have to respond afterwards (You can use the dictionary keys or the parts folder) Recommended to use keys", inline=False)
    embed.add_field(name="Keys available", value="""   "reohair" : f"
   "bachirahair" 
   "barouhair" 
   "nagihair" 
   "isagihair
   "nikohair" 
   "aikuhair" 
   "chigirihair"
   "shidouhair" 
    it goes on till mouth-eyes-hair                 """, inline=False)
    
    await ctx.send(embed=embed)
@bot.command()
async def imagemodifier(ctx):
    base_image_path = mainpath
    async def get_image(prompt):
        await ctx.send(prompt)
        try:
            msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=60.0)
            gottenvars = imagecalls.get(msg.content)
            if gottenvars:
                print("path : " + gottenvars, " message content : " + msg.content)
                return gottenvars
        
            if not gottenvars:
                await ctx.send("You used images(Attachements) which works  or i didn't find any keys that match the exact message you sent, in the datastore, " + f"message content : {msg.content}" + ". You can always use the Parts folder!")
                
            if msg.attachments:
                attachment = msg.attachments[0]
                if attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    await attachment.save(attachment.filename)  
                    return attachment.filename
                else:
                    await ctx.send("Please send a valid image file (PNG/JPG).")
                    return None
            else:
                await ctx.send("No image attached. Try again.")
                return None
        except asyncio.TimeoutError:
            await ctx.send("Timed out. Command cancelled.")
            return None
    
    hair_path = await get_image("Please send your hair image.")
    if not hair_path: return
    
    eyes_path = await get_image("Please send your eyes image.")
    if not eyes_path: return
    
    mouth_path = await get_image("Please send your mouth image.")
    if not mouth_path: return
    
    try:
        base_img = Image.open(base_image_path).convert("RGBA")
        base_width, base_height = base_img.size
        center_x = base_width // 2
    except FileNotFoundError:
        await ctx.send("Base image not found. Ensure 'base.jpg' is in the script directory.")
        return
    
    try:
        hair_img = Image.open(hair_path).convert("RGBA")
        eyes_img = Image.open(eyes_path).convert("RGBA")
        mouth_img = Image.open(mouth_path).convert("RGBA")
        

        hair_center = (center_x, base_height // 4 + 155) 
        eyes_center = (center_x, base_height // 2 - 20)  
        mouth_center = (center_x, 3 * base_height // 4 - 185)  
        hair_x = hair_center[0] - hair_img.width // 2
        hair_y = hair_center[1] - hair_img.height // 2
        eyes_x = eyes_center[0] - eyes_img.width // 2
        eyes_y = eyes_center[1] - eyes_img.height // 2
        mouth_x = mouth_center[0] - mouth_img.width // 2
        mouth_y = mouth_center[1] - mouth_img.height // 2
        
        
        base_img.paste(hair_img, (hair_x, hair_y), hair_img)
        base_img.paste(eyes_img, (eyes_x, eyes_y), eyes_img)
        base_img.paste(mouth_img, (mouth_x, mouth_y), mouth_img)
        
      
        output_path = 'modified_image.png'
        base_img.save(output_path)
        await ctx.send(file=discord.File(output_path))
        
      
        os.remove(hair_path)
        os.remove(eyes_path)
        os.remove(mouth_path)
        os.remove(output_path)
        
    except Exception as e:
        await ctx.send(f"Error processing images: {str(e)}")
try:
    bot.run(token)

except Exception as e:

    print("Token failed")