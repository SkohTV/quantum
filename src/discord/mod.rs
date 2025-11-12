use std::sync::Mutex;
use tasks::Task;
use tokio::sync::mpsc::Sender;
use tokio::task::JoinHandle;

pub mod app;
pub mod framework;
pub mod ids;
pub mod utils;

pub mod commands;
pub mod events;
pub mod tasks;

pub struct Data {
    joined_livechat: Mutex<Option<JoinHandle<()>>>,
    task_tx: Mutex<Sender<Task>>,
}

pub type Error = Box<dyn std::error::Error + Send + Sync>;
pub type Context<'a> = poise::Context<'a, Data, Error>;

pub struct Handler;
