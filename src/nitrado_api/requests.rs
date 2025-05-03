use reqwest::header::AUTHORIZATION;


pub async fn get_servers() {
    let client = reqwest::Client::new();

    let req = client
        .get("https://api.nitrado.net/services")
        .header(AUTHORIZATION, std::env::var("NITRADO_API_TOKEN")
            .expect("missing or wrong NITRADO_API_TOKEN"))
        .send()
        .await
        .unwrap()
        .text()
        .await;

    println!("{}", req.unwrap());
}

