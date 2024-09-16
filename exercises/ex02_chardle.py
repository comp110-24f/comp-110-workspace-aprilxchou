"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730754347"


def input_word() -> str:  # using input function so no parameters
    """Gathers a word input from the user"""
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        print("'" + word + "'") # must concatenate in order to use quotes
    else:  # use else because all other words will not be 5 characters long
        print("Error: Word must contain 5 characters.")
        print("'" + word + "'")
    return word


input_word()  # call function with no arguments


def input_letter() -> str:
    """Gathers a character input from the user"""
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        print("'" + letter "'")
    else:
        print("Error: Character must be a single character.")
        print("'" + letter "'")
    return letter

input_letter() # written same way as input_word

def contains_char(word:str, letter:str) -> None:
    