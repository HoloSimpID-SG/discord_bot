import discord
class DiscordServer:
	def __init__(self, name: str, guild: discord.Guild, channel_cart: discord.TextChannel):
		self.name			= name
		self.guild			= guild
		self.channel_cart	= channel_cart