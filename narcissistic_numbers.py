def narcissistic_numbers():
    test_number = input(
        "Please input a number that will be checked for narcissism \n\n"
    )
    order = len(test_number)
    sum = 0
    for digit in test_number:
        sum += int(digit) ** order
    print("")
    if str(sum) == test_number:
        return True
    else:
        return False


print(narcissistic_numbers())
