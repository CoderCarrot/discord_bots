import os
import discord
from discord.ext import commands

# Import the token from the .env folder
TOKEN = os.environ['DISCORD_TOKEN']

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
    # make sure the bot can't trigger itself
    if message.author == client.user:
        return

    # setup variables needed later
    # save the role "student" for multiple use later
    student_role = discord.utils.get(message.guild.roles, name='students')

    # start the dictionary for assigning pairs
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

    ######### This is the section that contains the pairing bot. #########

    # Check to see if the message is in the pairing channel to ensure the command doesn't misfire elsewhere.
    if message.channel.name == '🤝-lab-pairs' or message.channel.name == '🍐lab-pairs':
        # This section of the pairing bot gathers the list of students that will participating in lab.
        # This checks for the trigger in order to send the message for the students to react to. 
        if message.content == 'get students':
            # Send the message for the students to react to if they will be in lab for the day.
            await message.channel.send(
                f':pear: :pear: :pear: Get Paired! :pear: :pear: :pear:\n'
                f'{student_role.mention} React to this message with an emoji if you will be in lab today!'
            )
        
        # This section of the pairing bot grabs the student info from the lasts message via the reactions and makes the pairs.
        # This could just be another if statement, but I decided on elif since it's used in combo with the above.
        # This checks for the trigger in order to start the pairing process.
        elif message.content == 'make pairs':
            # Get a list of the last 2 messages so that we can grab the reactions to see which students will be in lab.
            messages = await message.channel.history(limit=2).flatten()
            # Get the pairing message the students reacted to.
            student_reactions = messages[1]
            # Initiate a set to put the student names into and prevent duplicates.
            students = set()
            # Loop through the reactions from the pairing message to grab the user information.
            for reaction in student_reactions.reactions:
                # Loop through each user for each reaction to add them to the set of students who will be in lab.
                async for user in reaction.users():
                    # Add each student who reacted to the last message to a set.
                    students.add(user)

            # Change the set into a list and split it in half to evenly distribute students in each lab. 
            m_students = list(students)[:round(len(students)/2)]
            r_students = list(students)[round(len(students)/2):]

            # Put the students from the lists into their respecitive labs/voice channels.
            for key in pairs['Malala'].keys():
                # Check if the list have more than 1 student to determine how many times to pop from the list.
                if len(m_students) > 1:
                    pairs['Malala'][key] = f'{m_students[-1].mention}, {m_students[-2].mention}'
                    # remove student from the list so it stops assigning when the list is empty.
                    m_students.pop()
                    m_students.pop()
                # Check if the list only has 1 student to only pop once.
                elif len(m_students) == 1:
                    pairs['Malala'][key] = f'{m_students[-1].mention}'
                    # remove student from the list so it stops assigning when the list is empty.
                    m_students.pop()
                # Stop assigning when the list is empty.
                else:
                    break
            for key in pairs['Ruth'].keys():
                # Check if the list have more than 1 student to determine how many times to pop from the list.
                if len(r_students) > 1:
                    pairs['Ruth'][key] = f'{r_students[-1].mention}, {r_students[-2].mention}'
                    # remove student from the list so it stops assigning when the list is empty.
                    r_students.pop()
                    r_students.pop()
                # Check if the list only has 1 student to only pop once.
                elif len(r_students) == 1:
                    pairs['Ruth'][key] = f'{r_students[-1].mention}'
                    # remove student from the list so it stops assigning when the list is empty.
                    r_students.pop()
                # Stop assigning when the list is empty.
                else:
                    break

            # Send the altered dictionary to the channel to show assigned pairs.
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

    ######### This is the section that contains the queue open/close bot. #########

    # Check to see if the message is in the queue channel to ensure the command doesn't misfire elsewhere.
    if message.channel.name == '🔨-lab-queue' or message.channel.name == '🧭lab-queue':
        # set the permission for the channel such that students can send messages if the queue is open.
        if message.content == 'queue.open()':
            await message.channel.set_permissions(student_role, send_messages=True)
        # set the permission for the channel such that students cannot send messages if the queue is closed.
        elif message.content == 'queue.close()':
            await message.channel.set_permissions(student_role, send_messages=False)

# run the client to connect to the server(s)
client.run(TOKEN)