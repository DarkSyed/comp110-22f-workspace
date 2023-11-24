def mim_letter(my_words: str, letter_idx: int):
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx >= len(my_words):
        return ("index too high")
    #if we made it here, that meaans the letter_idx is valid
    return my_words[letter_idx]

def f(x: int) -> int:
    return x
    print(x)
    x *= 2
    

y: int = f(3)

