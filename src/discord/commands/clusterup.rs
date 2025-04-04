use crate::discord::{Context, Error};
use poise::serenity_prelude as serenity;
use crate::database;



/// Add informations to a cluster member profile
#[poise::command(
    slash_command,
    rename="clusterup",
)]
pub async fn cmd(
    ctx: Context<'_>,
    #[description = "Cluster member"] user: Option<serenity::Member>,
    #[description = "SteamID"] steam_id: Option<String>,
) -> Result<(), Error> {

    let text = format!("⌛ Loading...");
    let response = ctx.say(text).await?;
    let author_member = ctx.author_member().await.unwrap().into_owned();

    // A non-admin trying to change someone's stuff
    if user.is_some() && !author_member.permissions.unwrap().administrator() {
        let msg = poise::CreateReply::default()
            .content("You are not allowed to do that >:(")
            .ephemeral(true);
        response.edit(ctx, msg).await?;

        return Ok(())
    } 

    let user = match user {
        Some(x) => x,
        _ => author_member,
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

    let mut content: Vec<String> = Vec::new();
    content.push(format!("Updated user {}", user));

    if let Some(steam_id) = steam_id {
        database::requests::update_user_steamid(con.clone(), &userid, &steam_id).await?;
        content.push(format!("Steamid changed"));
    }

    let msg = poise::CreateReply::default()
        .content(content.join("\n"));

    response.edit(ctx, msg).await?;

    Ok(())

}
