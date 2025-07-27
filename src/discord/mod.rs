pub mod app;
pub mod framework;
pub mod ids;
pub mod utils;

pub mod commands;
pub mod events;
// pub mod tasks;



pub struct Data {}
pub type Error = Box<dyn std::error::Error + Send + Sync>;
pub type Context<'a> = poise::Context<'a, Data, Error>;

pub struct Handler;
