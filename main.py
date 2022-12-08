import discord
import os
import requests
from discord import app_commands
import interactions

url = "https://api-football-v1.p.rapidapi.com/v3/timezone"

headers = {
	"X-RapidAPI-Key": "3ae49bd480msh5a2534d4142299ep1d1970jsn9bdcd8eb72ba",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}
response = requests.request("GET", url, headers=headers)
#récuperer que les 4000 premier caractères de la réponse et les afficher en string
print(response.text[0:4000])



intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
GUILD = os.getenv('1047812022789734480')
#intents = discord.Intents.default()
#intents.message_content = True
        
@client.event
async def on_ready():
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
        elif user_message.lower() == "!abdou":
            await message.channel.send(f"il pue bien sa mère")
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
        elif username == "adia" and message.channel.name == "langue-de-molière" or message.channel.name == "général":
            await message.channel.send(f" j'ai d'abord rappelé à {username} qu'il n'a jamais été un grand joueur de foot")
            await message.channel.send(file=discord.File('./etp.jpeg'))
            return
           

        
#pourcourir tout les guilds et envoyer un message dans le channel 

client.run("MTA0NzgxMjAyMjc4OTczNDQ4MA.G4BPik.98asQSXagjsjBGUMuBsNPk2RUPvlOORMvdcEnA")