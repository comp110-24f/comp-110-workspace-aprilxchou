"""A simple number guessing game!"""

__author__ = "730754347"


def guess_a_number() -> None:  # all variables will be input
    secret: int = 7
    x: str = input("Guess a number: ")  # use input function, but must be string
    print("Your guess was " + str(x))
    if int(x) == secret:  # convert x to int type to make compatible with secret
        print("You got it!")
    elif int(x) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:  # can use else here because no other possiblities
        print("Your guess was too high! The secret number is " + str(secret))
    return None  # no return value needed


if __name__ == "__main__":
    guess_a_number()
