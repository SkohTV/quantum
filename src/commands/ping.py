from discord import app_commands, Interaction, Object
from src.classes import Custom_Command
from src.consts import Ids




class Ping(Custom_Command):
  # Command decorator
  @app_commands.command(
    name='ping',
    description='Renvoi le délai de Quantum entre les messages et réponses'
  )

  # Command definition
  async def ping(self, interaction: Interaction):

    # Permissions
    is_allowed, err_msg = (True, '')
    if not is_allowed:
      await interaction.response.send_message(err_msg, ephemeral=True)
      return

    # Core command code
    await interaction.response.send_message(content='⌛ Loading...')
    websockets_latency = self.bot.ws.latency

    await interaction.edit_original_response(content=f"Discord Websocket ⇒ `{websockets_latency:.3f}ms`")




async def setup(bot):
  '''Cog setup'''
  await bot.add_cog(Ping(bot), guilds=[Object(id=Ids.guild_main)])
