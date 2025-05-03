use crate::discord::{ids, Context, Error};
use crate::database;
use mongodb::bson::{doc, Document};
use poise::serenity_prelude as serenity;


/// Add a member to the cluster
#[poise::command(
    slash_command,
    rename="clusteradd",
    default_member_permissions="ADMINISTRATOR",
)]
pub async fn cmd(
    ctx: Context<'_>,
    #[description = "User to add to cluster"] user: serenity::Member,
) -> Result<(), Error> {

    // Init
    let text = format!("⌛ Loading...");
    let discord_response = ctx.say(text).await?;

    let client = database::start_db().await;
    let discord_id = user.user.id.to_string();

    let collec = client.database("cluster").collection::<Document>("discord_members");

    // Check if user in cluster
    let users_in_cluster = collec.find_one(doc!{ "discord_id": &discord_id }).await?;
    if users_in_cluster.is_some() {
        let msg = poise::CreateReply::default()
            .content(format!("{} is already in the cluster !", user));
        discord_response.edit(ctx, msg).await?;
        return Ok(());
    }

    // Add user to cluster
    collec.insert_one(doc!{
        "discord_id": &discord_id,
        "steam_id": 0,
    }).await?;

    // Give role
    user.add_role(ctx, ids::CLUSTER_ROLE).await?;

    // Wrap up
    let msg = poise::CreateReply::default()
        .content(format!("Successfly added {} to cluster !", user));

    discord_response.edit(ctx, msg).await?;

    Ok(())
}
