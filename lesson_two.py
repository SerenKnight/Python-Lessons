list = ["1","2","3","4"]
output = []
def text_times_two(list):
    for letters in list:
        output.append((int(letters)*2))
    return(output)
text_times_two(list)

def if_else_l1(a, b):
    if a == b:
        print("a is equal to b")
    else:
        print("a is not equal to b")

def if_else_l2(a, b, c):
    if a > b and a > c:
        print("a is the biggest number")
    else:
        print("a is not the biggest number")
#if_else_l2(1, 2, 3)

def if_else_l3(a, b, c):
    largest = max(a, b, c)
    if largest == a == b == c:
        print("congratulations you have solved the bonus round")
    elif largest == a == b != c:
        print(f"a and b are the largest with value {a}")
    elif largest == b == c != a:
        print(f"b and c are the largest with value {b}")
    elif largest == a == c != b:
        print(f"a and c are the largest with value {a}")
    else:
        print(f"{largest} is the largest")

if_else_l3(2, 1, 2)


def for_and_while_loops_l1(games_list):
    for game in games_list:
        print(game)

#for_and_while_loops_l1(["botw", "skyrim", "runescape"])

def for_and_while_loops_l2(number):
    while number < 100:
        number += 3
        print(number)

#for_and_while_loops_l2(2)

def for_and_while_loops_l3():
    for integer in range(1, 101):
        if integer%2 == 0:
            print(integer)

#for_and_while_loops_l3()


def continue_break_l1():
    for number in range(1, 11):
        if number == 5:
            #continue
            break
        print(number)

continue_break_l1()


def continue_break_l2(list):
    count = 0
    for number in list:
        print(number)
        count += number
        if count > 21:
            print(count - number)
            break

continue_break_l2([1,2,3,4,5,6,7,8,9,10])

def continue_break_l3(colours):
    for colour in colours:
        if "a" in colour:
            continue
        print(colour)

continue_break_l3(["red", "blue", "yellow", "cyan", "green"])

