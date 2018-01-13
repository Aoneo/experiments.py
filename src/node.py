# https://discordapp.com/oauth2/authorize?client_id=377864481633730563&permissions=2146958591&scope=bot

import discord
import asyncio
client = discord.Client()

prefix = "n!"

@client.event
async def on_ready():
    print('Logged in as %s'%(client.user.name))
    print('ID: %s'%(client.user.ID))
    print('Node.py ready for service!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith(prefix + 'ping'):
        await client.send_message(message.channel, 'Pong!')


@client.run('Mzc3ODY0NDgxNjMzNzMwNTYz.DOTJSg.xzlo_tB71sG4ua7g98eHH7XXeMU')