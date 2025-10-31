mod consts;
mod discord;
mod youtube;


#[tokio::main]
async fn main() {
    discord::app::app().await;
}
