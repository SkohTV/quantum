use mongodb::{bson::doc, options::{ClientOptions, ServerApi, ServerApiVersion}, Client};



pub async fn start_db() -> Result<Client> {
    let uri = std::env::var("MONGO_URI").expect("MONGI_URI must be set");

    let mut client_options = ClientOptions
        ::parse(uri)
        .await
        .expect("Err");

    let server_api = ServerApi::builder().version(ServerApiVersion::V1).build();
    client_options.server_api = Some(server_api);

    let client = Client::with_options(client_options)?;

    client
}
