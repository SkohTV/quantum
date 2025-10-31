{

inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
};


outputs = {
  self,
  nixpkgs,
  flake-utils,
}:


flake-utils.lib.eachDefaultSystem (system:

    let
        pkgs = nixpkgs.legacyPackages.${system};
        quantum = pkgs.callPackage ./default.nix { };

    in {
        packages = {
            inherit quantum;
            default = quantum;
        };

        devShells = {
            default = pkgs.mkShell { inputsFrom = [ quantum ]; };
        };
    }
);


}
