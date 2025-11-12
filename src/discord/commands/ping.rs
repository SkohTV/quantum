use crate::discord::{Context, Error};

/// Display the latency of the bot
#[poise::command(slash_command, rename = "ping")]
pub async fn cmd(ctx: Context<'_>) -> Result<(), Error> {
    let text = format!("⌛ Loading...");

    // Discord ping
    let start = std::time::Instant::now();
    let discord_response = ctx.say(text).await?;
    let elapsed = start.elapsed();
    let discord_status = format!("Discord Websocket ⇒ `{}ms`", elapsed.as_millis());

    // Send msg
    let msg = poise::CreateReply::default().content(format!("{}", discord_status));

    discord_response.edit(ctx, msg).await?;

    Ok(())
}
