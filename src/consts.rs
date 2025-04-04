pub const MAJOR: u8 = 5;
pub const MINOR: u8 = 5;

pub fn mode() -> &'static str {
    let val = std::env::var("RELEASE");

    if val.is_ok() && val.unwrap() == "1" {
        "release"
    } else {
        "dev"
    }
}

pub fn version() -> String {
    format!("{}.{}-{}", MAJOR, MINOR, mode())
}
