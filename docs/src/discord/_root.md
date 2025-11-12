# Discord bot
Using [Poise](https://github.com/serenity-rs/poise) + [Serenity](https://github.com/serenity-rs/serenity)

## Commands
- [ping](./ping.md)
- [archive](./archive.md)
- [ytb post](./ytb-post.md)
- [ytb monitor](./ytb-monitor.md)
- [ytb join](./ytb-join.md)


## Events

### `guild_member_addition`
Add the role `@member` to any new user
```rust,noplayground
{{#include ../../../src/discord/events/guild_member_addition.rs}}
```


## Timers

### Livestream monitoring
```admonish missing
Work in progress
```

`@1min` -> For livestream monitored (see [`ytb monitor`](./ytb-monitor.md)), update the managed event

*no source code yet*
