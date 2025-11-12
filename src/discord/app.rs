use std::sync::Mutex;

use crate::consts;
use crate::discord::{Data, Handler, commands, framework, ids, tasks};
use poise::serenity_prelude as serenity;
use tokio::sync::mpsc;

pub async fn app() {
    let token = match consts::MODE {
        consts::Mode::DEV => std::env::var("DISCORD_TOKEN_DEV"),
        consts::Mode::RELEASE => std::env::var("DISCORD_TOKEN_RELEASE"),
    }
    .expect("Discord token not found");

    let intents =
        serenity::GatewayIntents::GUILD_MEMBERS | serenity::GatewayIntents::GUILDS;

    let status = serenity::OnlineStatus::Online;
    let activity = serenity::ActivityData::playing(consts::version());

    let options = poise::FrameworkOptions {
        commands: vec![commands::ping::cmd(), commands::ytb::cmd()],

        post_command: |ctx| Box::pin(framework::post_command(ctx)),
        on_error: |err| Box::pin(framework::on_error(err)),
        command_check: Some(|ctx| Box::pin(framework::command_check(ctx))),

        ..Default::default()
    };

    let framework = poise::Framework::builder()
        .options(options)
        .setup(|ctx, _ready, framework| {
            let (tx, mut rx) = mpsc::channel(32);

            tokio::task::spawn(tasks::start_tasks(ctx.clone(), rx));

            Box::pin(async move {
                let main_guild = serenity::GuildId::from(ids::GUILD_ID);

                poise::builtins::register_in_guild(
                    ctx,
                    &framework.options().commands,
                    main_guild,
                )
                .await?;

                Ok(Data {
                    joined_livechat: Mutex::new(None),
                    task_tx: Mutex::new(tx),
                })
            })
        })
        .build();

    let client = serenity::ClientBuilder::new(token, intents)
        .framework(framework)
        .status(status)
        .activity(activity)
        .event_handler(Handler)
        .await;

    client.unwrap().start().await.unwrap();
}
