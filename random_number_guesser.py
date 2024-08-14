import random
from colorama import Fore, Style


# def random_number_guesser():
#     guessed = False
#     go_again = True
#     guesses = 0
#     high_score = 100
#     while go_again:
#         generated_random = random.randrange(1, 100)
#         while not guessed:
#             user_guess = int(input("\nChoose a number between 1 and 100: \n\n"))
#             if user_guess == generated_random:
#                 guesses += 1
#                 guessed = True
#             else:
#                 if user_guess < generated_random:
#                     print("\nYou guessed Lower \n")
#                     guesses += 1
#                 elif user_guess > generated_random:
#                     print("\nYou guessed Higher \n")
#                     guesses += 1
#         if guessed:
#             if guesses < high_score:
#                 high_score = guesses
#             print(f"\nYou guessed correctly in: {guesses} guesses! \n")
#             print(f"\nYour current High Score is: {high_score}. \n")
#             play_again = input("\nWould you like to play again? (y/n)\n\n")
#             if "y" in play_again:
#                 guesses = 0
#                 guessed = False
#             else:
#                 go_again = False


# random_number_guesser()


# def random_number_guesser():
#     guessed = False
#     go_again = True
#     guesses = 0
#     high_score = 100
#     while go_again:
#         generated_random = random.randrange(1, 101)
#         while not guessed:
#             user_guess = int(input("\nChoose a number between 1 and 100:\n\n"))
#             if user_guess == generated_random:
#                 guesses += 1
#                 guessed = True
#             else:
#                 percentage_diff = abs(generated_random - user_guess)
#                 if user_guess < generated_random:
#                     if percentage_diff > 30:
#                         print(Fore.CYAN + "\n+++ You guessed Lower +++")
#                         print(Style.RESET_ALL)
#                     elif 6 <= percentage_diff <= 30:
#                         print(Fore.YELLOW + "\n+++ You guessed Lower +++")
#                         print(Style.RESET_ALL)
#                     elif percentage_diff < 6:
#                         print(Fore.RED + "\n+++ You guessed Lower +++")
#                         print(Style.RESET_ALL)
#                     else:
#                         print("Error\n")
#                     guesses += 1
#                 elif user_guess > generated_random:
#                     if percentage_diff > 30:
#                         print(Fore.CYAN + "\n--- You guessed Higher ---")
#                         print(Style.RESET_ALL)
#                     elif 6 <= percentage_diff <= 30:
#                         print(Fore.YELLOW + "\n--- You guessed Higher ---")
#                         print(Style.RESET_ALL)
#                     elif percentage_diff < 6:
#                         print(Fore.RED + "\n--- You guessed Higher ---")
#                         print(Style.RESET_ALL)
#                     guesses += 1
#         if guessed:
#             if guesses < high_score:
#                 high_score = guesses
#             print(Fore.GREEN + f"\nYou guessed correctly in: {guesses} guesses!\n")
#             print(Style.RESET_ALL)
#             print(f"\nYour current High Score is: {high_score}. \n")
#             play_again = input("\nWould you like to play again? (y/n)\n\n")
#             if "y" in play_again:
#                 guesses = 0
#                 guessed = False
#             else:
#                 go_again = False


# random_number_guesser()


def random_number_guesser():
    guessed = False
    go_again = True
    range_check = False
    guesses = 0
    high_score = []

    while go_again:
        while not range_check:

            # Checks user input by splitting and removing brackets (if present)
            # If exit is input the program is exited

            user_range = input(
                "\nWhat range would you like to guess from? e.g. [1, 100] \n\n"
            )
            user_range = user_range.replace("[", "")
            user_range = user_range.replace("]", "")
            user_range = user_range.replace("(", "")
            user_range = user_range.replace(")", "")
            user_range = user_range.split(", ")
            if "exit" in user_range:
                exit()

            # Tries to get the first element of the list and the second + 1

            try:
                range_lower = int(user_range[0])
                range_upper = int(user_range[1]) + 1

                try:
                    if 0 <= range_lower < range_upper and 0 <= range_upper:
                        range_check = True

                    # Otherwise asks again for input

                    else:
                        print(Fore.RED + "\nIncorrect format please try again!")
                        print(Style.RESET_ALL)
                except:
                    print(Fore.RED + "\nIncorrect format please try again!")
                    print(Style.RESET_ALL)

            # If this is a character for example will ask again for input

            except:
                print(Fore.RED + "\nIncorrect format please try again!")
                print(Style.RESET_ALL)

            # Tries to check the lower range is below the upper range and both are > 0

        # Generates a random number in the custom range

        generated_random = random.randrange(range_lower, range_upper)

        # While the user has not guessed this loop repeats

        while not guessed:
            try:

                # Asks for user input

                user_guess = int(
                    input(
                        f"\nChoose a number between {user_range[0]} and {user_range[1]}:\n\n"
                    )
                )

            # If exit is input, the program exits

            except UnboundLocalError:
                if "exit" in user_guess:
                    exit()
            else:

                # If the number is guessed correctly

                if user_guess == generated_random:
                    guesses += 1
                    guessed = True
                else:

                    # Checks the percentage difference between the user input and
                    # the random number

                    percentage_diff = round(
                        abs(generated_random - user_guess)
                        / (int(user_range[1]) - int(user_range[0]))
                        * 100
                    )

                    # Depending on the percentage difference, cold warm or hot is
                    # displayed in different colours 2 loops for if your guess is
                    # above or below the target it also says higher/lower

                    if user_guess < generated_random:
                        if percentage_diff > 30:
                            print(Fore.CYAN + "\n+++ You guessed Lower +++")
                            print(Style.RESET_ALL)
                        elif 6 <= percentage_diff <= 30:
                            print(Fore.YELLOW + "\n+++ You guessed Lower +++")
                            print(Style.RESET_ALL)
                        elif percentage_diff < 6:
                            print(Fore.RED + "\n+++ You guessed Lower +++")
                            print(Style.RESET_ALL)
                        else:
                            print("Error\n")
                        guesses += 1
                    elif user_guess > generated_random:
                        if percentage_diff > 30:
                            print(Fore.CYAN + "\n--- You guessed Higher ---")
                            print(Style.RESET_ALL)
                        elif 6 <= percentage_diff <= 30:
                            print(Fore.YELLOW + "\n--- You guessed Higher ---")
                            print(Style.RESET_ALL)
                        elif percentage_diff < 6:
                            print(Fore.RED + "\n--- You guessed Higher ---")
                            print(Style.RESET_ALL)
                        else:
                            print("Error\n")
                        guesses += 1

            # If the number is guessed, highscore is appended with the guess
            # The smallest highscore is displayed and then the user is asked if they
            # want to go again, if yes, the program repeats from the start otherwise
            # it is not repeated

            if guessed:
                high_score.append(guesses)
                best_score = min(high_score)
                print(Fore.GREEN + f"\nYou guessed correctly in: {guesses} guesses!\n")
                print(Style.RESET_ALL)
                print(f"Your current High Score is: {best_score}. \n")
                play_again = input("\nWould you like to play again? (y/n)\n\n")
                if "y" in play_again:
                    guesses = 0
                    go_again = True
                    range_check = False
                    guessed = False
                    break
                else:
                    go_again = False


random_number_guesser()
