"""A word-guessing game with six chances and hints at the accuracy of each guess."""

__author__ = "730754347"

def input_guess(secret_word_len:int) -> str:
    """Takes word guess from user"""
    user_guess = input(f"Enter a { secret_word_len } character word: ") #f-string format, do not have to concatenate
    while len(user_guess) != secret_word_len: #l oop allows us to repeat if word of wrong length is entered again
        user_guess = input(f"That wasn't { secret_word_len } chars! Try again: ") 
    print(str(user_guess)) # outside of while loop but inside function
    return user_guess

def contains_char(secret_word:str, char_guess: str) -> bool:
    """Determines whether character can be found in word"""
    assert len(char_guess) == 1
    index: int = 0 # use index to prevent 
    while index < len(secret_word):
        if secret_word[index] == char_guess:
            return True
        else:
            index += 1
    return False # function will exit after return statement so must be outside while loop

def emojified(guess:str, secret:str) -> str:
    """Uses emojis to determine accuracy of guess"""
    assert len(guess) == len(secret), "Guess must be same length as secret."
    WHITE_BOX:str = "\U00002B1C" # begin by defining variables
    GREEN_BOX:str = "\U0001F7E9"
    YELLOW_BOX:str = "\U0001F7E8"
    index:int = 0 # index will allow us to test every letter individually
    result:str = "" # add on to each emoji
    while index < len(guess):
        if guess[index] == secret[index]:
            result += GREEN_BOX
        elif contains_char(secret, guess[index]): # allows us to check for every instance
            result += YELLOW_BOX
        else:
            result += WHITE_BOX 
        index += 1 # check the next letter
    return result

def main(secret:str) -> None:
    """The entrypoint of the program and main game loop."""
    turn:int = 1 # variable for number of guesses
    while turn <= 6:
        print(f"=== Turn { turn }/6 ===")
        user_guess = input_guess(len(secret)) # call other functions
        result_emoji = emojified(user_guess,secret)
        print(f"Result: { result_emoji }")

        if user_guess == secret:
            print(f"You won in {turn}/6 turns!")
            return
        turn += 1 # code will reach this line if guess is not correct

    print(f"X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main(secret="donut")

