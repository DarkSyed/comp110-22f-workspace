"""Utilizing Dictionaries!"""

__author__ = "730720671"


def invert(didi: dict[str, str]) -> dict[str, str]:
    """Inverts values within our dictionary."""
    inverted_dict: dict[str, str] = {}
    for key, value in didi.items():
        if value in inverted_dict:
            raise KeyError("Duplicate value found during inversion!")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(colors: dict[str, str]) -> str:
    """Determines which is the fav color."""
    color_count: dict[str, int] = {}
    most_frequent_color: str = ""  # Initialized to be an empty string to ensure return type is a string
    max_count: int = 0

    for name, color in colors.items():
        color_count[color] = color_count.get(color, 0) + 1

        if color_count[color] > max_count or (color_count[color] == max_count and not most_frequent_color):
            most_frequent_color = color
            max_count = color_count[color]

    return most_frequent_color


def count(list_1: list[str]) -> dict[str, int]:
    """Count function."""
    count_dict: dict[str, int] = {}  # Changed variable name for consistency

    for value in list_1:
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1

    return count_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Alphabetizer for list."""
    categorized_words: dict[str, list[str]] = {}  # Changed variable name for clarity

    for word in word_list:
        first_letter = word[0].lower()  # Simplified variable names
        if first_letter not in categorized_words:
            categorized_words[first_letter] = []
        categorized_words[first_letter].append(word)

    return categorized_words


def update_attendance(att_log: dict[str, list[str]], day: str, student_name: str) -> dict[str, list[str]]:
    """Check for attendance!"""
    if day in att_log:
        if student_name not in att_log[day]:
            att_log[day].append(student_name)
    else:
        att_log[day] = [student_name]

    return att_log