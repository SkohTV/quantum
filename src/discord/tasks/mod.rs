// use tokio::{task, time};
// use std::time::Duration;
use poise::serenity_prelude as serenity;

// mod cluster_embeds;






// macro_rules! create_task {
//     ($fun:expr, $ctx:ident, $delay:literal) => {
//         let ctx2 = $ctx.clone();
//         let forever = task::spawn(async move {
//             let delay_ms = Duration::from_secs($delay);
//             let mut interval = time::interval(delay_ms);
//
//             loop {
//                 interval.tick().await;
//                 $fun(&ctx2).await;
//             }
//         });
//
//         tokio::task::spawn(forever);
//     };
// }


pub fn start_tasks<'a>(_ctx: serenity::Context){
    // create_task!(cluster_embeds::task, ctx, 60);
}
