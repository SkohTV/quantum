{

inputs = {
  nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
};


outputs = {
  self,
  nixpkgs
}:

let
  supportedSystems = [ "x86_64-linux" "x86_64-darwin" "aarch64-linux" "aarch64-darwin" ];
  forAllSystems = nixpkgs.lib.genAttrs supportedSystems;
  nixpkgsFor = forAllSystems (system: import nixpkgs { inherit system; });

in {

  packages = forAllSystems (system: {
    default = nixpkgsFor.${system}.stdenv.mkDerivation {
        pname = "quantum";
        version = "6.x.x";

        src = ./.;

        nativeBuildInputs = with nixpkgsFor.${system}; [
          mdbook
          mdbook-admonish

          cargo
          rustc
          rustfmt

          pkg-config
          openssl.dev
        ];
    };
  });

  devShells = forAllSystems (system: {
    default = nixpkgsFor.${system}.mkShell {
      inputsFrom = [ self.packages.${system}.default ];
    };
  });

};

}
