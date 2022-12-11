import discord
import os
import io
import requests
import PIL
import json
import asyncio
import re
from discord import app_commands
from PIL import Image
import time
import datetime

url = "https://api-football-v1.p.rapidapi.com/v3/timezone"

headers = {
	"X-RapidAPI-Key": "3ae49bd480msh5a2534d4142299ep1d1970jsn9bdcd8eb72ba",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers)
#récuperer que les 4000 premier caractères de la réponse et les afficher en string
#print(response.text[0:4000])



url_anime = "https://any-anime.p.rapidapi.com/anime/img"

headers_anime = {
	"X-RapidAPI-Key": "3ae49bd480msh5a2534d4142299ep1d1970jsn9bdcd8eb72ba",
	"X-RapidAPI-Host": "any-anime.p.rapidapi.com"
}

response_anime = requests.request("GET", url_anime, headers=headers)

#print(response_anime.text)







intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
GUILD = os.getenv('1047812022789734480')
#intents = discord.Intents.default()
#intents.message_content = True
        
@client.event
async def on_ready():
    synced = await tree.sync()
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
 
    
         
         

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    anime_name = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username} : {user_message} ({channel})')
    
    if message.author == client.user:
        return
    
    if message.channel.name == "général" or message.channel.name == "langue-de-molière" or message.channel.name == "test-bot-veen" or message.channel.name == "myges-api-for-adiadev" :
        if user_message.lower() == "hello":
            await message.channel.send(f"Hello {username}!")
            return
        elif username.lower() == "Bye":
            await message.channel.send(f"Bye {username}!")
            return
        elif user_message.lower() == "!insulte":
            await message.channel.send(f"Belek le nouveau")
            return
        elif user_message.lower() == "!precise"  and username == "Gavin APERANO":
            username2="The dev"
            await message.channel.send(f"On parle de toi {username2}!")
            return
        elif user_message.lower() == "!abdou":
            await message.channel.send(f"il pue bien sa mère")
            return
        elif user_message.lower() == "precise qu'on parle de se batard"  and username == "Gavin APERANO":
            await message.channel.send(f"on parle de toi abdou")
            return
        elif user_message.lower() == "@Gavin APERANO c'est toi tu pues !":
            await message.channel.send(f"toi trouve toi une vie")
            return
        
        elif user_message.lower() == "!rigole":
            await message.channel.send(f"🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣")
            return
        
        elif user_message.lower() == "!worldcup":
            await message.channel.send(f"https://www.youtube.com/watch?v=8n5dJwWXrbo")
            return

        elif user_message.lower() == "!foot":
            await message.channel.send(response.text[0:1000])
            return
        elif user_message.lower() == "!done":
            await message.channel.send("il est temps d'aller rompishpish")
            await message.channel.send("http://gavinaperano.com/Vid/thegoat.mp4")
            return
        #à chaque fois que le message.author ==adia#3344 envoie un message dans le channel "général" le bot envoie un message dans le channel "général" et afficher la photo etp.jpeg qui est dans le dossier du bot
        #elif username == "adia" and message.channel.name == "langue-de-molière":
        #    await message.channel.send(f" j'ai d'abord rappelé à {username} qu'il n'a jamais été un grand joueur de foot")
        #  await message.channel.send(file=discord.File('./etp.jpeg'))
        #  return
        #envoyer une photo de chat random à chaque fois qu'on fait !chat
        elif user_message.lower() == "!dog":
            response2 = requests.get("https://dog.ceo/api/breeds/image/random")
            #envoyer response2.message dans le channel
            await message.channel.send(response2.json()["message"])
            print(response2.json())          
            return
        elif user_message.lower() == "!quote":
            response4 = requests.get("https://animechan.vercel.app/api/random")
            #envoyer response2.message dans le channel
            await message.channel.send(response4.json()["character"])
            await message.channel.send("said one day in" )
            await message.channel.send(response4.json()["anime"])
            await message.channel.send(response4.json()["quote"])
            print(response4.json())          
            return
        elif user_message.lower() == "!onlyquote":
            response5 = requests.get("https://animechan.vercel.app/api/random")
            #envoyer response2.message dans le channel
            await message.channel.send(response5.json()["quote"])
            return     
        elif user_message.lower() == "!anime":
            #await message.channel.send(response_anime.json())
            response_ani = requests.get("https://pic.re/image")
            #envoyer le body de la requête dans le channel
            await message.channel.send(response_ani.headers["image_source"])   
 
            return
        elif user_message.lower() == "!cat":
            #envoyer response2.message dans le channel
            await message.channel.send("https://cataas.com/cat")
            return
        #si la personne écrit !bye éteindre le bot
        elif user_message.lower() == "!bye" and username == "Gavin APERANO":
            await message.channel.send("bye bye")
            await client.close()
            return
                    
  

       
@tree.command(name="foot" , description="afficher le calendrier des matchs de foot")
async def foot( interaction: discord.Interaction):
    await interaction.response.send_message(response.text[0:1000])  
    
@tree.command(name="project" , description="le nombre de jours où tu penses l'avoir fini et nom du projet")
async def project( interaction: discord.Interaction, project: str , day: int):
     user = interaction.user.mention
     date = datetime.date.today()
     date_fin = date + timdelta(days=day)
     print(time.time())     #username = interaction.user.name
     print (datetime.date.today())
     await interaction.response.send_message(f"😆{user} commence un nouveau projet qu'il a appélé  {project} souhaitons lui bonne chance il en a pour {day} jours")     
     #sauvergarder tous les projets dans un fichier
     with open("project.txt", "a") as f: 
         f.write(f"{project} {day} {user}")
         f.write(f"{date} {date_fin} \n")
         f.close()

client.run("Token")