
import random


def roll (sides):
    num_rolled = random.randint(1, sides)
    return num_rolled


def mechanism():
    sides = input("How many numbers you need?")
    default_rolls = 0
    norolls = 0

    try:
        norolls = input("Enter the highest integer in your data range:  ")
    except Exception:
        print("Your input was not an integer. Please type in an applicable number.")

    finally:
        while default_rolls < int(norolls):
            print(roll(sides))
            default_rolls += 1

mechanism()


