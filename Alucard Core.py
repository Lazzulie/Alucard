# Discord Bot?!?!?! by Time Parabola
# Do note that I suck at Python
# so development will be infrequent at best

import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
	print("Starting with name: " + bot.user.name)

# Main Command Checker
@bot.event
async def on_message(message): 
	msg = message.content
	if msg[:1] == "!": # Checks for the command prefix
		print("Command Prefix Located")
		if message.content.upper().startswith("!PING"):
			username = message.author.mention
			await bot.send_message(message.channel, "{} Pong!".format(username))
		elif message.content.upper().startswith("!ASK"):
			num = random.randint(1, 4)
			
			response = { # Makeshift switch statement using a dictionary
				1: "Yes, definitely.",
				2: "No, absolutely not!", 
				3: "Well, it's a possibility",
				4: "The answer to that is hard to know"
			}
			await bot.send_message(message.channel, response.get(num, "Not sure about that one."))
		elif message.content.upper().startswith("!HELP"):
			await bot.send_message(message.channel, "**Commands:** \n\n!ping - Bot messages 'Pong!'.\n!ask - Answers a yes or no question.\n!help - I think you know what this one does...")
		else:
			await bot.send_message(message.channel, "Error: Command not found. Trying use !help.")
		

bot.run(INSERT_TOKEN_HERE) # Note: Do not give another person your token, they will have access to your bot's account. For this reason, my token is not included.