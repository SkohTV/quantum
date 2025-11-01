use tokio::join;

mod consts;
mod discord;
mod youtube;


#[tokio::main]
async fn main() {
    // discord::app::app().await;

    let _  = join!(
        discord::app::app(),
        // test()
    );
}
