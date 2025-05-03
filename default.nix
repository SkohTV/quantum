{
stdenv,

cargo,
rustc,
pkg-config,
openssl,
}:


stdenv.mkDerivation {
  pname = "quantum";
  version = "5.5";

  src = ./.;

  nativeBuildInputs = [
    cargo
    rustc

    pkg-config
    openssl.dev
  ];
}
