# `ytb join`
Join and monitor a livestream chat (check [YouTube](../youtube) for available commands)

```admonish warning
This is actively work in progress
```

## Usage
`/ytb join id=...`  
`/ytb leave` (the opposite)

<br>

| Argument  | Description | Exemple |
| --------------- | --------------- | ---------------- |
| **id** | ID of currently active livestream | `C4qJeIjNd2U` |

## Source code
```rust,noplayground
{{#include ../../../src/discord/commands/ytb.rs:ytb}}
```
```rust,noplayground
{{#include ../../../src/discord/commands/ytb.rs:join}}
```
```rust,noplayground
{{#include ../../../src/discord/commands/ytb.rs:leave}}
```
