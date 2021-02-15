import os
import discord
from dotenv import load_dotenv

PathOfTxt = os.path.dirname(__file__)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Hallo'):
        await message.channel.send('Hallo!')
    
    if message.content == '§Hilfe':
        await message.channel.send("""Liste der Befehle beginnend mit "§":
        -Hallo
        -Hausaufgabe für den {Tag} == {Hausaufgaben}
        -Was ist Hausaufgabe am {Tag}
        """)

    if "§Hausaufgabe für den" in message.content:
        Day = message.content.split("den ")[1]
        Day = Day.split(" ==")[0]
        Content = message.content.split("== ")[1]
        await message.channel.send('Tag = ' + Day + ', Hausaufgabe = ' + Content)
        f = open(os.path.join(PathOfTxt, "homework.txt"), "a")
        f.write(Day + " == " + Content)
        f.write("\n")
        f.close()
        await message.channel.send('Hausaufgaben gesetzt')

    if "§Was ist Hausaufgabe am" in message.content:
        Day = message.content.split("am ")[1]
        search = open(os.path.join(os.path.join(PathOfTxt, "homework.txt"), "homework.txt"))
        for line in search:
            if Day in line:
                Homework = line.split("==")[1]
                await message.channel.send("Am " + Day + " ist folgendes zu tun: " + Homework)

client.run(TOKEN)