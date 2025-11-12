use crate::{
    discord::{Context, Error, ids},
    youtube::livechat::chat_monitor,
};
use poise::serenity_prelude as serenity;
use tokio::task;

// ANCHOR: ytb
#[poise::command(
    slash_command,
    rename = "ytb",
    subcommands("post", "join", "leave"),
    subcommand_required
)]
pub async fn cmd(_: Context<'_>) -> Result<(), Error> {
    Ok(())
}

#[derive(poise::ChoiceParameter)]
pub enum Kind {
    Video,
    Stream,
}
// ANCHOR_END: ytb

// ANCHOR: post
#[poise::command(slash_command)]
pub async fn post(
    ctx: Context<'_>,
    #[description = "Message preset"] kind: Kind,
    #[description = "Youtube video URL"] url: String,
) -> Result<(), Error> {
    let msg = match kind {
        Kind::Video => "Hey @everyone, **Skoh** à posté une nouvelle vidéo !!",
        Kind::Stream => "Hey @here, **Skoh** est en live !",
    };

    let _ = serenity::ChannelId::from(ids::VIDEO_CHANNEL)
        .say(ctx, format!("{msg}\n\n▷ {url}"))
        .await?;

    ctx.say(format!("✔ Message sent in <#{}>", ids::VIDEO_CHANNEL))
        .await?;

    Ok(())
}
// ANCHOR_END: post

// ANCHOR: join
#[poise::command(slash_command)]
pub async fn join(
    ctx: Context<'_>,
    #[description = "Youtube livestream URL"] livestream_id: String,
) -> Result<(), Error> {
    {
        let mut joined_livechat = ctx.data().joined_livechat.lock().unwrap();
        let task_tx = ctx.data().task_tx.lock().unwrap();

        let hndl = task::spawn(chat_monitor(livestream_id.clone(), task_tx.clone()));

        if joined_livechat.is_some() {
            joined_livechat.as_ref().unwrap().abort();
        }

        *joined_livechat = Some(hndl);
    }

    ctx.say(format!(
        "✔ Joined https://youtube.com/watch?v={} livestream",
        livestream_id.clone()
    ))
    .await?;

    Ok(())
}
// ANCHOR_END: join

// ANCHOR: leave
#[poise::command(slash_command)]
pub async fn leave(ctx: Context<'_>) -> Result<(), Error> {
    {
        let mut joined_livechat = ctx.data().joined_livechat.lock().unwrap();

        if joined_livechat.is_some() {
            joined_livechat.as_ref().unwrap().abort();
            *joined_livechat = None;
        }
    }

    ctx.say("✔ Left current livestream").await?;

    Ok(())
}
// ANCHOR_END: leave
