mod consts;
mod discord;


#[tokio::main]
async fn main() {
    discord::app::app().await;
}
