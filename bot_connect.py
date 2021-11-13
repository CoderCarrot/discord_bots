import os
import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# represents the connection to Discord
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.reactions = True
client = discord.Client(intents=intents)


# print a statement confirming connection and client readiness
@client.event
async def on_ready():
    print('Hackbright Bot has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    pairs = {
        'Malala': {
            'A': '',
            'B': '',
            'C': '',
            'D': '',
            'E': '',
            'F': '',
            'G': '',
            'H': '',
        },
        'Ruth': {
            'A': '',
            'B': '',
            'C': '',
            'D': '',
            'E': '',
            'F': '',
            'G': '',
            'H': '',
        }
    }

    if message.channel.name == '🤝-lab-pairs' or message.channel.name == '🍐lab-pairs':
        if message.content == 'get students':
            # confirm_first = 'React to this message if this is the 1st time pairs are being created for this cohort.'
            # await message.channel.send(confirm_first)
            # pair_dict = {}
            # if message.channel.last_message.reactions:
            #     for member in discord.utils.get(message.guild.roles.members, name='students'):
            #         pair_dict[member.display_name] = 
            response = """:pear: :pear: :pear: Get Paired! :pear: :pear: :pear:
            students React to this message with an emoji if you will be in lab today!"""
            await message.channel.send(response)
        elif message.content == 'make pairs':
            messages = await message.channel.history(limit=2).flatten()
            student_reactions = messages[1]
            students = set()
            for reaction in student_reactions.reactions:
                async for user in reaction.users():
                    students.add(user)
            m_students = list(students)[:round(len(students)/2)]
            r_students = list(students)[round(len(students)/2):]
            for key in pairs['Malala'].keys():
                if len(m_students) > 1:
                    pairs['Malala'][key] = f'{m_students[-1].mention}, {m_students[-2].mention}'
                    m_students.pop()
                    m_students.pop()
                elif len(m_students) == 1:
                    pairs['Malala'][key] = f'{m_students[-1].mention}'
                    m_students.pop()
                else:
                    break
            for key in pairs['Ruth'].keys():
                if len(r_students) > 1:
                    pairs['Ruth'][key] = f'{r_students[-1].mention}, {r_students[-2].mention}'
                    r_students.pop()
                    r_students.pop()
                elif len(r_students) == 1:
                    pairs['Ruth'][key] = f'{r_students[-1].mention}'
                    r_students.pop()
                else:
                    break
            await message.channel.send(
                ":pear: :pear: :pear: Today's Pairs! :pear: :pear: :pear: \n"
                f'Malala\n'
                f"A: {pairs['Malala']['A']}\n"
                f"B: {pairs['Malala']['B']}\n"
                f"C: {pairs['Malala']['C']}\n"
                f"D: {pairs['Malala']['D']}\n"
                f"E: {pairs['Malala']['E']}\n"
                f"F: {pairs['Malala']['F']}\n"
                f"G: {pairs['Malala']['G']}\n"
                f"H: {pairs['Malala']['H']}\n"
                f'Ruth\n'
                f"A: {pairs['Ruth']['A']}\n"
                f"B: {pairs['Ruth']['B']}\n"
                f"C: {pairs['Ruth']['C']}\n"
                f"D: {pairs['Ruth']['D']}\n"
                f"E: {pairs['Ruth']['E']}\n"
                f"F: {pairs['Ruth']['F']}\n"
                f"G: {pairs['Ruth']['G']}\n"
                f"H: {pairs['Ruth']['H']}\n"
            )


    if message.channel.name == '🔨-lab-queue' or message.channel.name == '🧭lab-queue':
        if message.content == 'queue.open()':
            await message.channel.set_permissions(discord.utils.get(message.guild.roles, name='students'), send_messages=True)
        elif message.content == 'queue.close()':
            await message.channel.set_permissions(discord.utils.get(message.guild.roles, name='students'), send_messages=False)
        else:
            return


client.run(TOKEN)

###############################################################################
################################# Bot Code ####################################

# bot = commands.Bot(command_prefix='!')

# @bot.command(name='get_students')
# @commands.has_role('admin')
# async def get_students(ctx):
#     response = ':pear: :pear: :pear: \n students React to this message with an emoji if you will be in lab today!'
#     await ctx.send(response)

# @bot.command(name='make_pairs')
# @commands.has_role('admin')
# async def make_pairs(ctx):
#     messages = await ctx.channel.history(limit=3).flatten()
#     last_message = messages[1]
#     students = set()
#     for reaction in last_message.reactions:
#         async for user in reaction.users():
#             students.add(''.join(['@', str(user.id)]))
#     for student in students:
#         await ctx.send(student)

# bot.run(TOKEN)