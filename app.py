import os,discord,requests,string
from coinbase.wallet.client import Client as CoinbaseClient
from collections import deque
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
    # input needs to be sanitized so that trailing extra message text is dropped, but conversion price is not lost
    currency_pair = message_partiton[2].split(' ', 2)

    # match a command or ignore
    match message_partiton[0]:
        case '$ping':
            await message.channel.send('pong')
        case '$price':
            print(currency_pair)
            await price_check_coinbase(message, currency_pair)
        case _:
            return

async def price_check_coinbase(message, pair: list):
    # check coinbase for price of coin specified
    # handle empty message after command
    if not len(pair) == 0:
        response = f'price check request recieved for {str.upper(pair[0])}'
        print(response)
        await message.channel.send(response)

        price = coinbase_client.get_spot_price(currency_pair=f'{str.upper(pair[0])}-{str.upper(pair[1])}')
        response = f'price per {str.upper(pair[0])} is {price["amount"]} {pair[1]}'
    else:
        response = 'price check request recieved but no coin specified'

    print(response)
    await message.channel.send(response)
    


client.run(bot_token)