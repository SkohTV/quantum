use mongodb::{bson::doc, options::{ClientOptions, ServerApi, ServerApiVersion}, Client};



pub async fn start_db() -> Result<Client> {
    // let url = std::env::var("TURSO_DATABASE_URL").expect("TURSO_DATABASE_URL must be set");
    // let token = std::env::var("TURSO_AUTH_TOKEN").expect("TURSO_AUTH_TOKEN must be set");
    //
    // let db = Builder::new_remote(url, token)
    //     .build()
    //     .await
    //     .unwrap();
    //
    // let con = db.connect().unwrap();
    //
    // init_tables(con.clone()).await;
    //
    // con

    let mut client_options = ClientOptions
        ::parse("mongodb+srv://admin:<db_password>@quantum.m5ylaih.mongodb.net/?appName=quantum")
        .await
        .expect("Err");

    let server_api = ServerApi::builder().version(ServerApiVersion::V1).build();
    client_options.server_api = Some(server_api);

    let client = Client::with_options(client_options)?;

    // client
    //     .database("admin")
    //     .run_command(doc! {"ping": 1}, None)
    //     .await?;
    // println!("Pinged your deployment. You successfully connected to MongoDB!");

    client
}



async fn init_tables(con: libsql::Connection) {
    con.execute("CREATE TABLE IF NOT EXISTS users( \
        userid text PRIMARY KEY, \
        steamid text \
    )", ()).await.unwrap();
}

