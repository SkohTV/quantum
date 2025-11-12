// use tokio::{task, time};
// use std::time::Duration;
use poise::serenity_prelude as serenity;
use tokio::sync::mpsc::Receiver;

mod ytb_clip;

pub enum Task {
    YoutubeClip {
        url: String,
        name: String,
        author: String,
    },
}

// CHANGE TIME TO MPSC (tokio)
// https://tokio.rs/tokio/tutorial/channels

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

pub async fn start_tasks<'a>(_ctx: serenity::Context, mut rx: Receiver<Task>) {
    // create_task!(cluster_embeds::task, ctx, 60);

    while let Some(task) = rx.recv().await {
        match task {
            Task::YoutubeClip { url, name, author } => println!("RECEIVED"),
        }
    }
}
