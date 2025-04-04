{ outputs = { nixpkgs, ... }:

let
  allSystems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];

  forAllSystems = f: nixpkgs.lib.genAttrs allSystems (system: f {
    pkgs = import nixpkgs { inherit system; };
  });

in {
  devShells = forAllSystems ({ pkgs }: {
    default = pkgs.mkShell {
      packages = with pkgs; [
        cargo
        rustc

        pkg-config
        openssl
        openssl.dev
      ];
    };

  });
};
}
