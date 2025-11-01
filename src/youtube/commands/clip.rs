use chrono::{TimeDelta, Utc};

use crate::youtube::{Author, Livestream};
use tokio::sync::mpsc::Sender;
use crate::discord::tasks::Task;


pub async fn clip(tx: Sender<Task>, livestream: &Livestream, author: Author, clip_name: &str) {
    let backtrack = TimeDelta::seconds(20);

    let now = Utc::now() - backtrack;
    let diff = now.signed_duration_since(livestream.start_time);
    let diff = diff.num_seconds().abs();

    let _ = tx.send(Task::YoutubeClip {
        author: author.username,
        url: format!("https://youtube.com/watch?v={}&t={}s", livestream.id, diff),
        name: clip_name.to_string(),
    }).await;
}
