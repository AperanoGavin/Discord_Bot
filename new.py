import discord
import os
import requests
from discord import app_commands

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


client.run("MTA1MDM4ODY2NTYxODE1MzUyNA.GBn3U1.JEsdfTpS0ckza-eGo7Uj81PnR5S1YE9cnAPI1k")