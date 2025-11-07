# Quantum
[Server](https://discord.gg/G8hrncZ) | [Docs](https://quantum.skoh.dev)  
Small all-in-one bot written in Rust  
Made for my **Discord server**, **Youtube channel** & **Game servers**  

## Disclaimer
This project is actively `work in progress`  
Documentation and README **might not** be up to date


## Usage
### Running
```bash
# Will need a better solution, but don't really wanna use `dotenv` crate
(source .env && cargo build && DISCORD_TOKEN_DEV="$DISCORD_TOKEN_DEV" YOUTUBE_TOKEN="$YOUTUBE_TOKEN" ./target/debug/quantum)
```

## Capabilities

### Discord

Commands:
`/ping` -> Send the discord websocket delay<br>

`/ytb post type=... url=...` -> Post a video/stream in an announcement channel<br>
`/ytb monitor url=...` -> monitor an upcoming livestream to edit a discord event #todo<br>
`/ytb join url=...` -> join and monitor a livestream chat (ref [youtube](#Youtube)) #wip<br>

`/archive #channel` #todo<br>

Events:<br>
`On new member -> Add role @member`<br>

Timers:<br>
\* Discord events for streams (cf ytb monitor) #todo<br>


### Youtube
`!clip [name]` -> create a clip and send in clips channel #wip<br>
`!ping` -> ping #todo<br>
`!help` -> https://quantum.skoh.dev/youtube #todo<br>
`!join` -> discord link #todo<br>
