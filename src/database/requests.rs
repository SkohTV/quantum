pub async fn add_user(con: libsql::Connection, userid: &str) -> Result<u64, libsql::Error> {
    con.execute(
        "INSERT INTO cluster_users(discord_id, steam_id) VALUES(?1, NULL)",
        libsql::params!(userid)
    ).await
}

// pub async fn retrieve_users(con: libsql::Connection) -> Result<libsql::Rows, libsql::Error> {
//     con.query(
//         "SELECT userid, steamid FROM cluster_users",
//         ()
//     ).await
// }


pub async fn user_in_cluster(con: libsql::Connection, userid: &str) -> Result<libsql::Rows, libsql::Error> {
    con.query(
        "SELECT COUNT(*) FROM cluster_users WHERE discord_id = ?1",
        libsql::params!(userid)
    ).await
}


pub async fn remove_user(con: libsql::Connection, userid: &str) -> Result<libsql::Rows, libsql::Error> {
    con.query(
        "DELETE FROM cluster_users WHERE discord_id = ?1",
        libsql::params!(userid)
    ).await
}

pub async fn update_user_steamid(con: libsql::Connection, userid: &str, data: &str) -> Result<libsql::Rows, libsql::Error> {
    con.query(
        "UPDATE cluster_users SET steam_id = ?1 WHERE discord_id = ?2",
        libsql::params!(data, userid)
    ).await
}

pub async fn user_get_data(con: libsql::Connection, userid: &str) -> Result<libsql::Rows, libsql::Error> {
    con.query(
        "SELECT steam_id FROM cluster_users WHERE discord_id = ?1",
        libsql::params!(userid)
    ).await
}

pub async fn add_embed(con: libsql::Connection, message_id: &str, content: &str) -> Result<u64, libsql::Error> {
    con.execute(
        "INSERT INTO cluster_embeds(message_id, server_id, content) VALUES(?1, NULL, ?2)",
        libsql::params!(message_id, content)
    ).await
}

pub async fn remove_embed(con: libsql::Connection, messageid: &str) -> Result<libsql::Rows, libsql::Error> {
    con.query(
        "DELETE FROM cluster_embeds WHERE message_id = ?1",
        libsql::params!(messageid)
    ).await
}

pub async fn embed_get_data(con: libsql::Connection, messageid: &str) -> Result<libsql::Rows, libsql::Error> {
    con.query(
        "SELECT content FROM cluster_embeds WHERE message_id = ?1",
        libsql::params!(messageid)
    ).await
}

// pub async fn add_embed()

// pub async fn get_servers(con: libsql::Connection) -> Result<libsql::Rows, libsql::Error> {
//     con.query(
//         "SELECT id, name FROM servers",
//         ()
//     ).await
// }

// pub async fn add_user(con: libsql::Connection, userid: &str) -> Result<u64, libsql::Error> {


// pub async fn retrieve_embeds(con: libsql::Connection) -> Result<libsql::Rows, libsql::Error> {
//     con.query(
//         "SELECT id, tags FROM embeds",
//         ()
//     ).await
// }
//
// pub async fn retrieve_embed_data(con: libsql::Connection, message_id: &str) -> Result<libsql::Rows, libsql::Error> {
//     con.query(
//         "SELECT data FROM embeds WHERE id = ?1",
//         libsql::params!(message_id)
//     ).await
// }
//
// pub async fn add_embed() {
//
// }
// pub async fn update_embed() {
//
// }
// pub async fn update_tags() {
//
// }
