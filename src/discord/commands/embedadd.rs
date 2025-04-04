use crate::discord::{ids, Context, Error};
use poise::serenity_prelude as serenity;
use crate::database;



/// Add a server embed to the database
#[poise::command(
    slash_command,
    rename="embedadd",
    default_member_permissions="ADMINISTRATOR",
)]
pub async fn cmd(
    ctx: Context<'_>,
    #[description = "JSON embed data"] data: String,
) -> Result<(), Error> {

    let text = format!("⌛ Loading...");
    let response = ctx.say(text).await?;

    let con = database::client::start_db().await;
    let embed: serenity::Embed = serde_json::from_str(data.as_str())?;
    let msg = serenity::CreateMessage::default()
        .embed(embed.into());

    let channel = serenity::ChannelId::from(ids::CLUSTER_INFO_CHANNEL);
    let message = channel.send_message(ctx, msg).await?;
    let message_id = message.id;

    database::requests::add_embed(con.clone(), &message_id.to_string(), &data).await?;

    let msg = poise::CreateReply::default()
        .content(format!("Successfully sent embed > {}", message.link()));

    response.edit(ctx, msg).await?;

    Ok(())
}
