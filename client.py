import random
import asyncio
import discord
import os
from dotenv import load_dotenv, find_dotenv

from discord.ext import commands

client = commands.Bot(command_prefix="&", case_insensitive=True)
client.remove_command('help')
token = load_dotenv(find_dotenv())
token = os.environ.get('bot_token')


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="&help"))

@client.command(name='help')
async def help(ctx):
    if ctx.author.bot or ctx.guild is None:
        return
    await ctx.send(" Just a hand cricket bot :) \n&start - To start a match \nFollow along to complete the match \n(There will be glitches) ")

@client.command(name='start')
async def game(ctx):
    if ctx.author.bot or ctx.guild is None:
        return
    
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
    
    while True:  
        try:
            await ctx.send(f"{ctx.author}, Choose a number(1-10) and odd or even (For eg: 2 odd, 5 even) : ")
            msg1 = await client.wait_for('message', timeout=30, check=check)
            
            if msg1.author == ctx.author:
                ch = random.randint(1,10)
                inp = msg1.content.split()
                
                start = True
                
                if int(inp[0]) <= 10 and int(inp[0]) > 0:
                    if inp[1].lower() == "even":
                        
                        if (ch + int(inp[0])) % 2 == 0:
                            await ctx.send(f"{ctx.author}, I chose {ch} \nYou win")
                            start = False
                            break
                        
                        elif (ch + int(inp[0])) % 2 != 0:
                            await ctx.send(f"{ctx.author}, I chose {ch} \nYou lose")
                            break
                    
                    if inp[1].lower() == "odd":
                        
                        if (ch + int(inp[0])) % 2 != 0:
                            await ctx.send(f"{ctx.author}, I chose {ch} \nYou win")
                            start = False
                            break
                        
                        elif (ch + int(inp[0])) % 2 == 0:
                            await ctx.send(f"{ctx.author}, I chose {ch} \nYou lose")
                            break
                
                else:
                    pass
            
            else:
                pass
        
        except asyncio.TimeoutError:
            await ctx.send(f"{ctx.author}, You took too much time.")
            break
        
        except:
            await ctx.send(f"{ctx.author}, Choose properly.")
    
    ch = random.choice(['Bat','Bowl'])
    await ctx.send(f"{ctx.author}, Rules: Only 1-6 allowed. I will send msg after you send. If you want to quit send 0.")
    
    if start == True and ch.lower() == "bowl":
        await ctx.send(f"{ctx.author}, I will {ch}. Send your msg for first ball")
        xyz = True
        score_h = 0
        score_b = 0
        
        while xyz:
            try:
                msg2 = await client.wait_for('message', check=check)
                
                if msg2.author == ctx.author and int(msg2.content) == 0:
                    await ctx.send(f"{ctx.author}, Bye")
                    xyz = False
                    break
                
                elif msg2.author == ctx.author and int(msg2.content) < 7 and int(msg2.content) > 0:
                    choice = random.randint(1,6)
                    
                    if int(msg2.content) == choice:
                        await ctx.send(f"Out!!!!!")
                        await ctx.send(f"{ctx.author}, I will bat now. Send your msg for first ball")
                        
                        while True:
                            try:
                                msg3 = await client.wait_for('message', timeout=30, check=check)
                                
                                if msg3.author == ctx.author and int(msg3.content) == 0:
                                    await ctx.send(f"{ctx.author}, Bye")
                                    xyz = False
                                    break
                                
                                if msg3.author == ctx.author and int(msg3.content) < 7 and int(msg3.content) > 0:
                                    choice1 = random.randint(1,6)
                                    score_b += choice1
                                    
                                    if score_b > score_h:
                                        await ctx.send(f"{ctx.author}, You chose {msg3.content}. I chose {choice1}.")
                                        await ctx.send(f"{ctx.author}, You Win!! :) \nFinal Score: \nHuman: {score_h} \nBot: {score_b} \nThanks for playing :)")
                                        xyz = False
                                        break
                                    
                                    elif (score_b - choice1) <= score_h:
                                        
                                        if int(msg3.content) == choice1:
                                            
                                            if (score_b - choice1) == score_h:
                                                await ctx.send(f"{ctx.author}, LOL its draw. Lets settle this with odd or even")
                                                await ctx.send(f"{ctx.author}, Choose a number(1-10) and odd or even (For eg: 2 odd, 5 even) : ")
                                                msg4 = await client.wait_for('message', check=check)
                                                
                                                if msg4.author == ctx.author:
                                                    ch = random.randint(1,10)
                                                    inp = msg1.content.split()
                                                                                                    
                                                    if int(inp[0]) <= 10 and int(inp[0]) > 0:
                                                        if inp[1].lower() == "even":
                                                            
                                                            if (ch + int(inp[0])) % 2 == 0:
                                                                await ctx.send(f"{ctx.author}, I chose {ch} \nYou win")
                                                                xyz = False
                                                                break
                                                            
                                                            else:
                                                                await ctx.send(f"{ctx.author}, I chose {ch} \nYou lose")
                                                                xyz = False
                                                                break
                                                        
                                                        else:
                                                            
                                                            if (ch + int(inp[0])) % 2 != 0:
                                                                await ctx.send(f"{ctx.author}, I chose {ch} \nYou win")
                                                                xyz = False
                                                                break
                                                            
                                                            else:
                                                                await ctx.send(f"{ctx.author}, I chose {ch} \nYou lose")
                                                                xyz = False
                                                                break
                                                    
                                                    else:
                                                        pass
                                                else:
                                                    pass

                                            elif (score_b - choice1) < score_h:
                                                await ctx.send(f"{ctx.author}, You chose {msg3.content}. I chose {choice1}.")
                                                await ctx.send(f"Out :( \nFinal Score: \nHuman: {score_h} \nBot: {score_b - choice1} \nThanks for playing :)")
                                                xyz = False
                                                break
                                        
                                        else:
                                            await ctx.send(f"{ctx.author}, You chose {msg3.content}. I chose {choice1}. \nScore: \nHuman: {score_h} \nBot : {score_b}")
                            
                                elif msg3.author != ctx.author:
                                    continue
                            
                                else:
                                    if not msg3.author.bot: await ctx.send(f"{ctx.author}, Enter correct number")
                    
                            except asyncio.TimeoutError:
                                await ctx.send(f"{ctx.author}, You took too much time.")
                                xyz = False
                                break
                            except:
                                pass
                    
                    else:
                        score_h += int(msg2.content)
                        await ctx.send(f"{ctx.author}, You chose {msg2.content}. I chose {choice}. \nScore: \nHuman: {score_h} \nBot : {score_b}")
                
                elif msg2.author != ctx.author:
                    continue
                
                else:
                    if not msg2.author.bot: await ctx.send("Enter correct number")   
            
            except asyncio.TimeoutError:
                await ctx.send(f"{ctx.author}, You took too much time.")
                xyz = False
                break
            except:
                pass
    
    if start == True and ch.lower() == "bat":
        await ctx.send(f"{ctx.author}, I will {ch}. Send your msg for first ball")
        score_h = 0
        score_b = 0
        xyz = True
        
        while xyz:
            try:
                msg2 = await client.wait_for('message', check=check)
                
                if msg2.author == ctx.author and int(msg2.content) == 0:
                    await ctx.send("Bye")
                    xyz = False
                    break
                
                elif msg2.author == ctx.author and int(msg2.content) < 7 and int(msg2.content) > 0:
                    choice = random.randint(1,6)
                    
                    if int(msg2.content) == choice:
                        await ctx.send(f"Out!!!!!")
                        await ctx.send(f"{ctx.author}, I will bowl now. Send your msg for first ball")
                        
                        while True:
                            try:
                                msg3 = await client.wait_for('message', check=check)
                                
                                if msg3.author == ctx.author and int(msg3.content) == 0:
                                    await ctx.send("Bye")
                                    xyz = False
                                    break
                                
                                if msg3.author == ctx.author and int(msg3.content) < 7 and int(msg3.content) > 0:
                                    choice1 = random.randint(1,6)
                                    score_h += int(msg3.content)
                                                                    
                                    if score_b >= (score_h - int(msg3.content)):
                                        
                                        if int(msg3.content) == choice1:

                                            if score_b == (score_h - int(msg3.content)):
                                                await ctx.send(f"{ctx.author}, LOL its draw. Lets settle this with odd or even")
                                                await ctx.send(f"{ctx.author}, Choose a number(1-10) and odd or even (For eg: 2 odd, 5 even) : ")
                                                msg4 = await client.wait_for('message', check=check)
                                                
                                                if msg4.author == ctx.author:
                                                    ch = random.randint(1,10)
                                                    inp = msg1.content.split()
                                                                                                    
                                                    if int(inp[0]) <= 10 and int(inp[0]) > 0:
                                                        if inp[1].lower() == "even":
                                                            
                                                            if (ch + int(inp[0])) % 2 == 0:
                                                                await ctx.send(f"{ctx.author}, I chose {ch} \nYou win")
                                                                xyz = False
                                                                break
                                                            
                                                            else:
                                                                await ctx.send(f"{ctx.author}, I chose {ch} \nYou lose")
                                                                xyz = False
                                                                break
                                                        
                                                        else:
                                                            if (ch + int(inp[0])) % 2 != 0:
                                                                await ctx.send(f"{ctx.author}, I chose {ch} \nYou win")
                                                                xyz = False
                                                                break
                                                            
                                                            else:
                                                                await ctx.send(f"{ctx.author}, I chose {ch} \nYou lose")
                                                                xyz = False
                                                                break
    
                                                    else:
                                                        pass
                                                else:
                                                    pass

                                            elif score_b > (score_h - int(msg3.content)):
                                                await ctx.send(f"{ctx.author}, You chose {msg3.content}. I chose {choice1}.")
                                                await ctx.send(f"Out!!! \nFinal Score: \nBot: {score_b} \nHuman: {score_h - int(msg3.content)} \nThanks for playing :)")
                                                xyz = False
                                                break
                                                                            
                                        else:
                                            await ctx.send(f"{ctx.author}, You chose {msg3.content}. I chose {choice1}. \nScore: \nHuman: {score_h} \nBot : {score_b}")
                                    
                                    elif score_b < score_h:
                                        await ctx.send(f"{ctx.author}, You chose {msg3.content}. I chose {choice1}.")
                                        await ctx.send(f"{ctx.author}, Win!! :) \nFinal Score: \nBot: {score_b} \nHuman: {score_h}\nThanks for playing :)")
                                        xyz = False
                                        break
                                
                                elif msg3.author != ctx.author:
                                    continue
                                
                                else:
                                    if not msg3.author.bot: await ctx.send(f"{ctx.author}, Enter correct number")

                            except asyncio.TimeoutError:
                                await ctx.send(f"{ctx.author}, You took too much time.")
                                xyz = False
                                break
                            except:
                                pass
                    
                    else:
                        score_b += choice
                        await ctx.send(f"{ctx.author}, You chose {msg2.content}. I chose {choice}. \nScore: \nHuman: {score_h} \nBot : {score_b}")
                
                elif msg2.author != ctx.author:
                    continue
                
                else:
                    if not msg2.author.bot: await ctx.send(f"{ctx.author}, Enter correct number")
            
            except asyncio.TimeoutError:
                await ctx.send(f"{ctx.author}, You took too much time.")
                xyz = False
                break
            except:
                pass
    
    elif start == False:
        await ctx.send("1. Bat \n2. Bowl")
        cho = (await client.wait_for('message', check=check)).content
        
        if cho == "0":
            await ctx.send("Bye")
        
        elif cho == "1":
            await ctx.send(f"{ctx.author}, I will bowl. Send your msg for first ball")
            score_h = 0
            score_b = 0
            xyz = True
            
            while xyz:
                try:
                    msg2 = await client.wait_for('message', check=check)
                    
                    if msg2.author == ctx.author and int(msg2.content) == 0:
                        await ctx.send(f"{ctx.author}, Bye")
                        xyz = False
                        break
                    
                    elif msg2.author == ctx.author and int(msg2.content) < 7 and int(msg2.content) > 0:
                        choice = random.randint(1,6)
                        
                        if int(msg2.content) == choice:
                            await ctx.send("Out!!!!!")
                            await ctx.send(f"{ctx.author}, I will bat now. Send your msg for first ball")
                            
                            while True:
                                try:
                                    msg3 = await client.wait_for('message', check=check)
                                    
                                    if msg3.author == ctx.author and int(msg3.content) == 0:
                                        await ctx.send(f"{ctx.author}, Bye")
                                        xyz = False
                                        break
                                    
                                    elif msg3.author == ctx.author and int(msg3.content) < 7 and int(msg3.content) > 0:
                                        choice1 = random.randint(1,6)
                                        score_b += choice1
                                        
                                        if score_b > score_h:
                                            await ctx.send(f"{ctx.author}, You chose {msg3.content}. I chose {choice1}.")
                                            await ctx.send(f"{ctx.author}, You Win!! :) \nFinal Score: \nHuman: {score_h} \nBot:{score_b} \nThanks for playing :)")
                                            xyz = False
                                            break
                                        
                                        elif (score_b - choice1) <= score_h:
                                            
                                            if int(msg3.content) == choice1:

                                                if (score_b - choice1) == score_h:
                                                    await ctx.send(f"{ctx.author}, LOL its draw. Lets settle this with odd or even")
                                                    await ctx.send(f"{ctx.author}, Choose a number(1-10) and odd or even (For eg: 2 odd, 5 even) : ")
                                                    msg4 = await client.wait_for('message', check=check)
                                                    
                                                    if msg4.author == ctx.author:
                                                        ch = random.randint(1,10)
                                                        inp = msg1.content.split()
                                                                                                        
                                                        if int(inp[0]) <= 10 and int(inp[0]) > 0:
                                                            if inp[1].lower() == "even":
                                                                
                                                                if (ch + int(inp[0])) % 2 == 0:
                                                                    await ctx.send(f"{ctx.author}, I chose {ch} \nYou win")
                                                                    xyz = False
                                                                    break
                                                                
                                                                else:
                                                                    await ctx.send(f"{ctx.author}, I chose {ch} \nYou lose")
                                                                    xyz = False
                                                                    break
                                                            
                                                            else:
                                                                
                                                                if (ch + int(inp[0])) % 2 != 0:
                                                                    await ctx.send(f"{ctx.author}, I chose {ch} \nYou win")
                                                                    xyz = False
                                                                    break
                                                                
                                                                else:
                                                                    await ctx.send(f"{ctx.author}, I chose {ch} \nYou lose")
                                                                    xyz = False
                                                                    break
                                                        
                                                        else:
                                                            pass
                                                    else:
                                                        pass
                                                
                                                elif (score_b - choice1) < score_h:
                                                    await ctx.send(f"{ctx.author}, You chose {msg3.content}. I chose {choice1}.")
                                                    await ctx.send(f"Out :(  \nFinal Score: \nHuman: {score_h} \nBot:{(score_b - choice1)} \nThanks for playing :)")
                                                    xyz = False
                                                    break
                                            
                                            else:
                                                await ctx.send(f"{ctx.author}, You chose {msg3.content}. I chose {choice1}. \nScore: \nHuman: {score_h} \nBot : {score_b}")
                                    
                                    elif msg3.author != ctx.author:
                                        continue
                                    
                                    else:
                                        if not msg3.author.bot: await ctx.send(f"{ctx.author}, Enter correct number")
                        
                                except asyncio.TimeoutError:
                                    await ctx.send(f"{ctx.author}, You took too much time.")
                                    xyz = False
                                    break
                                except:
                                    pass

                        else:
                            score_h += int(msg2.content)
                            await ctx.send(f"{ctx.author}, You chose {msg2.content}. I chose {choice}. \nScore: \nHuman: {score_h} \nBot : {score_b}")
                    
                    elif msg2.author != ctx.author:
                        continue
                    
                    else:
                        if not msg2.author.bot: await ctx.send(f"{ctx.author}, Enter correct number")
                
                except asyncio.TimeoutError:
                    await ctx.send(f"{ctx.author}, You took too much time.")
                    xyz = False
                    break
                except:
                    pass
        
        elif cho == "2":
            await ctx.send(f"{ctx.author}, I will bat. Send your msg for first ball")
            score_h = 0
            score_b = 0
            xyz = True
            
            while xyz:
                try:
                    msg2 = await client.wait_for('message', check=check)
                    
                    if msg2.author == ctx.author and int(msg2.content) == 0:
                        await ctx.send(f"{ctx.author}, Bye")
                        xyz = False
                        break
                    
                    elif msg2.author == ctx.author and int(msg2.content) < 7 and int(msg2.content) > 0:
                        choice = random.randint(1,6)
                        
                        if int(msg2.content) == choice:
                            await ctx.send(f"Out!!!!!")
                            await ctx.send(f"{ctx.author}, I will bowl now. Send your msg for first ball")
                            
                            while True:
                                try:
                                    msg3 = await client.wait_for('message', check=check)
                                    
                                    if msg2.author == ctx.author and int(msg2.content) == 0:
                                        await ctx.send(f"{ctx.author}, Bye")
                                        xyz = False
                                        break
                                    
                                    if msg3.author == ctx.author and int(msg3.content) < 7 and int(msg3.content) > 0:
                                        choice1 = random.randint(1,6)
                                        score_h += int(msg3.content)
                                        
                                        if score_b < score_h:
                                            await ctx.send(f"{ctx.author}, You chose {msg3.content}. I chose {choice1}.")
                                            await ctx.send(f"{ctx.author}, You Win!! :) \nFinal Score: \nBot: {score_b} \nHuman: {score_h} \nThanks for playing :)")
                                            xyz = False
                                            break
                                        
                                        elif score_b >= (score_h - int(msg3.content)):
                                            
                                            if int(msg3.content) == choice1:

                                                if score_b == (score_h - int(msg3.content)):
                                                    await ctx.send(f"{ctx.author}, LOL its draw. Lets settle this with odd or even")
                                                    await ctx.send(f"{ctx.author}, Choose a number(1-10) and odd or even (For eg: 2 odd, 5 even) : ")
                                                    msg4 = await client.wait_for('message', check=check)
                                                    
                                                    if msg4.author == ctx.author:
                                                        ch = random.randint(1,10)
                                                        inp = msg1.content.split()
                                                                                                        
                                                        if int(inp[0]) <= 10 and int(inp[0]) > 0:
                                                            if inp[1].lower() == "even":
                                                                
                                                                if (ch + int(inp[0])) % 2 == 0:
                                                                    await ctx.send(f"{ctx.author}, I chose {ch} \nYou win")
                                                                    xyz = False
                                                                    break
                                                                
                                                                else:
                                                                    await ctx.send(f"{ctx.author}, I chose {ch} \nYou lose")
                                                                    xyz = False
                                                                    break
                                                            
                                                            else:
                                                                
                                                                if (ch + int(inp[0])) % 2 != 0:
                                                                    await ctx.send(f"{ctx.author}, I chose {ch} \nYou win")
                                                                    xyz = False
                                                                    break
                                                                
                                                                else:
                                                                    await ctx.send(f"{ctx.author}, I chose {ch} \nYou lose")
                                                                    xyz = False
                                                                    break
                                                        
                                                        else:
                                                            pass
                                                    else:
                                                        pass
                                                
                                                elif score_b > (score_h - int(msg3.content)):
                                                    await ctx.send(f"{ctx.author}, You chose {msg3.content}. I chose {choice1}.")
                                                    await ctx.send(f"Out!!!!! \nFinal Score: \nBot: {score_b} \nHuman: {(score_h - int(msg3.content))} \nThanks for playing :)")
                                                    xyz = False
                                                    break
                                                
                                            else:
                                                await ctx.send(f"{ctx.author}, You chose {msg3.content}. I chose {choice1}. \nScore: \nHuman: {score_h} \nBot : {score_b}")
                                    
                                    elif msg3.author != ctx.author:
                                        continue
                                    
                                    else:
                                        if not msg3.author.bot: await ctx.send(f"{ctx.author}, Enter correct number")
                                
                                except asyncio.TimeoutError:
                                    await ctx.send(f"{ctx.author}, You took too much time.")
                                    xyz = False
                                    break
                                except:
                                    pass

                        else:
                            score_b += choice
                            await ctx.send(f"{ctx.author}, You chose {msg2.content}. I chose {choice}. \nScore: \nHuman: {score_h} \nBot : {score_b}")
                
                    elif msg2.author != ctx.author:
                        continue
                
                    else:
                        if not msg2.author.bot: await ctx.send(f"{ctx.author}, Enter correct number")
                
                except asyncio.TimeoutError:
                    await ctx.send(f"{ctx.author}, You took too much time.")
                    xyz = False
                    break
                except:
                    pass


client.run(token)