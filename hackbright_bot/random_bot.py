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
    # make sure the bot can't trigger itself
    if message.author == client.user:
        return

    # setup variables needed later
    # save the role "student" for multiple use later
    student_role = discord.utils.get(message.guild.roles, name='students')

    # List names on channels per Lab
    channels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    # start the list for assigning pairs
    pairs = [":pear: :pear: :pear: Today's Pairs! :pear: :pear: :pear: \n", 'Malala\n']

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
        
        # This section of the pairing bot grabs the student info from the last message via the reactions and makes the pairs.
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

            # Put the students from the lists into their respecitive labs/voice channels.
            for index in range(len(channels)):
                # Check if the set has 3 students to determine if a 3-person group is needed.
                # Add the group to the pairs list by popping and adding the mention for the removed name.
                if len(students) == 3:
                    pairs.append(f'{channels[index]}: {students.pop().mention} | {students.pop().mention} | {students.pop().mention}\n')
                elif len(students) >= 2:
                    pairs.append(f'{channels[index]}: {students.pop().mention} | {students.pop().mention}\n')
                # Stop assigning when the list is empty.
                else:
                    break
            # Check if there are still students that need pairing after filling up Malala
            if len(students) != 0:
                # Add the name of the 2nd lab when more students need pairing.
                pairs.append('Ruth\n')
                for index in range(len(channels)):
                    # Check if the set has 3 students to determine if a 3-person group is needed.
                    # Add the group to the pairs list by popping and adding the mention for the removed name.
                    if len(students) == 3:
                        pairs.append(f'{channels[index]}: {students.pop().mention} | {students.pop().mention} | {students.pop().mention}\n')
                    elif len(students) >= 2:
                        pairs.append(f'{channels[index]}: {students.pop().mention} | {students.pop().mention}\n')
                    # Stop assigning when the list is empty.
                    else:
                        break

            # Send/print the altered list to the channel to show assigned pairs.
            await message.channel.send(''.join(pairs))

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