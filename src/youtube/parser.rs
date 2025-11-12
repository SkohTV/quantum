use std::{thread::sleep, time::Duration};

use chrono::{TimeDelta, Utc};
use tokio::sync::mpsc::Sender;

use crate::{
    discord::tasks::Task,
    youtube::{Author, Livestream, Message, commands::clip::clip},
};

pub async fn parse_msg(
    tx: Sender<Task>,
    livestream: &Livestream,
    author: Author,
    message: Message,
) {
    if !message.msg.starts_with("!") {
        return;
    }

    let it: Vec<&str> = message.msg[1..].splitn(2, " ").collect();
    let command = it[0];
    let msg = it[1];

    match command {
        "clip" => clip(tx, livestream, author, &msg).await,
        _ => return,
    }
}

// pub async fn test() {
//     sleep(Duration::from_secs(5));
//
//     let a = Livestream {
//         id: "0".to_string(),
//         start_time: Utc::now(),
//     };
//
//     let b = Author {
//         username: "skoh".to_string(),
//         is_moderator: true,
//     };
//
//     let c = Message {
//         msg: "!clip Omg that's so cool".to_string(),
//     };
//
//     parse_msg(&a, b, c).await;
// }
