def input_l1():
    user_input = input("Please enter your name: ")
    print(f"Your name is + {user_input}")

#input_l1()

def input_l2():
    first_number = input("Please enter a number: ")
    second_number = input("Please enter a number: ")
    multiplied = str(first_number * second_number)
    print(f"Multiplied they equal {multiplied}")

#input_l2()

def input_l3():
    months = ["January", "February", "March", "April", "May", "June",\
        "July", "August", "September", "October", "November", "December"]
    sum = 0

    monthly_rain_fall = []
    for rain_fall in range(len(months)):
        monthly_rain_fall.append(input(f"Please enter the rainfall "
        f"of {months[rain_fall]} in mm: "))

    for month in months:
        print(f" In {month} there was "
        f"{monthly_rain_fall[months.index(month)]} mm of rainfall.")

    for value in monthly_rain_fall:
        sum += int(value)
    average_monthly_rain_fall = round(sum / len(monthly_rain_fall),3)
    max_monthly_rain_fall = max(monthly_rain_fall)
    print(f"\nThe Average rain fall was {average_monthly_rain_fall}mm")
    print(f"\nThe Maximum rainfall was {max_monthly_rain_fall}mm")

input_l3()
