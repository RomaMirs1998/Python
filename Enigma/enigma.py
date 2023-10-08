import sys


class Enigma:
    def __init__(self, rotor_positions, plug_board_mappings):
        # Rotor mappings from the provided data
        self.rotors = [
            "JGDQOXUSCAMIFRVTPNEWKBLZYH",
            "NTZPSFBOKMWRCJDIVLAEYUXHGQ",
            "JVIUBHTCDYAKEQZPOSGXNRMWFL"
        ]

        # Set initial rotor positions
        self.positions = rotor_positions

        # Set plug-board mappings
        self.plug_board = {char: char for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
        for mapping in plug_board_mappings:
            self.plug_board[mapping[0]] = mapping[2]
            self.plug_board[mapping[2]] = mapping[0]

    def reflect(self, char):
        # Add +13 mod 26
        return chr((ord(char) - ord('A') + 13) % 26 + ord('A'))

    def rotate_rotors(self):
        # Rotate rotor 1
        self.positions[0] = (self.positions[0] + 1) % 26

        # Check if rotor 1 has completed 7 rotations
        if self.positions[0] % 7 == 0:
            # Rotate rotor 2
            self.positions[1] = (self.positions[1] + 1) % 26

            # Check if rotor 2 has completed 7 rotations
            if self.positions[1] % 7 == 0:
                # Rotate rotor 3
                self.positions[2] = (self.positions[2] + 1) % 26

    def encode_char(self, char):
        # If character is not a letter, return as is
        if not char.isalpha():
            return char

        # Convert to upper case
        char = char.upper()

        # Pass through plug-board
        char = self.plug_board[char]

        # Pass through rotors
        for i in range(3):
            offset = self.positions[i]
            char = self.rotors[i][(ord(char) - ord('A') + offset) % 26]

        # Reflect
        char = self.reflect(char)

        # Pass back through rotors
        for i in range(2, -1, -1):
            offset = self.positions[i]
            char = chr((self.rotors[i].index(char) - offset + 26) % 26 + ord('A'))

        # Pass through plug-board again
        char = self.plug_board[char]

        return char

    def encode(self, text):
        encoded_text = ""
        for char in text:
            encoded_char = self.encode_char(char)
            encoded_text += encoded_char

            # Rotate rotors only if character is a letter
            if char.isalpha():
                self.rotate_rotors()

        return encoded_text


def main():
    # Extract command line arguments
    args = sys.argv[1:]

    # Check for required arguments
    if "-init" not in args or "-plug" not in args or len(args) != 5:
        return "Usage: ./enigma -init x:y:z -plug A:B[,C:D,...] \"Text\""

    # Extract rotor initial positions
    init_index = args.index("-init")
    rotor_positions = list(map(int, args[init_index + 1].split(":")))

    # Extract plug-board mappings
    plug_index = args.index("-plug")
    plug_board_mappings = args[plug_index + 1].split(",")

    # Extract text to be encoded/decoded
    text = args[-1]

    # Initialize Enigma machine and encode/decode text
    enigma = Enigma(rotor_positions, plug_board_mappings)
    encoded_text = enigma.encode(text)

    return encoded_text


# For the purpose of this demonstration, we'll mock the command line input
#sys.argv = ["./enigma", "-init", "3:22:15", "-plug", "A:H,D:P,X:Y", "Hello world"]
output = main()
print(output)