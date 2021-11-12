import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# represents the connection to Discord
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.reactions = True
client = discord.Client(intents=intents)


# print a statement confirming connection and client readiness
@client.event
async def on_ready():
    # loop through guilds to connect to the correct one
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} has connected to Discord!\n'
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

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

    if message.channel.name == '🤝-lab-pairs':
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
                    students.add(user.display_name)
            m_students = list(students)[:round(len(students)/2)]
            r_students = list(students)[round(len(students)/2):]
            for key in pairs['Malala'].keys():
                if len(m_students) > 1:
                    pairs['Malala'][key] = [m_students[-1], m_students[-2]]
                    m_students.pop()
                    m_students.pop()
                elif len(m_students) == 1:
                    pairs['Malala'][key] = m_students[-1]
                    m_students.pop()
                else:
                    break

                


            # Ask if this is the 1st time making pairs for this cohort
            # store info in a private message in the channel to read from and update accordingly
            # put message ID in public response to use for lookup
            
            response = """:pear: :pear: :pear: Today's Pairs! :pear: :pear: :pear:
            Malala
            A @pair[0][0] & @pair[0][1]
            B @pair[1][0] & @pair[1][1]
            C @pair[2][0] & @pair[2][1]
            D @pair[0][0] & @pair[0][1]
            E @pair[0][0] & @pair[0][1]
            F @pair[0][0] & @pair[0][1]
            G @pair[0][0] & @pair[0][1]
            H @pair[0][0] & @pair[0][1]
            Ruth
            A @student_1 & @student_2
            B @student_3 & @student_4
            C @student_5 & @student_6
            D @student_7 & @student_8
            E @student_9 & @student_10
            F @student_11 & @student_12
            G @student_13 & @student_14
            H @student_15 & @student_16"""


    if message.channel.name == '🔨-lab-queue':
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