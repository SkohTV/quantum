## Build
Create a python virtual env and install packages
```sh
# Create a virtual env
python -m venv _venv

# Install packages
_venv/bin/python -m pip install -r requirements.txt
```

Then you will need a `.env` file that contains the following :
```sh
DISCORD_BOT_TOKEN='your_personnal_testing_bot_token'
```

Afterward you can run the bot locally on your server with 
```sh
_venv/bin/python main.py
```


## Todo
- Remove python dotenv and dotfile parser


## Bot

✅ -> Finished and functionnal<br>
✨ -> Usable, but not finished<br>
🔥 -> Not usable, but wip<br>
❌ -> Work started, but suspended/stopped<br>
📌 -> Work not started, but high priority<br>
⚰️ -> Work not started, not planned yet<br>

### Commands
| Mod                                                                                   | Command                    | Status |
|---------------------------------------------------------------------------------------|----------------------------|--------|
| <img src="doc/img/discord.png" width=24px>                                            | `/ping`                    | ✨      |
| <img src="doc/img/discord.png" width=24px> <img src="doc/img/youtube.png" width=12px> | `/post [ytb_url] [format]` | 📌     |
| <img src="doc/img/youtube.png" width=24px> <img src="doc/img/discord.png" width=12px> | `!ping [name]`             | ⚰️     |
|                                                                                       |                            |        |

### Events
| Mod                                                                                   | Event                                             | Status |
|---------------------------------------------------------------------------------------|---------------------------------------------------|--------|
| <img src="doc/img/discord.png" width=24px> <img src="doc/img/youtube.png" width=12px> | On new video/stream/post... from Skoh ytb channel | 📌     |
|                                                                                       |                                                   |        |

### Other
| Mod                                        | Event                                | Status |
|--------------------------------------------|--------------------------------------|--------|
| <img src="doc/img/discord.png" width=24px> | Logs in #quantum-logs                | 📌     |
| <img src="doc/img/discord.png" width=24px> | Sync commands to Skoh discord server | ✨      |
|                                            |                                      |        |
