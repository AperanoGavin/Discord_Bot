import discord
import os
import io
import requests
import json
import xmltodict
import asyncio
import re
from discord import app_commands
import time
import datetime
from datetime import timedelta
import mysql.connector as sql
from deep_translator import GoogleTranslator



mydb = sql.connect(
    host = "sql7.freemysqlhosting.net",
    user = "sql7584311",
    password = "kPsBAhZcwS",
     database= "sql7584311"
)




url = "https://api-football-v1.p.rapidapi.com/v3/timezone"

headers = {
	"X-RapidAPI-Key": "3ae49bd480msh5a2534d4142299ep1d1970jsn9bdcd8eb72ba",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers)



url_anime = "https://any-anime.p.rapidapi.com/anime/img"

headers_anime = {
	"X-RapidAPI-Key": "3ae49bd480msh5a2534d4142299ep1d1970jsn9bdcd8eb72ba",
	"X-RapidAPI-Host": "any-anime.p.rapidapi.com"
}

response_anime = requests.request("GET", url_anime, headers=headers)








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
        elif user_message.lower() == "!dog":
            response2 = requests.get("https://dog.ceo/api/breeds/image/random")
            #envoyer response2.message dans le channel
            await message.channel.send(response2.json()["message"])
            print(response2.json())          
            return
        elif user_message.lower() == "!quote":
            response4 = requests.get("https://animechan.vercel.app/api/random")
            response4_quote = response4.json()["quote"]
            response4_quote_translate = GoogleTranslator(source='auto', target='fr').translate(response4_quote)
            # outpout -> Ich möchte diesen Text übersetzen
            #envoyer response2.message dans le channel
            await message.channel.send(response4.json()["character"])
            await message.channel.send("à dit un jour dans " )
            await message.channel.send(response4.json()["anime"])
            await message.channel.send(response4_quote_translate)
            print(response4.json())          
            return
        elif user_message.lower() == "!onlyquote":
            response5 = requests.get("https://animechan.vercel.app/api/random")
            response5_quote = response5.json()["quote"]
            response5_quote_translate = GoogleTranslator(source='auto', target='fr').translate(response5_quote)
            await message.channel.send(response5_quote_translate)
            return     
        elif user_message.lower() == "!anime":
            #await message.channel.send(response_anime.json())
            response_ani = requests.get("https://pic.re/image")
            await message.channel.send(response_ani.headers["image_source"])   
 
            return
        elif user_message.lower() == "!cat":
            #envoyer response2.message dans le channel
            await message.channel.send("https://cataas.com/cat")
            return
        elif user_message.lower() == "!bye" and username == "Gavin APERANO":
            await message.channel.send("bye bye")
            await client.close()
            return
        elif user_message.lower() == "!anime":
            response_nsfw = requests.get("https://nekos.life/api/v2/img/lewd")
            
                    
  

       
@tree.command(name="foot" , description="afficher le calendrier des matchs de foot")
async def foot( interaction: discord.Interaction):
    await interaction.response.send_message(response.text[0:1000])  
    
@tree.command(name="anime" , description="type(sfw) category (waifu,bully,cuddle, cry) ou type (nsfw) (blowjob ,neko , trap, waifu)")
async def anime( interaction: discord.Interaction , type: str , category: str):
    url_anime_command =  f"https://api.waifu.pics/{type}/{category}"
    get_anime = requests.get(url_anime_command)
    await interaction.response.send_message(get_anime.json()["url"]) 
    
@tree.command(name = "idnba")
async def id_nba( interaction: discord.Interaction , name: str ):
    url_id_nbaplayer = f"https://www.balldontlie.io/api/v1/players?search={name}"
    get_idnbaplayer = requests.get(url_id_nbaplayer)
    get_reel_id = get_idnbaplayer.json()["data"][0]["id"]
    await interaction.response.send_message(get_reel_id)      



@tree.command(name="nba" , description= " info about nba player")    
async def nba( interaction: discord.Interaction , id: int ):
    url_nba_command =  f"https://www.balldontlie.io/api/v1/players/{id}"
    get_nba= requests.get(url_nba_command)
    get_nba_name = get_nba.json()["first_name"]
    get_nba_position = get_nba.json()["position"]
    get_nba_team = get_nba.json()["team"]["full_name"]
    get_nba_weight = get_nba.json()["weight_pounds"]

    embed = discord.Embed(title =" nba players stats " , description= "all of this player" , color= discord.Colour.random())    
    embed.add_field(name = "Name",value= get_nba_name)
    embed.add_field(name ="Position", value = get_nba_position)
    embed.add_field(name="Team",value = get_nba_team)
    embed.add_field(name="Weight", value = get_nba_weight)
    await interaction.response.send_message( embed = embed)      
    
@tree.command(name="project" , description="le nombre de jours où tu penses l'avoir fini et nom du projet")
async def project( interaction: discord.Interaction, project: str , day: int):
     user = interaction.user.mention
     date = datetime.date.today()
     date_fin = date + timedelta(days=day)
     print (mydb)
     print(time.time())    
     print (datetime.date.today())
     await interaction.response.send_message(f"😆{user} commence un nouveau projet qu'il a appélé  {project} souhaitons lui bonne chance il en a pour {day} jours")  
    
     cursor = mydb.cursor()
     query = """
            INSERT INTO project
            (id_discord, title , date_start_at, date_end_at)
            VALUES (?, ? , ? , ?)
        """
     values = [(interaction.user.id, project, date, date_fin)]   
     cursor.executemany(query, values)
     
     with open("project.txt", "a+") as f: 
         int = f.readlines()
         f.write(f"{int} {project} {day} {user}")
         f.write(f"{date} {date_fin} \n")
         f.close()



               
client.run("Token")