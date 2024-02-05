from discord.ext import commands


# In order to create a command, event or task, you inherit from the following classes
# They are small boilerplate snippets that set the `bot` variable and print add a log
# When they are loaded


class Custom_Command(commands.Cog):
	'''Cog setup'''
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		'''Send message when cog is successfully loaded'''
		print(f"Command loaded -> {type(self).__name__.lower()}")

#class Custom_Event

#class Custom_Task
