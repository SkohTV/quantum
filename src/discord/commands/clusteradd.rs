use crate::discord::{Context, Error, ids};
use poise::serenity_prelude as serenity;
use crate::database;



/// Add a user to the server cluster
#[poise::command(
    slash_command,
    rename="clusteradd",
    default_member_permissions="ADMINISTRATOR",
)]
pub async fn cmd(
    ctx: Context<'_>,
    #[description = "User to add to cluster"] user: serenity::Member,
) -> Result<(), Error> {

    let text = format!("⌛ Loading...");
    let response = ctx.say(text).await?;

    let con = database::client::start_db().await;
    let userid = user.user.id.to_string();

    // Check if user in db
    let mut val = database::requests::user_in_cluster(con.clone(), &userid).await?;

    if let Some(val) = val.next().await? {
        let val: u32 = val.get(0)?;

        // If yes
        if val == 1 {
            let msg = poise::CreateReply::default()
                .content(format!("{} is already in cluster", user))
                .ephemeral(true);
            response.edit(ctx, msg).await?;
            
            return Ok(());
        }
    }

    // If not
    database::requests::add_user(con.clone(), &userid).await?;
    user.add_role(ctx, serenity::RoleId::from(ids::CLUSTER_ROLE)).await?;

    let msg = poise::CreateReply::default()
        .content(format!("Added {} to cluster !", user));

    response.edit(ctx, msg).await?;

    Ok(())

}
