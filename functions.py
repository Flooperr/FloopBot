import discord
import bard
shittonofdashes = '\n------------------------------------------\n'
DiscordNames = {'flooperrr': 'Ariel', 'flamingoish': 'Devin', 'lazyrus123': 'Cameron', 'notjewish': 'Grady', 'illegal_mexico21': 'Erick', 'yizzzz69': 'Yiz'}
help1 = discord.Embed(
        title="Help Menu",
        description= (f'\n**Floop Help Utility**: Brings Menu of Utility Commands{shittonofdashes}**Floop Help Fun**: Brings Menu of Fun Commands'),
        color=discord.Color.green()
            )
help1.set_author(name="FloopBot")
help1.set_footer(text="Flooper#4502")

help2 = discord.Embed(
        title="Utility Menu",
        description= (f'\n**Floop Ping**: Pings message with the response time{shittonofdashes}**Floop Ask [question]:** Ask FloopBot a question using BARD{shittonofdashes}**Floop Clear [digit]**: Clear amount of messages'),
        color=discord.Color.green()
            )
help2.set_author(name="FloopBot")
help2.set_footer(text="Flooper#4502")

help3 = discord.Embed(
        title="Fun Menu",
        description= (f'\n**Floop Die**: no u + your name (if ur special){shittonofdashes}**Floop Flopper**: Flopper gif goes hard '),
        color=discord.Color.green()
            )
help3.set_author(name="FloopBot")
help3.set_footer(text="Flooper#4502")
                

def setCustomPrefix(prefix = '?'):
    return prefix

CustomPrefix = setCustomPrefix('floop ')

def PrefixMessageCheck(prefix, content):
    messagecheck = ''
    for i in range(len(prefix)):
        if prefix[i].lower() == content[i].lower():
            messagecheck += prefix[i]
        else:
            break
    return messagecheck
    

async def send_help(message, content):
    checkmessage = content[len('help '):].lower()
    print(checkmessage)
    if checkmessage == 'utility':
        print('hello')
        await message.channel.send(embed=help2)
    elif checkmessage == 'fun':
        await message.channel.send(embed=help3)
    else:
        await message.channel.send(embed=help1)

async def nou(message):
    if message.author.name in DiscordNames:
        await message.channel.send(f'no u {DiscordNames[message.author.name]}')
        await message.channel.send('https://tenor.com/view/ltg-low-tier-god-yskysn-ltg-thunder-thunder-gif-23523876')
    else:
        await message.channel.send('no u')

async def bardresponse(message, content1):
    if message.author.name in DiscordNames:
        answer = bard.answer(content1[3:],  DiscordNames[message.author.name])
        if 'Response Error' in answer:
            await message.channel.send('```Google is Dumb, I need a cookie```')
        else:
            await message.channel.send(f'```{answer}```')
    else:
        answer = bard.answer(content1[3:], message.author.name)
        if 'Response Error' in answer:
            await message.channel.send('```Google is Dumb, I need a cookie```')
        else:
            await message.channel.send(f'```{answer}```')


async def clearmessages(message, content):
    newamount = int(content[len('clear '):])
    print(newamount)
    await message.channel.purge(limit=newamount + 1)


async def play(message, query):
    # Check if the user is in a voice channel
    if not message.author.voice:
        await message.channel.send("You are not in a voice channel.")
        return

    channel = message.author.voice.channel
    voice_client = await channel.connect()

    source = discord.FFmpegPCMAudio("your_downloaded_mp3.mp3")
    voice_client.play(source)

