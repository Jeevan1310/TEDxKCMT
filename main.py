import discord
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True
client=discord.Client(intents=intents)


@client.event #presence and online
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name="TEDx Server"))
  print('We have logged in as {0.user}'.format(client))

@client.event #for messaging purpose
async def on_message(message):
  channel=message.channel


  if message.author == client.user:
    return
  msg = message.content

  if msg.startswith('hello'):
    await channel.send(f'Hello! {message.author.mention} ')
    print(msg)

  if msg.startswith('=help'):
    embed = discord.Embed(title=f"Hello User", description=">>> **Thank you for calling me If you need any help please contact <@&878335486429630505> **", colour=0x87CEEB)
    await channel.send(embed=embed)
    print('User used help command')


  if msg.startswith('=organiser'):
    await channel.send('https://user-images.githubusercontent.com/81223681/151385150-e79601f3-f2c3-495a-b902-cfacbd4c616b.jpg',delete_after=30.0)



  if msg.startswith('=tedxkcmt'):
    embed = discord.Embed(title=f"TEDxKCMT", description=" **This is the story of a dream brought to life. A story that will be remembered and cherished forever. In 2019, we officially became TEDxKCMT (first license approval). It was never easy; all the struggles, failures, rejections and hard work granted us this title. In the same year conducting TEDxKCMTWomen within a short notice was yet another achievement for the team. Forming a TEDx team was a small seed planted in our minds. Today, it has grown into a big tree with beautiful branches. It is giving warmth and support to the young ignited minds of KCMT.Sharing our journey so far, this is a tale known to some, new for others. It is also a fascinating chapter in the story of our lives.This whole story is being shared, continuing with each season to come, changing with perspectives and add-ons .With strong determination and never-dying spirit, we march forward to spread ideas that matter. We bring change and we become the change this world needs. To know more about TEDxKCMT goto-https://tedxkcmt.com/**", colour=0x87CEEB)
    embed.set_image(url="https://user-images.githubusercontent.com/81223681/152631380-e8378398-5f93-4d0e-acca-e0f68cd2d12d.jpg")
    await channel.send(embed=embed , delete_after=15.0)
    reaction_channel=client.get_channel(938100802831134740)
    await reaction_channel.send('Bot performed and sucessfully deleted message')
    await msg.delete()
    print('User used know command')

  if msg.startswith('=website'):
    embed = discord.Embed(title=f"WEBSITE : https://tedxkcmt.com/", description="TEDxKCMT Official Website", colour=0x89CEEB)
    await channel.send(embed=embed)
    print('User used web command')

  if msg.startswith('=instagram'):
    embed = discord.Embed(title=f"INSTAGRAM : https://www.instagram.com/tedxkcmtofficial/", description="TEDxKCMT Official Instagram Handle", colour=0x89CEEB)
    await channel.send(embed=embed)
    print('User used insta command')
  
  if msg.startswith('=commands'):
    embed1 = discord.Embed(title=f"Bot Commands 1) =help", description="**This Commands helps you to provide support from Server Handler in case of emergency**",colour=0x89CEEB)
    embed2 = discord.Embed(title=f"Bot Commands 2) =tedxkcmt", description="**This Commands helps you to provide more info about TEDxKCMT that includes a short history of our organisation**",colour=0x89CEEB)
    embed3 = discord.Embed(title=f"Bot Commands 3) =instagram",
    description="**This command helps you to provide details about our insta handle if you you want know any more go and check there**",colour=0x89CEEB)
    await channel.send(embed=embed1,delete_after=60.0)
    await channel.send(embed=embed2,delete_after=60.0)
    await channel.send(embed=embed3,delete_after=60.0)
    print('User used  command')
  else:
    print('used else condition')
  

  #role function 
  if message.content.startswith(f'#intro-tedx'):
    user=message.author
    role=discord.utils.get(user.guild.roles,name="NOVICE")
    await user.add_roles(role)
    await message.add_reaction('\U00002705')
    reaction_channel = client.get_channel(938100802831134740)
    await reaction_channel.send(f'{user.mention} has posted a introduction and given the role <@&936284676954411050> Moderators please verify the activity')
  else:
    print('some people used other words and its solved')

@client.event #welcome message
async def on_member_join(member):
  guild = client.get_guild(878039808713293845)
  channel = guild.get_channel(935150094691500103)
  await channel.send(f'Welcome to the server {member.mention}  :tada:')
  print('new user joined')
  if not channel:
    return
  



keep_alive()  
client.run(os.getenv('TEDx'))