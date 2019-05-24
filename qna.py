import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print('login')
    print(client.user.name)
    print(client.user.id)
    print('------------------')
    game = discord.Game('건의 확인중')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith('!문의') and not message.content.startswith("!문의확인"):
        content = message.content[4:]
        author = message.author
        file = open("문의.txt", "r")
        c = file.read()
        file.close()
        file = open("문의.txt", "w")
        file.write(c + "\n" + author.name + "(" + str(author.id) + ") : " + content)
        file.close()
        await message.delete()
        await message.channel.send(author.name + "님의 문의 접수가 완료되었습니다.")

    if message.content.startswith("!문의확인") and (message.author.id == 463243589703434250 or message.author.id == 366221416967700483):
        file = open("문의.txt", "r")
        c = file.read()
        await message.channel.send(c)
        
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
