"""turtle project, my drawing."""

from turtle import Turtle, Screen, colormode
import random

__author__ = "730720671"

leo: Turtle = Turtle()


def draw_rectangle(x: float, y: float, width: float, height: float, color: str) -> None:
    """Filled rectangle with dimensions and color."""
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.color(color)
    leo.begin_fill()
    for _ in range(2):
        leo.forward(width)
        leo.left(90)
        leo.forward(height)
        leo.left(90)
    leo.end_fill()


def draw_moon(x: float, y: float, size: float, radius: float, color: str) -> None:
    """This will be the moon!"""
    leo.penup()
    leo.goto(x, y)
    leo.pendown()
    leo.color(color)
    leo.begin_fill()
    leo.circle(radius)
    leo.end_fill()


def draw_star(x: float, y: float, size: float) -> None:
    """Draws a five pointed star from this function."""
    leo.penup()
    leo.goto(x, y)
    leo.setheading(-72)
    leo.pendown()
    leo.color("white")
    for _ in range(5):
        leo.forward(size)
        leo.right(144)
        leo.forward(size)
        leo.left(72)


def draw_smiley_face(x: float, y: float, radius: float) -> None:
    """Draw a smiley face."""
    eye_radius = radius // 5
    eye_distance = radius // 2.5

    # Left Eye
    leo.penup()
    leo.goto(x - eye_distance, y + eye_distance)
    leo.pendown()
    leo.color("black")
    leo.begin_fill()
    leo.circle(eye_radius)
    leo.end_fill()

    # Right Eye
    leo.penup()
    leo.goto(x + eye_distance, y + eye_distance)
    leo.pendown()
    leo.color("black")
    leo.begin_fill()
    leo.circle(eye_radius)
    leo.end_fill()

    # Draws the smile, set heading function makes it so that the smile can be angled properly
    leo.width(5)
    leo.penup()
    leo.goto(x - eye_distance, y - eye_distance / 4)
    leo.setheading(-60)
    leo.pendown()
    leo.circle(eye_distance, 120)


def main() -> None:
    """The Main Function. Entrance to the Turtle Scene."""
    output = Screen()
    output.bgcolor("black")
    colormode(255)
    leo.speed(5)  # Supa Sonic Drawing Speed

    # Blue ocean at the bottom
    draw_rectangle(-400, -300, 800, 150, "blue")

    # Drawing the moon
    draw_moon(0, 0, 60, 80, "white")

    # Drawing the Moon's Craters
    i: int = 0
    x = 0
    y = 0
    while (i < 3):
        draw_moon(x, y, 20, 10, "gray")
        x = random.randint(-10, 50)
        y = random.randint(0, 55)
        i += 1 

    # Random Stars
    for _ in range(14):  # The number of stars that are drawn
        x = random.randint(-290, 290)
        y = random.randint(-90, 290)
        draw_star(x, y, 20)
    
    # Drawing a smiley face cuz why not
    draw_smiley_face(-10, 40, 60)

    output.mainloop()  


if __name__ == "__main__":
    main()