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
            await price_check(message, message_partiton[2])
        case _:
            return

async def price_check(message, message_body):
    if not message_body == '':
        # check coinbase for price of coin specified
        response = f'price check request recieved for {message_body}'
    else:
        response = 'price check request recieved but no coin specified'
        
    print(response)
    await message.channel.send(response)
    



client.run(bot_token)