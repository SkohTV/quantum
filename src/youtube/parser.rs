use chrono::{TimeDelta, Utc};

use crate::youtube::{commands::clip::clip, Author, Livestream, Message};



pub async fn parse_msg(livestream: &Livestream, author: Author, message: Message) {

    if ! message.msg.starts_with("!") {
        return;
    }

    let it: Vec<&str> = message.msg[1..].splitn(2, " ").collect();
    let command = it[0];
    let msg = it[1];

    match command {
        "clip" => clip(livestream, author, &msg).await,
        _ => return,
    }
}




pub async fn test() {
    let a = Livestream {
        id: "0".to_string(),
        start_time: Utc::now(),
    };

    let b = Author {
        username: "skoh".to_string(),
        is_moderator: true,
    };

    let c = Message {
        msg: "!clip Omg that's so cool".to_string(),
    };

    parse_msg(&a, b, c).await;
}
