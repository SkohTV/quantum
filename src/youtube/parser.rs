use crate::youtube::{Author, Message};

pub fn parse_msg(author: Author, msg: Message) {
    println!("{}: {}", author.username, msg.msg);
}
