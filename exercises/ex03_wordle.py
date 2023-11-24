"""EX03 - Wordle, Structured!"""

__author__ = "730720671"

"""Characters for wordle"""
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"


def contains_char(long_string: str, singular: str) -> bool:
    """This is the Character Container Function."""
    assert len(singular) == 1 
    str_idx = 0
    checker = False  # Initialized checker outside loop
    while str_idx < len(long_string):
        if singular == long_string[str_idx]:  # Check if singular is equal to the character at the current index
            checker = True
            return checker  # Exit the loop once a match is found
        str_idx += 1
    return checker
    # Check if a single character is present in a given string.

    # bool: True if sing_char is found in long_string, otherwise False.


def emojified(guess: str, secret: str) -> str:
    """This is the Emojified function that adds emojis."""
    assert len(guess) == len(secret)
    # Parameters:
    # guess (str): The guess string to be tested.
    # secret (str): The secret string used for comparison
    result: str = ""
    word_idx = 0
    while word_idx < len(secret):
        if guess[word_idx] == secret[word_idx]:
            result += green_box
        elif contains_char(secret, guess[word_idx]):
            result += yellow_box
        else:
            result += white_box
        word_idx += 1
    # loop checks that if the index is less than the length of our secret word, then it will index and determine if these words are in the wordle or not
    return result


def input_guess(expected_length: int) -> str:
    """Prompts the user to input a word of the given length, and loops until a word of the correct length is given."""
    while True:
        word_guess: str = input(f"Enter a {expected_length} character word: ")
        if len(word_guess) == expected_length:
            return word_guess
        print(f"That wasn't {expected_length} chars! Try again.")


def main() -> None:
    """The entry point of the program and main game loop."""
    secret_word: str = "codes"
    number_of_turns: int = 1
    while number_of_turns <= 6:
        print(f"=== Turn {number_of_turns}/6 ===")
        new_word: str = input_guess(len(secret_word))
        if len(new_word) != len(secret_word):
            print('not same length')
            return
        print(emojified(new_word, secret_word))
        if new_word != secret_word and number_of_turns == 6:
            print("X/6 - Sorry, try again tomorrow!")
        elif new_word == secret_word:
            print(f"You won in {number_of_turns}/6 turns!")
            return
        number_of_turns += 1


if __name__ == "__main__":
    main()