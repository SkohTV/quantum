use crate::discord::{ids, Context, Error};
use poise::serenity_prelude as serenity;
use crate::database;



/// Get the raw data of the embed (from the db)
#[poise::command(
    slash_command,
    rename="embedget",
    default_member_permissions="ADMINISTRATOR",
)]
pub async fn cmd(
    ctx: Context<'_>,
    #[description = "MessageID"] message_id: serenity::MessageId,
) -> Result<(), Error> {

    let text = format!("⌛ Loading...");
    let response = ctx.say(text).await?;

    let con = database::client::start_db().await;

    let val = database::requests::embed_get_data(con.clone(), &message_id.to_string())
        .await;
    let val = val.unwrap().next().await?.unwrap();
    let data: String = val.get(0).unwrap();

    let msg = poise::CreateReply::default()
        .content(format!("```json\n{}```", data));

    response.edit(ctx, msg).await?;

    Ok(())
}
