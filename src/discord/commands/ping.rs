use reqwest::StatusCode;
use crate::discord::{Context, Error};
use crate::database;


/// Display the latency of the bot
#[poise::command(
    slash_command,
    rename="ping",
)]
pub async fn cmd(ctx: Context<'_>) -> Result<(), Error> {

    let text = format!("⌛ Loading...");

    // Discord ping
    let start = std::time::Instant::now();
    let discord_response = ctx.say(text).await?;
    let elapsed = start.elapsed();
    let discord_status = format!("Discord Websocket ⇒ `{}ms`", elapsed.as_millis());

    // Nitrado ping
    let start = std::time::Instant::now();
    let nitrado_api = reqwest::get("https://api.nitrado.net/ping").await?.status();
    let elapsed = start.elapsed();
    let nitrado_status = match nitrado_api {
        StatusCode::OK => format!("Nitrado API = `{}ms`", elapsed.as_millis()),
        err => format!("Nitrado API ⇒ `err: {}`", err.as_str()),
    };

    // Turso ping
    let start = std::time::Instant::now();
    let _ = database::client::start_db().await;
    let elapsed = start.elapsed();
    let turso_status = format!("Turso Database ⇒ `{}ms`", elapsed.as_millis());

    // Send msg
    let msg = poise::CreateReply::default()
        .content(format!("{}\n{}\n{}", discord_status, nitrado_status, turso_status));

    discord_response.edit(ctx, msg).await?;

    Ok(())
}
