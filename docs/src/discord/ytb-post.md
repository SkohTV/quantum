# `ytb post`
Post a video/stream in an announcement channel

## Usage
`/ytb post type=... url=...`

<br>

| Argument  | Description | Exemple |
| --------------- | --------------- | ---------------- |
| **type** | Type of message to send | `Video` or `Stream` |
| **url** | URL of any YouTube video | `https://youtu.be/S37C2SQb6qQ` |

## Source code
```rust,noplayground
{{#include ../../../src/discord/commands/ytb.rs:ytb}}
```
```rust,noplayground
{{#include ../../../src/discord/commands/ytb.rs:post}}
```
