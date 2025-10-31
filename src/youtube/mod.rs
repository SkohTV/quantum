use chrono::{DateTime, Utc};

pub mod livechat;
pub mod parser;
pub mod commands;


pub struct Livestream {
    id: String,
    start_time: DateTime<Utc>,
}

pub struct Author {
    is_moderator: bool,
    username: String,
}

pub struct Message {
    msg: String
}
