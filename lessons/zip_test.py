"""Test my functions in zip!"""

__author__ = "730720671"

from lessons.zip import zip


def test_empty_lists() -> None:
    """Edge case, test with two empty lists."""
    assert zip([], []) == {}, "Expected empty dictionary with two empty lists"


def test_equal_length() -> None:
    """Use case, tests to see if the two lists are going to be of equal lengths."""
    assert zip(["Happy", "Tuesday"], [1, 2]) == {"Happy": 1, "Tuesday": 2}, "Expected dictionary with keys from first list and values from second list"


def test_diff_length_lists() -> None:
    """Also use case but sees if they are of two different lengths among the lists."""
    assert zip(["Happy", "Tuesday", "Wednesday"], [1, 2]) == {}, "Expected empty dictionary because lists are different lengths"


def test_nonempty_equal_lists() -> None:
    """Use case, tests the functions within zip with non-empty lists of equal lengths."""
    assert zip(["Happy", "Tuesday", "Wednesday"], [1, 2, 3]) == {"Happy": 1, "Tuesday": 2, "Wednesday": 3}, "Expected dictionary to zip lists of same length"


def run() -> None:
    """Runs the tests."""
    test_functions = [
        test_empty_lists,
        test_equal_length,
        test_diff_length_lists,
        test_nonempty_equal_lists
    ]
    for test_function in test_functions:
        test_function()
        print(f"{test_function.__name__} passed.")


if __name__ == "__main__":
    run()