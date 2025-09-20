use poise::serenity_prelude as serenity;
use crate::discord::{Context, Error, ids};

#[poise::command(
    slash_command,
    rename="ytb",
    subcommands("post"),
    subcommand_required
)]
pub async fn cmd(_: Context<'_>) -> Result<(), Error> { Ok(()) }


#[derive(poise::ChoiceParameter)]
pub enum Kind { Video, Stream }


#[poise::command(slash_command)]
pub async fn post(
    ctx: Context<'_>,
    #[description = "Message preset"] kind: Kind,
    #[description = "Youtube video URL"] url: String
) -> Result<(), Error> {

    let msg = match kind {
        Kind::Video => "Hey @everyone, **Skoh** à posté une nouvelle vidéo !!",
        Kind::Stream => "Hey @here, **Skoh** est en live !",
    };

    let _ = serenity::ChannelId::from(ids::VIDEO_CHANNEL)
        .say(ctx, format!("{msg}\n\n▷ {url}"))
        .await?;

    ctx.say(format!("✔ Message sent in <#{}>", ids::VIDEO_CHANNEL)).await?;

    Ok(())
}
