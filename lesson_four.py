# variable_a = 0
# variable_b = 0
# variable_c = 0
# count = 0
# keep_going = True
# user_input = ""
# while keep_going == True:
#   for i in range(1,100,3):
#     print(i)
#     count += 1
#   print(count)
#   if count < 150:
#     print("counted above")
#     variable_a += 1
#     count = 0
#   else:
#     print("counted below")
#     variable_b += 1
#   variable_a += variable_b
#   variable_c += variable_a
#   if variable_c > 200:
#     keep_going = False


# variable_test = "Working"

# try:
#     print(variable_test)
# except:
#     print("Sorry I can't do that")
# else:
#     print("Success!")
# finally:
#     print("Program complete.")


def method():
    name = input()
    print(name.title())

    print(name.upper())
    print(name.lower())

    words = name.split()
    words.reverse()
    full = " ".join(words)
    print(full)


method()
