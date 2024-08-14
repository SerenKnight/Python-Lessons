def caeser_salad_encrypt():
    word_check = False
    shift_check = False

    # Asks what word to encrypt

    while not word_check:
        word = input("What Word/Phrase would you like to Encrypt? \n")
        if all(x.isascii() for x in word):
            word_check = True
        else:
            print("Invalid format. \n")

    # Asks what shift value to use (digits only but allows for negative)

    while not shift_check:
        shift_value = input("What Shift Value would you like to use? \n")

        # ! if type int

        if all(y.isdigit() or y == "-" or y == "+" for y in shift_value):
            shift_value = int(shift_value)
            shift_check = True
        else:
            print("Invalid format. \n")

    encrypted_word = []

    # If shift value was negative or above 26 then multiples of 26 are added/subtracted

    while shift_value < 0:
        shift_value += 26

    while shift_value > 26:
        shift_value -= 26

    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    # Makes the word lowercase then for each letter moves the shift value along in the list
    # 26 is subtracted after to account for going beyond the list e.g. z + a shift
    # Value of 10 would be outside the range of the list, 25 + 10 - 26 = 9 = j (the 9th entry)
    # Adds these values to a list iteratively and then joins the entries of the list
    # Into a string at the very end

    for letter in word:
        letter = letter.lower()
        if letter not in letters:
            encrypted_word.append(letter)
        else:
            encrypted_word.append(
                letters[letters.index(letter) + shift_value - len(letters)]
            )

    print("".join(e for e in encrypted_word))


# Same as above but shift value is subtracted and no need to subtract 26
# From each letter as they cannot exceed the range of the list


def caeser_salad_decrypt():
    word_check = False
    shift_check = False

    while not word_check:
        word = input("What Word/Phrase would you like to Decrypt? \n")
        if all(x.isascii for x in word):
            word_check = True
        else:
            print("Invalid format. \n")

    while not shift_check:
        shift_value = input("What Shift Value would you like to use? \n")
        if all(y.isdigit() or y == "-" or y == "+" for y in shift_value):
            shift_value = int(shift_value)
            shift_check = True
        else:
            print("Invalid format. \n")

    decrypted_word = []

    while shift_value < 0:
        shift_value += 26

    while shift_value > 26:
        shift_value -= 26

    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    for letter in word:
        letter = letter.lower()
        if letter not in letters:
            decrypted_word.append(letter)
        else:
            decrypted_word.append(letters[letters.index(letter) - shift_value])

    print("".join(e for e in decrypted_word))


# Essentailly same as the Decrypt function but for the shift value in range(1, 26)


def caeser_salad_brute_force():
    word_check = False

    while not word_check:
        word = input("What Word/Phrase would you like to Brute Force? \n")
        if all(x.isascii for x in word):
            word_check = True
        else:
            print("Invalid format. \n")

    decrypted_word = []

    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]

    for shift_value in range(1, 26):
        for letter in word:
            letter = letter.lower()
            if letter not in letters:
                decrypted_word.append(letter)
            else:
                decrypted_word.append(letters[letters.index(letter) - shift_value])
        print(str(shift_value) + " " + "".join(e for e in decrypted_word))
        decrypted_word.clear()


def sneaky_solution():
    solution = input("Which program would you like to run? \n")
    match solution:
        case "brute":
            caeser_salad_brute_force()
        case "force":
            caeser_salad_brute_force()
        case "encrypt":
            caeser_salad_encrypt()
        case "decrypt":
            caeser_salad_decrypt()
        case _:
            caeser_salad_brute_force()


sneaky_solution()
