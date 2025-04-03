let
    pkgs = import <nixpkgs> {};
in
    pkgs.mkShell {
        buildInputs = with pkgs; [
            bash
            zip
        ];

        shellHook = ''
        ./build.sh
        exit
        '';
    }
