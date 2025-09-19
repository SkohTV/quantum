{
    stdenv,
    cargo,
    rustc,
    pkg-config,
    openssl,
}:


stdenv.mkDerivation {
  pname = "quantum";
  version = "6.x.x";

  src = ./.;

  nativeBuildInputs = [
    cargo
    rustc

    pkg-config
    openssl.dev
  ];
}
