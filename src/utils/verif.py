from discord import Interaction
from src.utils.consts import Ids







def is_allowed(name: str, msg: Interaction) -> tuple[bool, str]:
  match name.lower():
    case 'ping':
      if not in_valid_channel([Ids.TextChannels.coding_commands], msg):
        return (False, 'Cannot post message in this channel')
      


  return (True, '')




def in_valid_channel(allowed_ids: list[int], msg: Interaction) -> bool:
  return msg.channel_id in allowed_ids

