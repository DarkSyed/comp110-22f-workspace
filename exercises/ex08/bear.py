"""This assignment reminds me of my old java projects."""

class Bear:
    """A class to represent a bear living near a river."""
    
    def __init__(me):
        # Initialize new bear
        me.hunger_score = 0
        me.age = 0


    def one_day(me):
        # Each day, the bear ages and gets hungrier
        me.age += 1
        me.hunger_score -= 1

    def eat(me, num_fish: int):
        # Bear eats fish, reducing hunger
        me.hunger_score += num_fish

    def __str__(me):
        """Return a string representation of our bear."""
        return f"{me.__init__}, Age: {me.one_day:.2f} years, Fullness: {me.eat}"