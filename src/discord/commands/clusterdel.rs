use crate::discord::{ids, Context, Error};
use crate::database;
use mongodb::bson::{doc, Document};
use poise::serenity_prelude as serenity;


/// Remove a member from the cluster
#[poise::command(
    slash_command,
    rename="clusterdel",
    default_member_permissions="ADMINISTRATOR",
)]
pub async fn cmd(
    ctx: Context<'_>,
    #[description = "User to remove from cluster"] user: serenity::Member,
) -> Result<(), Error> {

    // Init
    let text = format!("⌛ Loading...");
    let discord_response = ctx.say(text).await?;

    let client = database::start_db().await;
    let discord_id = user.user.id.to_string();

    let collec = client.database("cluster").collection::<Document>("discord_members");

    // Check if user not in cluster
    let users_in_cluster = collec.find_one(doc!{ "discord_id": &discord_id }).await?;
    if users_in_cluster.is_none() {
        let msg = poise::CreateReply::default()
            .content(format!("{} is not in the cluster !", user));
        discord_response.edit(ctx, msg).await?;
        return Ok(());
    }

    // Remove user from cluster
    collec.delete_one(doc!{
        "discord_id": &discord_id
    }).await?;

    // Remove role
    user.remove_role(ctx, ids::CLUSTER_ROLE).await?;

    // Wrap up
    let msg = poise::CreateReply::default()
        .content(format!("Successfly removed {} from cluster !", user));

    discord_response.edit(ctx, msg).await?;

    Ok(())
}
