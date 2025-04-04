use crate::discord::{Context, Error, default};
use poise::serenity_prelude as serenity;
use crate::database;



/// Show informations of a user in the cluster
#[poise::command(
    slash_command,
    rename="clustershow",
)]
pub async fn cmd(
    ctx: Context<'_>,
    #[description = "Cluster member"] user: Option<serenity::Member>,
) -> Result<(), Error> {

    let text = format!("⌛ Loading...");
    let response = ctx.say(text).await?;

    let user = match user {
        Some(x) => x,
        _ => ctx.author_member().await.unwrap().into_owned(),
    };

    let con = database::client::start_db().await;
    let userid = user.user.id.to_string();

    // Check if user in db
    let mut val = database::requests::user_in_cluster(con.clone(), &userid).await?;

    if let Some(val) = val.next().await? {
        let val: u32 = val.get(0)?;

        if val == 0 {
            let msg = poise::CreateReply::default()
                .content(format!("{} is not in cluster", user))
                .ephemeral(true);
            response.edit(ctx, msg).await?;

            return Ok(());
        }
    }

    let val = database::requests::user_get_data(con.clone(), &user.user.id.to_string())
        .await;
    let val = val.unwrap().next().await?.unwrap();
    let steamid: String = val.get(0).unwrap_or("null".to_string());
    
    let embed = default::embed()
        .title("Cluster profile")
        .description(format!("{}\n\nSteamID -> `{}`", user, steamid));

    let msg = poise::CreateReply::default()
        .content("")
        .embed(embed);

    response.edit(ctx, msg).await?;

    Ok(())

}
