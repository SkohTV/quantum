use crate::consts;
use crate::discord::{Context, Data, Error, ids, utils};
use poise::serenity_prelude as serenity;

pub async fn on_error(error: poise::FrameworkError<'_, Data, Error>) {
    match error {
        poise::FrameworkError::Setup { error, .. } => panic!("Failed to start bot: {:?}", error),
        poise::FrameworkError::Command { error, ctx, .. } => {
            let msg = format!(
                "{} in <#{}>\n➜ `/{}`\n\n```{}```",
                ctx.author(),
                ctx.channel_id(),
                ctx.command().qualified_name,
                error
            );

            utils::log_to_discord(&ctx, msg, utils::LogRole::Error).await;
            let _ = ctx
                .send(
                    poise::CreateReply::default()
                        .content(format!("An error happened\n```{}```", error))
                        .ephemeral(true),
                )
                .await;
        }
        error => {
            if let Err(e) = poise::builtins::on_error(error).await {
                println!("Error while handling error: {}", e)
            }
        }
    }
}

pub async fn post_command(ctx: Context<'_>) {
    let msg = format!(
        "{} in <#{}>\n➜ `/{}`\nSuccess",
        ctx.author(),
        ctx.channel_id(),
        ctx.command().qualified_name,
    );

    utils::log_to_discord(&ctx, msg, utils::LogRole::Success).await;
}

pub async fn command_check(
    ctx: Context<'_>,
) -> Result<bool, Box<dyn std::error::Error + Send + Sync>> {
    // Channel check
    let channels = match consts::MODE {
        consts::Mode::DEV => vec![ids::PRIVATE_BOT_CHANNEL],
        consts::Mode::RELEASE => vec![ids::PUBLIC_BOT_CHANNEL, ids::PRIVATE_BOT_CHANNEL],
    };

    let channels = channels
        .iter()
        .map(|x| serenity::ChannelId::from(x.clone()))
        .collect::<Vec<_>>();

    if !channels.contains(&ctx.channel_id()) {
        let msg = poise::CreateReply::default()
            .content(format!(
                "You can't use commands here, try in <#{}>",
                ids::PUBLIC_BOT_CHANNEL
            ))
            .ephemeral(true);

        ctx.send(msg).await?;

        utils::log_to_discord(
            ctx,
            format!(
                "{} tried to run `/{}` in <#{}>",
                ctx.author(),
                ctx.command().name,
                ctx.channel_id()
            ),
            utils::LogRole::Error,
        )
        .await;

        return Ok(false);
    }

    Ok(true)
}
