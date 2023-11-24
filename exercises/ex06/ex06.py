"""Utilizing Dictionaries!"""

__author__ = "730720671"

def invert(didi: dict [str, str]) -> dict[str, str]:
    """Inverts values within our dictionary."""
    # Creates empty dictionary with the for loop inverting the values in dictionary
    empty_dict: dict[str, str] = {}

    for keys, values, in didi.items():
        empty_dict[values] = keys
        if values in empty_dict:
            raise KeyError("there are two of the same keys!")
        empty_dict[values] = keys 
    return empty_dict

def favorite_color(colors: dict[str, str]) -> str:
    """Determines which is the fav color."""
    color_count = {}
    most_frequent_color = None
    max_count = 0
    
    for name, color in colors.items():
        # Color frequency counter
        color_count[color] = color_count.get(color, 0) + 1

        # Check color is now the most frequent or if it's a tie, it's the first
        if color_count[color] > max_count or (color_count[color] == max_count and most_frequent_color is None):
            most_frequent_color = color
            max_count = color_count[color]

    return most_frequent_color

def count(list_1: list[str]) -> dict[str, int]:
     """Count function."""
     empty_dict2: dict [str, int] #instantiting empty dict

     for value in range(len(list_1)):
        if list_1[value] in empty_dict2:
            # If the item is already a key in the dictionary, increment its count
            empty_dict2[list_1[value]] += 1
        else:
            # If the item is not in the dictionary, add it with a count of 1
            empty_dict2[list_1[value]] = 1

     return empty_dict2

def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Alphabetizer for list."""
    cat_words = {}

    for word in word_list:
        # Convert the first letter to lower case
        lowercase_w = word.lower()
        first_l = lowercase_w[0]
        if first_l in cat_words:
            cat_words[first_l].append(word)
        else:
            cat_words[first_l] = [word]

    return cat_words 

def update_attendance(att_log: dict[str, list[str]], day: str, student_name: str) -> dict[str, list[str]]:
    """Check for attendance!"""
    # Check if day is in dictionary
    if day in att_log:
        # Append the student to the list 
        if student_name not in att_log[day]:
            att_log[day].append(student_name)
    else:
        # Creates entry for the day with the student in the new list written below V
        att_log[day] = [student_name]
    
    return att_log
