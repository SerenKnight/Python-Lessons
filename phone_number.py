def phone_number():
    digits = input("\nPlease enter 10 digits in array form: \n\n")
    for char in [" ", ",", "[", "]"]:
        if char in digits:
            digits = digits.replace(char, "")
    print("\n(" + digits[0:3] + ")" + " " + digits[3:6] + "-" + digits[6:10])


phone_number()
