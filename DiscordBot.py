import discord
import string
import functions
import bard

DiscordNames = {'flooperrr': 'Ariel', 'flamingoish': 'Devin', 'lazyrus123': 'Cameron', 'notjewish': 'Grady', 'illegal_mexico21': 'Erick', 'yizzzz69': 'Yiz'}
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="floop help"))
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(f'{message.content} in {message.channel} by {message.author}')
### commandsssss
    if message.author != client.user:
        if functions.PrefixMessageCheck(functions.CustomPrefix, message.content) == functions.CustomPrefix:
            content = message.content[len(functions.CustomPrefix):].lower()
            if 'help' in content:
                await functions.send_help(message, content)
            if content == 'ping':
                await message.channel.send(f'Pong, {round(client.latency * 1000, 2)} ms')
            if content == 'die':
                await functions.nou(message)
            if 'ask' in content:
                await functions.bardresponse(message, content)
            if 'clear' in content:
                await functions.clearmessages(message, content)

            if content == 'flopper':
                await message.channel.send('https://media.discordapp.net/attachments/984566553246834778/1165561177003270154/caption-7.gif?width=260&height=441')
            if content == 'join':
                if message.guild.voice_client:
                    await message.channel.send("I'm already in a voice channel")
                else:
                    await message.channel.send(f'`Joining {message.author.voice.channel}...`')
                    channel = message.author.voice.channel
                    voice_client = await channel.connect()
            if content == 'leave':
                if message.guild.voice_client:
                    await message.guild.voice_client.disconnect()
                else:
                    await message.channel.send("I'm not in a voice channel.")

client.run('DISCORD TOKEN HERE')

