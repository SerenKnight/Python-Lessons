import math


def christmas_tree():
    tree_height = input("How many tiers would you like the Christmas Tree to be? ")
    tiers = int(tree_height)

    for i in range(1, tiers + 1):
        print(" " * (tiers - i) + "*" * ((2 * i) - 1) + " " * (tiers - i))

    print(" " * (math.floor((tiers + (tiers - 1)) / 2)) + "*")


christmas_tree()
