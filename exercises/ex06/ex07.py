"""Disgusting user tests for my ex06 class."""

import pytest
from ex06 import invert, count, favorite_color, alphabetizer, update_attendance

__author__ = "730720671"


# Tests for the invert function
def test_invert():
    """Checks for inversion in dict."""
    assert invert({'a': 'b', 'c': 'd'}) == {'b': 'a', 'd': 'c'}


def test_furtherinvert():
    """Invert but with more items."""
    assert invert({'hello': 'world', 'python': 'code'}) == {'world': 'hello', 'code': 'python'}


def test_errorinvert():
    """IFTHEREAREDUPLICATESWITHIN THE DICTIONARY THEN IT IS GOING TO CHECK FOR THIS."""
    with pytest.raises(KeyError):
        invert({'key1': 'value', 'key2': 'value'})


# Tests for favorite_color
def test_favorite_color():
    """Finds most common color."""
    assert favorite_color({'Alice': 'blue', 'Bob': 'green', 'Charlie': 'blue'}) == 'blue'


def test_favorite_color_multiple():
    """Handles tie by choosing first."""
    assert favorite_color({'Alice': 'green', 'Bob': 'green', 'Charlie': 'blue', 'David': 'blue'}) == 'green'


def test_favorite_color_empty():
    """Empty dict gives empty string."""
    assert favorite_color({}) == ''


# Tests for count
def test_count_varied():
    """Tally list with varied elements."""
    assert count(['apple', 'banana', 'apple', 'cherry', 'banana', 'cherry', 'cherry']) == {'apple': 2, 'banana': 2, 'cherry': 3}


def test_count_empty_list():
    """Tests Empty list gives empty dict."""
    assert count([]) == {}


def test_count_single_elem():
    """Single element list counted right."""
    assert count(['only', 'only', 'only']) == {'only': 3}


# Tests for alphabetizer
def test_alphabetizer_simple():
    """Categorize words by starting letter."""
    assert alphabetizer(['apple', 'banana', 'apricot', 'cherry']) == {'a': ['apple', 'apricot'], 'b': ['banana'], 'c': ['cherry']}


def test_alphabetizer_empty_list():
    """Empty list gives empty dict."""
    assert alphabetizer([]) == {}


def test_alphabetizer_case_sens():
    """Case-insensitive sorting."""
    assert alphabetizer(['Apple', 'banana', 'Apricot', 'cherry']) == {'a': ['Apple', 'Apricot'], 'b': ['banana'], 'c': ['cherry']}


# Tests for update_attendance
def test_update_attendance_exist():
    """Adds name to existing date."""
    log = {'2023-10-01': ['Alice', 'Bob']}
    assert update_attendance(log, '2023-10-01', 'Charlie') == {'2023-10-01': ['Alice', 'Bob', 'Charlie']}


def test_update_attendance_new_day():
    """Adds new date with name."""
    log = {'2023-10-01': ['Alice', 'Bob']}
    assert update_attendance(log, '2023-10-02', 'Charlie') == {'2023-10-01': ['Alice', 'Bob'], '2023-10-02': ['Charlie']}


def test_update_attendance_empty_log():
    """Handles an empty log correctly."""
    assert update_attendance({}, '2023-10-01', 'Alice') == {'2023-10-01': ['Alice']}