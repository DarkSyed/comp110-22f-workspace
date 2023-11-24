"""Summing the elements of a list using different loops!"""

__author__ = "730720671"

"""The functions."""


def w_sum(vals: list[float]) -> float:
    """The w_sum function."""
    counter = 0
    sum = 0.0
    while counter < len(vals):
        sum += vals[counter]
        counter += 1
    return sum


def f_sum(moreval: list[float]) -> float:
    """f_sum function morevals."""
    counter = 0
    sum = 0.0
    for x in moreval:
        sum += x
        counter += 1 
    return sum


def f_range_sum(evenmorevals: list[float]) -> float:
    """f_range_sum function."""
    sum = 0.0
    for x in evenmorevals:
        sum += x
    return sum