"""This is cq07 for classes."""

from __future__ import annotations


__author__ = "730720671"


class Point:
    """A point on a 2D surface :)!"""

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0) -> None:
        """Initializes x and y values as shown in the arguments."""        
        self.x = x_init
        self.y = y_init

    def __str__(self) -> str:
        """Returns the two float var in __init__ arguments."""
        return f"x: {self.x}; y: {self.y}"

    def __mul__(self, factor: int | float) -> Point:
        """Overloads the * operator to scale the point."""
        return self.scale(factor)

    def __add__(self, factor: int | float) -> Point:
        """Overloads the + operator to add to the point."""
        return Point(self.x + factor, self.y + factor)

    def scale_by(self, factor: float) -> None:
        """Mutating method."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: float) -> Point:
        """Non-mutating method, Returns a new Point."""
        return Point(self.x * factor, self.y * factor)


# Testing it for idek how many times
point1 = Point()  
print(point1)  

point2 = Point(2.0, 1.0)
print(point2)