use crate::discord::{Handler, ids, utils};
use poise::serenity_prelude as serenity;
use serenity::async_trait;

#[async_trait]
impl serenity::EventHandler for Handler {
    async fn guild_member_addition(
        &self,
        ctx: serenity::Context,
        new_member: serenity::Member,
    ) {
        let role = serenity::RoleId::from(ids::MEMBER_ROLE);
        let _ = new_member.add_role(&ctx, role).await;

        let msg = format!("Given role <@&{}> to {}", role, new_member);

        utils::log_to_discord(&ctx, msg, utils::LogRole::Info).await;
    }
}
