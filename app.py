import os,discord,requests,string
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

    message_partiton = message.content.partition(' ')

    match message_partiton[0]:
        case '$ping':
            await message.channel.send('pong')
        case '$price':
            await price_check(message_partiton[2])
        case _:
            return

async def price_check(message):
    # check coinbase for price of coin specified
    print(f'price check request recieved for {message}')


client.run(bot_token)