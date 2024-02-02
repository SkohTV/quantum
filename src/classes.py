from discord.ext import commands


class Custom_Command(commands.Cog):
	'''Cog setup'''
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		'''Send message when cog is successfully loaded'''
		print(f"Command loaded -> {type(self).__name__.lower()}")

