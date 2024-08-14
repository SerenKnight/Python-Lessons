import re


def credit_card_validator():
    card_check = False
    card_type = ""
    card_sum = []
    validation = []
    count = 0

    while not card_check:

        # Gets user input and removes spaces

        card_details = input("Please enter your Mum's Credit Card Num: \n")
        new_card_details = card_details.replace(" ", "")

        # Checks card number is the right length, contains only digits and
        # Starts with either 4, 5, 6 or 37
        # Depending on this value determines the card type
        # If exit is input then the program exits

        if 13 <= len(new_card_details) <= 16:
            visa = bool(re.match("4", new_card_details[0]))
            if visa:
                card_type = "Visa"
            master = bool(re.match("5", new_card_details[0]))
            if master:
                card_type = "Master"
            discover = bool(re.match("6", new_card_details[0]))
            if discover:
                card_type = "Discover"
            amex = bool(re.match("37", new_card_details[0] + new_card_details[1]))
            if amex:
                card_type = "American Express"

            # ! The above is essentailly doing the below

            # match new_card_details[0]:
            #     case "4":
            #         card_type = "Visa"
            #     case "5":
            #         card_type = "Master"
            #     case "6":
            #         card_type = "Discover"
            # if new_card_details[0] + new_card_details[1] == "37":
            #     card_type = "American Express"

            if card_type != "":
                if new_card_details.isdigit():
                    card_check = True
                else:
                    print("Invalid Card Format, please enter again. \n")
            else:
                print("Invalid Card Format, please enter again. \n")
        elif "exit" in new_card_details:
            exit()
        else:
            print("Invalid Card Format, please enter again. \n")

    # Once validated performs the Luhn check by adding new digits to a list

    if card_check:
        i = 2
        j = 1
        while i <= len(new_card_details):
            card_sum.append(2 * int(new_card_details[-i]))
            i += 2
        while j <= len(new_card_details):
            card_sum.append(int(new_card_details[-j]))
            j += 2

        # Checks for 2 digit numbers then adds their digit sum to a new list
        # Adds 1 digit numbers to the new list straight away

        for k in card_sum:
            if len(str(k)) > 1:
                validation.append(int(str(k)[0]) + int(str(k)[1]))
            else:
                validation.append(k)

        # Counts the values in the list

        for value in validation:
            count += value

        # If the total is a factor of 10 it is valid, otherwise it is not

        if count % 10 == 0:
            print(f"That is a valid {card_type} Card Number.\n")
        else:
            print("That is an invalid Credit Card.\n")

        card_check = False

        # Calls another function to see if the user wants to retry

        go_again()


def go_again():
    again_check = input("Would you like to try again? (y/n) \n")

    if "y" in again_check:
        credit_card_validator()


credit_card_validator()


# Sum Over Every Other Value Python One-Liner
# sum(stock_prices[::2])
