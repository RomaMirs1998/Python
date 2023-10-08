def decrypt(message):
    '''
    Decrypts a message
    :param message:
    :return:
    '''

    encrypted_message = message # store encrypted message
    stored_letters= {} # store letters and their frequency

    for char in encrypted_message: # count letters
        if char not in stored_letters: # if letter is not in dictionary, add it
            stored_letters[char] = 1
        else: # if letter is in dictionary, increase its value by 1
            stored_letters[char] += 1
    # sort stored letters by values
    stored_letters = sorted(stored_letters.items(), key=lambda x: x[1], reverse=True)
    print(stored_letters)

    print()
    print()
    # W stands alone and is the most frequent letter in the encrypted message so it is probably "a" or "i" - "a" is more probable
    attempt= encrypted_message.replace("W", "\033[92ma\033[0m")
    # I find the pattern "aE" in the encrypted message so I replace "E" with "s" - maybe it is "as"
    attempt= attempt.replace("E", "\033[92ms\033[0m")
    # I find the pattern ", aDH" in the encrypted message so I replace "D" with "n" and "H" with "d- maybe it is "and"
    attempt= attempt.replace("H", "\033[92md\033[0m")
    attempt= attempt.replace("D", "\033[92mn\033[0m")
    # I find the pattern "daMa" in the encrypted message so I replace "M" with "t" - maybe it is "data"
    attempt= attempt.replace("M", "\033[92mt\033[0m")
    # I find the pattern "tBQ" in the encrypted message so I replace "B" with "h" and "Q" with "e" - maybe it is "the"
    attempt= attempt.replace("B", "\033[92mh\033[0m")
    attempt= attempt.replace("Q", "\033[92me\033[0m")
    # I find the pattern "aZe" in the encrypted message so I replace "Z" with "r" - maybe it is "are"
    attempt= attempt.replace("Z", "\033[92mr\033[0m")
    # I find the pattern "dataCases" in the encrypted message so I replace "C" with "b" - maybe it is "databases"
    attempt= attempt.replace("C", "\033[92mb\033[0m")
    # I find the pattern "httL" and "serYer" in the encrypted message so I replace "L" with "p" and "Y" with "v" - maybe it is "http server"
    attempt= attempt.replace("L", "\033[92mp\033[0m")
    attempt= attempt.replace("Y", "\033[92mv\033[0m")
    # I find the pattern "apprPaUhes" in the encrypted message so I replace "P" with "o" and "U" with "c" - maybe it is "approaches"
    attempt= attempt.replace("P", "\033[92mo\033[0m")
    attempt= attempt.replace("U", "\033[92mc\033[0m")
    # I find the pattern "neNt" in the encrypted message so I replace "N" with "x" - maybe it is "next"
    attempt= attempt.replace("N", "\033[92mx\033[0m")
    # I find the pattern "aOso" in the encrypted message so I replace "O" with "l" - maybe it is "also"
    attempt= attempt.replace("O", "\033[92ml\033[0m")
    # I find the pattern "applAcable" in the encrypted message so I replace "A" with "i" - maybe it is "applicable"
    attempt= attempt.replace("A", "\033[92mi\033[0m")
    # I find the pattern "tSples" in the encrypted message so I replace "S" with "u" - maybe it is "tuples"
    attempt= attempt.replace("S", "\033[92mu\033[0m")
    # "VocusinT" is a pattern in the encrypted message so I replace "T" with "g" and "V" with "f" - maybe it is "focusing"
    attempt= attempt.replace("T", "\033[92mg\033[0m")
    attempt= attempt.replace("V", "\033[92mf\033[0m")
    # "RaterXarFing" is a pattern in the encrypted message so I replace "R" with "w" and "X" with "m" and "F" with k - maybe it is "watermarking"
    attempt= attempt.replace("R", "\033[92mw\033[0m")
    attempt= attempt.replace("X", "\033[92mm\033[0m")
    attempt= attempt.replace("F", "\033[92mk\033[0m")
    # And the last one is only "K" with "y" and "I" with "q"
    attempt= attempt.replace("K", "\033[92my\033[0m")
    attempt= attempt.replace("I", "\033[92mq\033[0m")

    # Because of the standalone "W" it was really fast sure that this is a English message
    # I solved the problem by trying to find patterns in the encrypted message and replacing letters with the most probable ones
    # I used at first the most frequent letters in the English language and then I tried to find patterns in the encrypted message
    # but that didn't work so I tried to find patterns in the encrypted message and then I replaced letters with the most frequent ones
    # after a few tries I solved the problem and I got the decrypted message which is:

    print(attempt) # print decrypted message

