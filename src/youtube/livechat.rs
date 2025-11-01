use std::str::FromStr;

use serde_json::Value;
use stream_list::v3_data_live_chat_message_service_client::V3DataLiveChatMessageServiceClient;
use stream_list::{LiveChatMessageListRequest};
use tonic::metadata::MetadataValue;
use tonic::transport::Channel;
use tonic::Request;
use crate::discord::tasks::Task;
use crate::youtube::parser::parse_msg;
use crate::youtube::{Author, Message};
use tokio::sync::mpsc::Sender;

use chrono::{DateTime, Utc};

use super::Livestream;



pub mod stream_list {
    tonic::include_proto!("youtube.api.v3");
}


pub async fn chat_monitor(url: String, tx: Sender<Task>) {

    let api_key = std::env::var("YOUTUBE_TOKEN").expect("Youtube API key not found");
    
    // Get the livechat ID
    let client = reqwest::Client::new();
    let res = client
        .get(format!("https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id={url}"))
        .header("x-goog-api-key", &api_key)
        .send()
        .await
        .unwrap()
        .text()
        .await
        .unwrap();

    let v: Value = serde_json::from_str(&res).unwrap();
    let livechat_id = v["items"][0]["liveStreamingDetails"]["activeLiveChatId"]
        .as_str()
        .unwrap()
        .to_string();

    let starting_time = v["items"][0]["liveStreamingDetails"]["actualStartTime"]
        .as_str()
        .unwrap()
        .to_string();

    let dt: DateTime<Utc> = starting_time.parse().expect(format!("Converted {starting_time} to a datetime").as_str());

    let livestream = Livestream {
        id: url,
        start_time: dt,
    };


    // Open livechat gRPC
    let addr = "https://youtube.googleapis.com";
    let channel = Channel::from_static(addr)
        .tls_config(tonic::transport::ClientTlsConfig::new().with_native_roots()).unwrap()
        .connect()
        .await
        .unwrap();

    let mut client = V3DataLiveChatMessageServiceClient::new(channel);
    let mut next_page_token = None;

    // The big loop
    loop {
        let msg_req = LiveChatMessageListRequest {
            live_chat_id: Some(livechat_id.clone()),
            hl: None,
            profile_image_size: None,
            max_results: Some(20),
            page_token: next_page_token.clone(),
            part: vec!["snippet".to_string(), "authorDetails".to_string()],
        };

        let mut request = Request::new(msg_req);
        request
            .metadata_mut()
            .insert("x-goog-api-key", MetadataValue::from_str(&api_key).unwrap());

        let mut stream = client.stream_list(request).await.unwrap().into_inner();

        while let Some(resp) = stream.message().await.unwrap() {
            for item in resp.items {
                let Some(snippet) = item.snippet else { continue };
                let Some(msg) = snippet.display_message else { continue };
                let Some(author) = item.author_details else { continue };

                let author = Author {
                    is_moderator: author.is_chat_moderator.unwrap_or(false),
                    username: author.display_name.unwrap_or("Anonymous".to_string()),
                };

                let message = Message {
                    msg: msg,
                };

                parse_msg(tx.clone(), &livestream, author, message);
            }

            next_page_token = resp.next_page_token
        }
    }
}
