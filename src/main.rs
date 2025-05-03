mod database;
mod discord;
mod nitrado_api;
mod consts;

use dotenv::dotenv;



#[tokio::main]
async fn main() {
    dotenv().ok();

    discord::app::app().await;
    // nitrado_api::requests::get_servers().await;
}
