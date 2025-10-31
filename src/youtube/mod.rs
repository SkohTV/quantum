pub mod livechat;
pub mod parser;



pub struct Author {
    is_moderator: bool,
    username: String,
}

pub struct Message {
    msg: String
}
