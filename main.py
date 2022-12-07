import discord
import os
intents = discord.Intents.all()
client = discord.Client(intents=intents)
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
    
    
    
    if user_message.lower() == "!anywhere":
        await message.channel.send("this can be used anywhere!")
        return    
            
            
              
        
   
        
#pourcourir tout les guilds et envoyer un message dans le channel 

client.run("MTA0NzgxMjAyMjc4OTczNDQ4MA.GKkSXC.-LW3imofl3ezjvxcNlKTNr4ERh-8W-yl1K2oYM")