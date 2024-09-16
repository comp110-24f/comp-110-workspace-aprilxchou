"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730754347"


def input_word() -> str:  # using input function so no parameters
    """Gathers a word input from the user"""
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        return word
    else:  # use else because all other words will not be 5 characters long
        print("Error: Word must contain 5 characters.")
        exit()


def input_letter() -> str:
    """Gathers a character input from the user"""
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)  # use spaces to print correctly
    count: int = 0  # count must start at 0
    if letter == word[0]:
        print(
            letter + " found at index 0"
        )  # searching for instances of letter at every index of word
        count = count + 1
    if letter == word[1]:
        print(letter + " found at index 1")  # indexes are not equal to letter position
        count = count + 1
    if letter == word[2]:
        print(letter + " found at index 2")
        count = count + 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count = count + 1
    if letter == word[4]:
        print(letter + " found at index 4")
        count = count + 1
    if count == 0:
        print(
            "No instances of " + letter + " found in " + word
        )  # muust print "No" instead of 0
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(
        word=input_word(), letter=input_letter()
    )  # calls these two functions simultaneously


if __name__ == "__main__":
    main()
