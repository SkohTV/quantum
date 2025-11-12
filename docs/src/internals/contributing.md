# Contributing

## Develop
### Nix
```bash
nix develop
```
<details>
<summary>Nix files</summary>

#### `default.nix`
```nix
{{#include ../../../default.nix}}
```

#### `flake.nix`
```nix
{{#include ../../../flake.nix}}
```
</details>

### Manually
*todo*

## Building
```bash
cargo build
```

This will also build `gRPC` files in [`src/youtube/proto/`](https://github.com/SkohTV/quantum/tree/v6-dev/src/youtube/proto)  
Should be handeld automatically by `prost` ([`build.rs`](https://github.com/SkohTV/quantum/blob/v6-dev/build.rs))

## Running
```bash
# Will need a better solution, but don't really wanna use `dotenv` crate
(source .env && DISCORD_TOKEN_DEV="$DISCORD_TOKEN_DEV" YOUTUBE_TOKEN="$YOUTUBE_TOKEN" ./target/debug/quantum)
```

## Notes
If built in release mode, it uses `DISCORD_TOKEN_RELEASE`  
If built in debug mode, it uses `DISCORD_TOKEN_DEV`

Deployement should be fully automatic (both bot and docs by Github Actions)
