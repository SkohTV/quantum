use poise::serenity_prelude as serenity;
use crate::discord::ids::PRIVATE_BOT_CHANNEL;


pub async fn task(ctx: &serenity::Context) {
    println!("Hello");

    let ch = serenity::ChannelId::from(PRIVATE_BOT_CHANNEL);
    let _ = ch.send_message(ctx, serenity::CreateMessage::default()
       .content("HIIIIII")
    ).await;
    
    // Check servers
    // For each server
        // Check if embed exist
            //  if not, then skip
        // Check ping
        // Check joueurs on server
        // Generate new embed
}


