pub enum Mode {
   DEV, 
   RELEASE,
}


pub const MODE: Mode = if cfg!(debug_assertions) { Mode::DEV } else { Mode::RELEASE };


pub fn version() -> String {
    let major = env!("CARGO_PKG_VERSION_MAJOR");
    let minor = env!("CARGO_PKG_VERSION_MINOR");

    let mode = match MODE {
        Mode::DEV => "dev",
        Mode::RELEASE => "release",
    };

    format!("{major}.{minor}-{mode}")
}
