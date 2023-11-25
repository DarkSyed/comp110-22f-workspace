"""Combining two lists into a dictionairy."""

__author__ = "730720671"


def zip(list_1: list[str], list_2: list[int]) -> dict[str, int]:
    """Zip Function for lists and dictionairies."""
    # Return an empty dict if not equal
    if len(list_1) != len(list_2) or not list_1:
        return {}
    
    # if len(list_1) == len(list_2) or list_1:
    # didi: dict = {list_1, list_2}
    didi: dict[str, int] = {}

    for iter in range(len(list_1)):
        # ITEMS from list_1 are keys and list_2 as values to the dictionary
        didi[list_1[iter]] = list_2[iter]

    return didi
    
print(zip(["Happy", "Tuesday", "Wednesday"], [1, 2, 3]))
