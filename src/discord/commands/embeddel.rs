use crate::discord::{ids, Context, Error};
use poise::serenity_prelude as serenity;
use crate::database;



/// Delete an embed from the channel and the database
#[poise::command(
    slash_command,
    rename="embeddel",
    default_member_permissions="ADMINISTRATOR",
)]
pub async fn cmd(
    ctx: Context<'_>,
    #[description = "MessageID"] message_id: serenity::MessageId,
) -> Result<(), Error> {

    let text = format!("⌛ Loading...");
    let response = ctx.say(text).await?;

    let con = database::client::start_db().await;
    let channel = serenity::ChannelId::from(ids::CLUSTER_INFO_CHANNEL);

    database::requests::remove_embed(con.clone(), &message_id.to_string()).await?;
    channel.delete_message(ctx, message_id).await?;

    let msg = poise::CreateReply::default()
        .content("Successfully deleted embed");

    response.edit(ctx, msg).await?;

    Ok(())
}
