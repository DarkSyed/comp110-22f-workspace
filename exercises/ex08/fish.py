"""Fish class, which will be imported in other classes."""


class Fish:
    """A class to rep a lefish in tha river."""

    def __init__(a_fish):
        """Initialize new fish."""
        a_fish.age = 0

    def one_day(a_fish):
        """A day in the life of fish, aging."""
        a_fish.age += 1

    def __str__(a_fish):
        """Return a string representation of the fish, primarily his age."""
        return f"LeFish, Age: {a_fish.age} days"