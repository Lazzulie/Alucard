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
		print("Command Entered: {}".format(msg))
		if msg.upper().startswith("!PING"):
			username = message.author.mention
			await bot.send_message(message.channel, "{} Pong!".format(username))
		elif msg.upper().startswith("!ASK"):
			num = random.randint(1, 7)
			
			response = { # Makeshift switch statement using a dictionary
				1: "Yes, definitely.",
				2: "No, absolutely not!", 
				3: "Well, it's a possibility.",
				4: "The answer to that is hard to know.",
				5: "There is a 50/50 chance.",
				6: "I'd say so, yeah.",
				7: "Probably not."
			}
			
			await bot.send_message(message.channel, response.get(num, "Not sure about that one."))
		elif msg.upper().startswith("!HELP"):
			space = "\u200b" # Escape character that equats to a blank line, essentially allows me to set an element to be invisible so I can add blanks lines.

			embed=discord.Embed(title="Help Menu", description="Commands:", color=0x113dbd)
			embed.add_field(name=space, value=space, inline = False)
			embed.add_field(name="!ask", value="Answers a yes or no question.\n", inline=False)
			embed.add_field(name=space, value=space, inline = False)
			embed.add_field(name="!help", value="Lists all available commands.\n", inline=False)
			embed.add_field(name=space, value=space, inline = False)
			embed.add_field(name="!ping", value="Bot responds with 'Pong!'.\n", inline=False)
			embed.add_field(name=space, value=space, inline = False)
			embed.add_field(name="!report (username)", value="Sends a report to a staff-only channel.", inline=False)
			embed.add_field(name=space, value=space, inline = False)
			embed.add_field(name="!support", value="Sends a link to the support google form.", inline = False)
			embed.set_footer(text="Bot created by NinjaMouse")

			try:
				await bot.send_message(message.author, embed=embed)
			except discord.errors.Forbidden:
				await bot.send_message(message.channel, "Error: Unable to send in PMs. Sending in text channel.")
				await bot.send_message(message.channel, embed=embed)

		elif msg.upper()[:7] == "!REPORT":
			print("Report from a user")
			reporter = message.author.display_name + " ({})".format(message.author.name + "#" + message.author.discriminator)
			report = "----------------------------------------\n**Report from {}:**".format(reporter) + "\n@here\n{}".format(msg[8:]) + "\n----------------------------------------"
			await bot.send_message(bot.get_channel(STAFF_CHANNEL), report)
			await bot.send_message(message.channel, "Sent report.")

		elif msg.upper().startswith("!SUPPORT"):
			username = message.author.mention
			await bot.send_message(message.channel, "{} **Link:**\n".format(username) + LINK_HERE)

		elif msg.upper().startswith("!PMTEST"):
			await bot.send_message(message.author, "Yo")

		else:
			await bot.send_message(message.channel, "Error: Command not found. Try using !help.")
		

bot.run(INSERT_TOKEN_HERE) # Note: Do not give another person your token, they will have access to your bot's account. For this reason, my token is not included.