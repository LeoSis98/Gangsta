from keep_alive import keep_alive
from fraseis import *
from gifs import *
import discord,random,os
from replit import db

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#test

#USER_COMMANDS_1

if "responding" not in db.keys():
  db["responding"] = True

def update_melos(melos_message):
  if "melos" in db.keys():
    melos = db["melos"]
    melos.append(melos_message)
    db["melos"] = melos
  else:
    db["melos"] = [melos_message]

def delete_melos(index):
  melos = db["melos"]
  if len(melos) > index:
    del melos[index]
  db["melos"] = melos 
  

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Valorant"))
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  #USER_COMMANDS_2

  msg = message.content

  fun.extend(db["melos"])
  if db["responding"]:
    if 'Gang' in message.content.lower() or 'gang' in message.content.lower() or client.user.mentioned_in(message):
      await message.reply(random.choice(fun))

  if msg.startswith("$n"):
    melos_message = msg.split("$n ",1)[1]
    update_melos(melos_message)
    await message.add_reaction('\N{THUMBS UP SIGN}')

  if msg.startswith("$del"):
    melos = []
    if "melos" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_melos(index)
      melos = db["melos"]
    await message.channel.send(melos) and await message.add_reaction('\N{THUMBS UP SIGN}')

  if msg.startswith("$list"):
    melos = []
    if "melos" in db.keys():
      melos = db["melos"]
    await message.channel.send(melos)
    
  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

  # FRASEIS STARTS HERE...
    
  #if 'Gang' in message.content.lower() or 'gang' in message.content.lower() or client.user.mentioned_in(message):
    #response1= random.choice(fun)
    #await message.reply(response1)

  if message.content.startswith('cold') or message.content.startswith('Cold'):
    response2= random.choice(cold)
    await message.channel.send(response2)

  if message.content.startswith('??????????') or message.content.startswith('??????????'):
    response3= random.choice(night)
    await message.channel.send(response3)

  if message.content.startswith('??????????') or message.content.startswith('??????????'):
    response4= random.choice(day)
    await message.channel.send(response4)

  if message.content.startswith('fact') or message.content.startswith('Fact'):
    response5= random.choice(gegon)
    await message.channel.send(response5)

  if message.content.startswith('trex') or message.content.startswith('Trex'):
    response6= random.choice(rex)
    await message.channel.send(response6)

  if message.content.startswith('ask') or message.content.startswith('Ask'):
    response7= random.choice(sof)
    await message.channel.send(response7)
    
  if message.content.startswith('????????') or message.content.startswith('????????') or message.content.startswith('geia') or message.content.startswith('????????????') or message.content.startswith('????????????'):
    response8= random.choice(hello)
    await message.channel.send(response8)

  # GIFS STARTS HERE...

  if message.content.startswith('????????') or message.content.startswith('????????') or message.content.startswith('????????') or message.content.startswith('????????'):
    ap1= random.choice(than)
    await message.channel.send(ap1)

  if message.content.startswith('????????') or message.content.startswith('????????') or message.content.startswith('????????') or message.content.startswith('????????'):
    ap2= random.choice(tol)
    await message.channel.send(ap2)

  if message.content.startswith('????????????') or message.content.startswith('????????????') or message.content.startswith('????????????') or message.content.startswith('????????????'):
    ap3= random.choice(raph)
    await message.channel.send(ap3)

  if message.content.startswith('????????????????') or message.content.startswith('??????????????????') or message.content.startswith('????????????????') or message.content.startswith('????????????????'):
    ap4= random.choice(xrist)
    await message.channel.send(ap4)

  if message.content.startswith('????????????') or message.content.startswith('????????????') or message.content.startswith('????????????') or message.content.startswith('????????????'):
    ap5= random.choice(ili)
    await message.channel.send(ap5)

  if message.content.startswith('????????????') or message.content.startswith('????????????') or message.content.startswith('????????????') or message.content.startswith('????????????'):
    ap6= random.choice(georg)
    await message.channel.send(ap6)

  if message.content.startswith('??????????????') or message.content.startswith('??????????????') or message.content.startswith('??????????????') or message.content.startswith('??????????????'):
    ap7= random.choice(leo)
    await message.channel.send(ap7)

  # THE END...


keep_alive()
client.run(os.getenv('token'))