{
  description = "flake intro";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      packages.${system}.default = pkgs.mkShell {
        buildInputs = [
          pkgs.gcc
          pkgs.python3Packages.pip
	  pkgs.python3Packages.flask
	  pkgs.python3Packages.joblib
          pkgs.python3Packages.setuptools
          pkgs.python3Packages.wheel
          pkgs.python3Packages.numpy
          pkgs.python3Packages.pandas
          pkgs.python3Packages.jupyter
          pkgs.python3Packages.ipykernel
          pkgs.python3Packages.ipywidgets
          pkgs.python3Packages.matplotlib
	  pkgs.python3Packages.statsmodels
          pkgs.python3Packages.scipy
          pkgs.python3Packages.seaborn
          pkgs.python3Packages.scikit-learn
        ];
      };
      devShells.${system}.default = self.packages.${system}.default;
    };
}
