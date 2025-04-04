use libsql::Builder;



pub async fn start_db() -> libsql::Connection {
    let url = std::env::var("TURSO_DATABASE_URL").expect("TURSO_DATABASE_URL must be set");
    let token = std::env::var("TURSO_AUTH_TOKEN").expect("TURSO_AUTH_TOKEN must be set");

    let db = Builder::new_remote(url, token)
        .build()
        .await
        .unwrap();

    let con = db.connect().unwrap();

    init_tables(con.clone()).await;

    con
}



async fn init_tables(con: libsql::Connection) {
    con.execute("CREATE TABLE IF NOT EXISTS users( \
        userid text PRIMARY KEY, \
        steamid text \
    )", ()).await.unwrap();
}
