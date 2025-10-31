use chrono::{TimeDelta, Utc};

use crate::youtube::{Author, Livestream};


pub async fn clip(livestream: &Livestream, author: Author, clip_name: &str) {
    let backtrack = TimeDelta::seconds(20);

    let now = Utc::now() - backtrack;
    let diff = now.signed_duration_since(livestream.start_time);
    let diff = diff.num_seconds().abs();

    println!("{}", clip_name);
    println!("https://youtube.com/watch?v={}&t={}s", livestream.id, diff);
}
