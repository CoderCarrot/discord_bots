import os
import random
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = os.getenv('DISCORD_GUILD')

# represents the connection to Discord
bot = commands.Bot(command_prefix='!')

# print a statement confirming connection and client readiness
# @client.event
# async def on_ready():
    # loop trough guilds to connect to the correct one
    # for guild in client.guilds:
    #     if guild.name == GUILD:
    #         break

    # print(
    #     f'{client.user} has connected to Discord!\n'
    #     f'{client.user} is connected to the following guild:\n'
    #     f'{guild.name}(id: {guild.id})'
    # )

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
    
#     if message.content == 'get students':
#         response = ':pear: :pear: :pear: \n @students React to this message with an emoji if you will be in lab today!'
#         await message.channel.send(response)

@bot.command(name='get_students')
@commands.has_role('admin')
async def get_students(ctx):
    response = ':pear: :pear: :pear: \n students React to this message with an emoji if you will be in lab today!'
    await ctx.send(response)

@bot.command(name='make_pairs')
@commands.has_role('admin')
async def make_pairs(ctx):
    messages = await ctx.channel.history(limit=3).flatten()
    last_message = messages[1]
    students = set()
    for reaction in last_message.reactions:
        async for user in reaction.users():
            students.add(''.join(['@', str(user.id)]))
    for student in students:
        await ctx.send(student)

bot.run(TOKEN)