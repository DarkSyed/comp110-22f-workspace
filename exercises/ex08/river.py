"""The most annoying class that I had to make."""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

__author__ = "730720671"


class River:
    """A class to represent the river where the Fish and Bear populations Live and Thrive."""

    def __init__(me, num_fish: int, num_bears: int):
        """Initializes the river with fish and bears."""
        me.day = 0
        me.bears = [Bear() for _ in range(num_bears)]
        me.fish = [Fish() for _ in range(num_fish)]

    def check_ages(me):
        """Remove the older Fish and Bears. Old."""
        me.bears = [bear for bear in me.bears if bear.age <= 5]
        me.fish = [fish for fish in me.fish if fish.age <= 3]

    def bears_eating(me):
        """Bears eat fish if available."""
        for bear in me.bears:
            if len(me.fish) >= 5:
                me.remove_fish(3)
                bear.eat(3)

    def check_hunger(me):
        """Remove hungry Bears."""
        me.bears = [bear for bear in me.bears if bear.hunger_score >= 0]

    def view_river(me):
        """Print function for displaying the state of the river."""
        print(f"~~~ Day {me.day}: ~~~")
        print(f"Fish population: {len(me.fish)}")
        print(f"Bear population: {len(me.bears)}")

    def repopulate_fish(me):
        """Adds new Fish to the river."""
        new_fish = (len(me.fish) // 2) * 4
        me.fish.extend([Fish() for _ in range(new_fish)])

    def repopulate_bears(me):
        """Adds new Bears to the river."""
        new_bears = len(me.bears) // 2
        me.bears.extend([Bear() for _ in range(new_bears)])

    def one_river_day(me):
        """Simulates one day in the river!"""
        me.day += 1
        for fish in me.fish:
            fish.one_day()
        for bear in me.bears:
            bear.one_day()
        me.bears_eating()
        me.check_hunger()
        me.check_ages()
        me.repopulate_fish()
        me.repopulate_bears()
        me.view_river()

    def remove_fish(me, num_fish: int):
        """Remove a specific number of fish from the river."""
        me.fish = me.fish[num_fish:]

    def one_river_week(me):
        """Simulates one week in the river!"""
        for _ in range(7):
            me.one_river_day()