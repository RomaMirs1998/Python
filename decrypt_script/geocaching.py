c_text = "faovheendiiensidslsiictiirineneveeescishneshseeazendnuuuisrrishescdcbrwsenndnse"
c_text_position = "rueoantitresnbr"

def caesar_decrypt(text, key):
    """
    Decrypts a Caesar ciphered text.

    Parameters:
    - text (str): The encrypted text.
    - key (int): The shift key for decryption.

    Returns:
    - str: The decrypted text.
    """
    a_z = 'abcdefghijklmnopqrstuvwxyz'
    decrypted = ''.join(
        a_z[(a_z.index(char) - key) % 26] if char in a_z else char for char in text
    )
    return decrypted

def decrypt_rail_fence(cipher, key):
    """
    Decrypts text encrypted using the Rail Fence cipher.

    Parameters:
    - cipher (str): The encrypted text.
    - key (int): The key for decryption.

    Returns:
    - str: The decrypted text.
    """
    length = len(cipher)
    fence = [['' for _ in range(length)] for _ in range(key)]

    i = 0
    direction_down = True
    for column in range(length):
        fence[i][column] = "*"
        if i == key - 1:
            direction_down = False
        elif i == 0:
            direction_down = True

        i = i + 1 if direction_down else i - 1

    index = 0
    for i in range(key):
        for j in range(length):
            if fence[i][j] == '*' and index < length:
                fence[i][j] = cipher[index]
                index += 1

    result = []
    i = 0
    direction_down = True
    for j in range(length):
        result.append(fence[i][j])
        if i == key - 1:
            direction_down = False
        elif i == 0:
            direction_down = True

        i = i + 1 if direction_down else i - 1

    return ''.join(result)

def run():
    """
    Main function to run the decryption methods on the provided ciphers.
    """
    print("\nCAESAR-DECRYPTING")
    for key in range(1, 15):
        plain_text = caesar_decrypt(c_text, key)
        print(f"{key}: {plain_text.upper()}")

    print("\nRAIL FENCE-DECRYPTING")
    for key in range(2, 15):
        plain_text = decrypt_rail_fence(c_text, key)
        if plain_text == "findedasschlossbeivierachtzweieinsdreineunneunundeinsvierdreieinssechseinssechs":
            print(f"\033[92m{key}: {plain_text.upper()}\033[0m")
        else:
            print(f"{key}: {plain_text.upper()}")

    print("\nPOSITION-DECRYPTING")
    print("\nCAESAR-DECRYPTING")
    for key in range(1, 15):
        plain_text = caesar_decrypt(c_text_position, key)
        print(f"{key}: {plain_text.upper()}")

    print("\nRAIL FENCE-DECRYPTING")
    for key in range(2, 15):
        plain_text = decrypt_rail_fence(c_text_position, key)
        if plain_text == "rotbraunerstein":
            print(f"\033[92m{key}: {plain_text.upper()}\033[0m")
        else:
            print(f"{key}: {plain_text.upper()}")