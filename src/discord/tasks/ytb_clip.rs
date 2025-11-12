use crate::discord::ids::PRIVATE_BOT_CHANNEL;
use poise::serenity_prelude as serenity;

pub async fn task(ctx: &serenity::Context) {
    // add data as parameter
    println!("Hello");

    let ch = serenity::ChannelId::from(PRIVATE_BOT_CHANNEL);
    let _ = ch
        .send_message(ctx, serenity::CreateMessage::default().content("HIIIIII"))
        .await;
}
