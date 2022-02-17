import os,discord, requests
from getpass import getpass

bot_token = os.environ.get('CRYPPY_TOKEN')

if not bot_token:
    print('No env variable CRYPPY_TOKEN set..\n')
    bot_token = getpass('token: ')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message.content=str.lower(message.content)

    if message.content.startswith('$ping'):
        await message.channel.send('pong')

client.run(bot_token)