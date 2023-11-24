"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730720671"

chardle_word: str = input("Enter a 5-character word: ")
chardle_count: int = 0

break_tool = len(chardle_word)

if (break_tool > 5):
    print("Error: Word must contain 5 characters")
    exit()


if (break_tool == 0):
    print("Error: Word must contain 5 characters")
    exit()

chardle_char: str = input("Enter a single character: ")

break_char = len(chardle_char)

if (break_char > 1):
    print("Error: Character must be a single character.")
    exit()


if (break_char == 0):
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + chardle_char + " in " + chardle_word)

if (chardle_word[0] == chardle_char):
    print(chardle_char + " found at index 0")
    chardle_count += 1 

if (chardle_word[1] == chardle_char):
    print(chardle_char + " found at index 1")
    chardle_count += 1  

if (chardle_word[2] == chardle_char):
    print(chardle_char + " found at index 2")
    chardle_count += 1 

if (chardle_word[3] == chardle_char):
    print(chardle_char + " found at index 3")
    chardle_count += 1 

if (chardle_word[4] == chardle_char):
    print(chardle_char + " found at index 4")
    chardle_count += 1 

if (chardle_count > 1):
    print(str(chardle_count) + " instances of " + chardle_char + " found in " + chardle_word)

if (chardle_count == 0):
    print("No" + " instances of " + chardle_char + " found in " + chardle_word)

if (chardle_count == 1):
    print(str(chardle_count) + " instance of " + chardle_char + " found in " + chardle_word)