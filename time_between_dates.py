import re
from colorama import Fore, Style


# Imports used to check input is of the right format and to use different colour fonts


def days_alive():

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    month_values = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31,
    }

    today_check = False
    birthday_check = False

    while not today_check:

        todays_date = input("What is the date today? (dd/mm/yyyy) ")

        # Checks the input is of the form XX/XX/XXXX if it is sets True

        matched_today = re.match(
            "[0-3][0-9]\/[0-1][0-9]\/[0-9][0-9][0-9][0-9]", todays_date
        )
        is_match_today = bool(matched_today)

        # If check was True split the date into days months and years otherwise asks the user to try again

        if is_match_today:
            today_day = todays_date[0:2]
            today_month = todays_date[3:5]
            today_year = todays_date[6:10]
            today_check = True
        else:
            print(Fore.RED + "\nIncorrect format for date, please try again.")
        print(Style.RESET_ALL)

    while not birthday_check:

        birthday = input("When is your birthday? (dd/mm/yyyy) ")

        # Checks the input is of the form XX/XX/XXXX if it is sets True

        matched_birthday = re.match(
            "[0-3][0-9]\/[0-1][0-9]\/[0-9][0-9][0-9][0-9]", birthday
        )
        is_match_birthday = bool(matched_birthday)

        # If check was True split the date into days months and years otherwise asks the user to try again

        if is_match_birthday:
            birth_day = birthday[0:2]
            birth_month = birthday[3:5]
            birth_year = birthday[6:10]
            birthday_check = True
        else:
            print(Fore.RED + "\nIncorrect format for date, please try again.")
        print(Style.RESET_ALL)

    days_in_month_diff = 0

    # Calculates the number of days in the date difference (e.g. from 25/09/1994 to 17/04/1995)

    if birth_month <= today_month:
        month_range = range(int(birth_month) - 1, int(today_month))
        for x in month_range:
            days_in_month_diff += month_values[months[x]]
        days_in_month_diff -= (
            month_values[months[int(today_month) - 1]] + int(birth_day) - int(today_day)
        )
    else:
        month_range = range(int(today_month) - 1, int(birth_month) - 1)
        for x in month_range:
            days_in_month_diff += month_values[months[x]]
        days_in_month_diff = 365 - days_in_month_diff + int(today_day) - int(birth_day)

    # Calculates the number of years difference between birthday and current day

    if birth_month <= today_month:
        year_diff = int(today_year) - int(birth_year)
    else:
        year_diff = int(today_year) - int(birth_year) - 1

    # Checks for leap years between year of birth and current year

    leap_years = []
    year_range = range(int(birth_year), int(today_year))
    for year in year_range:
        if str(year).endswith("00"):
            if year % 400 == 0:
                leap_years.append(year)
        else:
            if year % 4 == 0:
                leap_years.append(year)

    # Calculates the number of days in the year difference (e.g. from 17/04/1995 to 17/04/2022)

    days_in_year_diff = year_diff * 365 + len(leap_years)

    # Total length alive in days

    length_alive = days_in_month_diff + days_in_year_diff

    if 0 <= length_alive < 10000:
        print(f"Young grasshopper, you are {length_alive:,} days old.")
    elif length_alive >= 10000:
        print(f"Old git, you are {length_alive:,} days old.")
    else:
        print("An error occurred.")


days_alive()
