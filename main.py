import discord
import json
import copy

client = discord.Client()
baseHydraState = {
    'light': [],
    'darkness': [],
    'earth': [],
    'water': [],
    'fire': [],
    'wind': []
}

hydra3 = copy.deepcopy(baseHydraState)
hydra4 = copy.deepcopy(baseHydraState)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        await message.channel.send('Simple explanation\n'
                                   '!hydra3 is ancient hydra and !hydra4 is for dreadful\n'
                                   'then add/remove/view/reset and finally user to generate a command like\n'
                                   'specify one of light,darkness,earth,water,fire,wind next\n'
                                   '!hydra4 add light chancellor')
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!hydra3'):
        await handle_action(message, hydra3)

    if message.content.startswith('!hydra4'):
        await handle_action(message, hydra4)


async def handle_action(message, hydra_dict):
    content_list = message.content.split(' ')
    action = content_list[1]
    if action == 'add':
        hydra_dict.get(content_list[2]).append(content_list[3])
    elif action == 'reset':
        hydra_dict.update(copy.deepcopy(baseHydraState))
    elif action == 'remove':
        hydra_dict.get(content_list[2]).remove(content_list[3])
    await message.channel.send(json.dumps(hydra_dict))


client.run('')
