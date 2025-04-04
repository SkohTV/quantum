mod database;
mod discord;
mod consts;

use dotenv::dotenv;



#[tokio::main]
async fn main() {
    dotenv().ok();

    discord::app::app().await;
}
