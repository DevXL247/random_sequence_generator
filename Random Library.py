
import random


def roll (sides):
    num_rolled = random.randint(1, sides)
    return num_rolled


def mechanism():
    sides = input("How many numbers you need?")
    hello = 0
    norolls = 0

    try:
        norolls = input("How many rolls do you want? ")
    except Exception:
        print("Print a number fam, don't be stupid")

    finally:
        while hello < int(norolls):
            print(roll(sides))
            hello += 1

mechanism()


