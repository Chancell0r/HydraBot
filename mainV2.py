import discord

from entity.attacker import Attacker
from entity.hydra import generate_base_hydras, generate_base_hydra

client = discord.Client()
hydras = generate_base_hydras()


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
                                   'say order in which to attack\n'
                                   'optionally after attacking specify remaining health\n'
                                   'Add Attacker:\t\t\t!hydra4 add light chancellor 2\n'
                                   'Attack:\t\t\t\t\t\t!hydra4 attack light chancellor 2 50000000\n'
                                   'Remove Attacker:\t!hydra4 remove light chancellor 2\n'
                                   'View Hydra Status:\t!hydra4 view\n'
                                   'Reset Hydra State:\t!hydra4 reset')
        return

    if message.content.startswith('!hydra'):
        await handle_action(message)


async def handle_action(message):
    content_list = message.content.split(' ')
    hydra_difficulty = content_list[0][1:len(content_list[0])]
    hydra = hydras[hydra_difficulty]
    action = content_list[1]
    if action == 'add':
        element = content_list[2]
        for hydra_head in hydra:
            if hydra_head.element == element:
                hydra_head.add_attacker(Attacker(content_list[3], content_list[4], False))

    elif action == 'reset':
        hydras[hydra_difficulty] = generate_base_hydra(hydra_difficulty)
        hydra = hydras[hydra_difficulty]
    elif action == 'remove':
        element = content_list[2]
        for hydra_head in hydra:
            if hydra_head.element == element:
                hydra_head.remove_attacker(content_list[3])
    elif action == 'attack':
        element = content_list[2]
        for hydra_head in hydra:
            if hydra_head.element == element:
                hydra_head.use_attack(Attacker(content_list[3], content_list[4], False))
                if len(content_list) > 5:
                    hydra_head.set_health_remaining(int(content_list[5]))

    await message.channel.send(print_hydra_list(hydra))


def print_hydra_list(hydra):
    hydra_string = 'hydras: \n'
    for head in hydra:
        hydra_string += str(head) + '\n'
    return hydra_string


client.run('')
