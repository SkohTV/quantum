use crate::consts;
use crate::discord;
use poise::serenity_prelude as serenity;

pub fn default_embed() -> serenity::CreateEmbed {
    let (name, pfp) = match consts::MODE {
        consts::Mode::DEV => (
            "Quantum Dev",
            "https://cdn.discordapp.com/avatars/1042497340352770142/17aa48868280edeb5edda826a0e49e48?size=1024",
        ),
        consts::Mode::RELEASE => (
            "Quantum",
            "https://cdn.discordapp.com/avatars/1033842126334742659/5235b0f44210455555f1685cac3580b9?size=1024",
        ),
    };

    let author = serenity::CreateEmbedAuthor::new(name)
        .url("https://github.com/SkohTV/quantum/")
        .icon_url(pfp);

    let footer = serenity::CreateEmbedFooter::new(format!(
        "Running on version {}",
        consts::version()
    ));

    serenity::CreateEmbed::default()
        .author(author)
        .footer(footer)
}

pub enum LogRole {
    Error,
    Info,
    Success,
}

pub async fn log_to_discord(
    ctx: impl serenity::CacheHttp + '_,
    log_message: String,
    role: LogRole,
) -> () {
    let color = match role {
        LogRole::Error => serenity::model::Color::RED,
        LogRole::Success => serenity::model::Color::FOOYOO,
        LogRole::Info => serenity::Colour::BLURPLE,
    };

    let embed = default_embed()
        .timestamp(serenity::Timestamp::now())
        .description(log_message)
        .color(color);

    let msg = serenity::CreateMessage::default().embed(embed);

    let _ = serenity::ChannelId::from(discord::ids::LOG_CHANNEL)
        .send_message(ctx, msg)
        .await;
}
