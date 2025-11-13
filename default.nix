{
    stdenv,
    cargo,
    rustc,
    rustfmt,
    pkg-config,
    openssl,
    mdbook,
    mdbook-admonish,
}:


stdenv.mkDerivation {
  pname = "quantum";
  version = "6.x.x";

  src = ./.;

  nativeBuildInputs = [
    mdbook
    mdbook-admonish

    cargo
    rustc
    rustfmt

    pkg-config
    openssl.dev
  ];
}
