"""EX02 - Wordle - A cute step toward Wordle."""

__author__ = "730720671"


emoji: str = "\U0001F920\U0001F40E"
secret_word: str = "python"
lenser = len(secret_word)


## Characters for wordle
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

wordle: str = input(f"What is your {lenser} letter guess? ")

while len(wordle) != len(secret_word):
    wordle = input("That was not 6 letters! Try again: ")


counter = 0
answer = " "

while counter < lenser:
    if wordle[counter] == secret_word[counter]:
        answer = f"{answer}{green_box}" 
    else:
        position = False
        counter_two = 0
        
        while not position and counter_two < lenser:
            if wordle[counter] == secret_word[counter_two]:
                position = True 
            counter_two += 1
        if position:

            answer = f"{answer}{yellow_box}" 
        else:

            answer = f"{answer}{white_box}" 
    counter += 1
print(answer)


if wordle == secret_word:
    print("Woo! You got it! ")
else:
    print(f"Not quite {emoji}. Play again soon!")