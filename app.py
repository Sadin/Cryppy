import os,discord,requests,string
from coinbase.wallet.client import Client as CoinbaseClient
from getpass import getpass

bot_token = os.environ.get('CRYPPY_TOKEN')
api_key = os.environ.get('API_KEY')
api_secret = os.environ.get('COINBASE_SECRET')

if not bot_token:
    print('No env variable CRYPPY_TOKEN set..\n')
    bot_token = getpass('token: ')

client = discord.Client()
coinbase_client = CoinbaseClient(api_key, api_secret, api_version='2021-02-07')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # ignore if message was sent by this bot user
    if message.author == client.user:
        return

    # partition message for ease of use with case / functions
    message_partiton = message.content.partition(' ')

    # match a command or ignore
    match message_partiton[0]:
        case '$ping':
            await message.channel.send('pong')
        case '$price':
            await price_check_coinbase(message, message_partiton[2])
        case _:
            return

async def price_check_coinbase(message, message_body):
    # check coinbase for price of coin specified
    # handle empty message after command
    if not message_body == '':
        response = f'price check request recieved for {message_body}'
        print(response)
        await message.channel.send(response)
        
        price = coinbase_client.get_spot_price(currency_pair=f'{str.upper(message_body)}-USD')
        response = f'price per {str.upper(message_body)} is {price["amount"]} USD'
    else:
        response = 'price check request recieved but no coin specified'

    print(response)
    await message.channel.send(response)
    


client.run(bot_token)