# Enigma Machine Command-Line Tool

The Enigma command-line tool is a simple implementation of the infamous Enigma machine used during World War II. This tool allows users to encode and decode texts using the Enigma's encryption mechanism.
Features

- One plug-board with arbitrary letter mappings (e.g., a maps to b).
- Three rotors with fixed internal letter mappings sourced from the Wikipedia article on Enigma rotor details.
- One reflector without the need for configuration.
 - Rotor 1 steps with every keypress. 
 - Rotor 2 steps every 7th step of rotor 1, and rotor 3 steps every 7th step of rotor 2.
- The reflector routes the signal back through all rotors without additional rotor stepping. It adds +13 mod 26 based on the initial result of rotor 3.

Usage

To use the Enigma command-line tool, you need to specify:

    Initial rotor settings using the -init x:y:z command-line option, where x, y, and z are the initial rotor positions given as integers from 0 to 25.
    Plug-board mappings using the -plug A:B[,C:D,...] command-line option.

For example:

```bash

./enigma -init 3:22:15 -plug A:H,D:P,X:Y "Hello world"
```
Note: Spaces are ignored and simply printed (i.e., no rotors are stepping)