# SPDX-License-Identifier: Apache-2.0
# This is a modified discord bot example from of https://github.com/Rapptz/discord.py/blob/v2.5.2/examples/basic_bot.py
# This example requires the 'members' and 'message_content' privileged intents to function.
import discord
from discord.ext import commands
import random
from discord_server import DiscordServer

def init(name: str):

	discordServer = DiscordServer(name, None, None)

	description = '''An example bot to showcase the discord.ext.commands extension
	module.

	There are a number of utility commands being showcased here.'''

	intents = discord.Intents.default()
	intents.members = True
	intents.message_content = True

	bot = commands.Bot(command_prefix='?', description=description, intents=intents)

	@bot.event
	async def on_ready():
		discordServer.guild			= discord.utils.get(bot.guilds, name=discordServer.name)
		if discordServer.guild is not None:
			discordServer.channel_cart	= discord.utils.get(discordServer.guild.text_channels, name='merchtalk')
		print(f'Logged in as {bot.user} (ID: {bot.user.id})')
		print('------')

	@bot.event
	async def on_message(message):
		#do not reply itself
		if message.author.id == bot.user.id:
			return

		#reply "Pong!" if ping is detected
		recv_message = str(message.content).lower()
		if (-1 != recv_message.find('ping')):
			await message.reply('Pong!', mention_author=True)
		#else run other command
		else:
			await bot.process_commands(message)


	@bot.command()
	async def add(ctx, left: int, right: int):
		"""Adds two numbers together."""
		await ctx.send(left + right)


	@bot.command()
	async def roll(ctx, dice: str):
		"""Rolls a dice in NdN format."""
		try:
			rolls, limit = map(int, dice.split('d'))
		except Exception:
			await ctx.send('Format has to be in NdN!')
			return

		result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
		await ctx.send(result)


	@bot.command(description='For when you wanna settle the score some other way')
	async def choose(ctx, *choices: str):
		"""Chooses between multiple choices."""
		await ctx.send(random.choice(choices))


	@bot.command()
	async def repeat(ctx, times: int, content='repeating...'):
		"""Repeats a message multiple times."""
		for i in range(times):
			await ctx.send(content)


	@bot.command()
	async def joined(ctx, member: discord.Member):
		"""Says when a member joined."""
		await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

	@bot.command()
	async def kys(ctx):
		"""Kill the discord bot"""
		await ctx.send('```\nあ、死んだ\n世界は酷い\nさよならー\n```')
		quit()

	@bot.command()
	async def guild_info(ctx):
		"""Get Guild Information"""
		if discordServer.guild is not None:
			members = ''
			async for member in discordServer.guild.fetch_members(limit=50):
				members = f'{members}\n{member.name}'
			await ctx.send(f'```\nGuild name   : {discordServer.guild.name}\nGuild members: {members}\n```')

	@bot.command()
	async def cart(ctx, command: str, argument: str):
		"""Usage: ?cart <command> <argument>"""
		if discordServer.channel_cart is not None:
			if discordServer.channel_cart == ctx.channel:
				await ctx.send("Cart command invoked!")
			else:
				await ctx.message.reply('Please invoke cart command at #merchtalk!', mention_author=True)

	@bot.group()
	async def cool(ctx):
		"""Says if a user is cool.

		In reality this just checks if a subcommand is being invoked.
		"""
		if ctx.invoked_subcommand is None:
			await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


	@cool.command(name='bot')
	async def _bot(ctx):
		"""Is the bot cool?"""
		await ctx.send('Yes, the bot is cool.')

	return bot
