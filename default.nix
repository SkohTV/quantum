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

  src = ./bpfilter;

  nativeBuildInputs = [
    cargo
    rustc

    pkg-config
    openssl.dev
  ];
}
