
import random


def roll (sides):
    num_rolled = random.randint(1, sides)
    return num_rolled


def mechanism():
    sides = input("Enter the highest integer in your data range:")
    default_rolls = 0
    norolls = 0

    try:
        norolls = input("How many terms would you like in your sequence?")
    except Exception:
        print("Your input was not an integer. Please type in an applicable number.")

    finally:
        while default_rolls < int(norolls):
            print(roll(sides))
            default_rolls += 1

mechanism()


