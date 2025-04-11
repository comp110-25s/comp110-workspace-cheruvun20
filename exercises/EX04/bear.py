"""File to define Bear class."""

__author__ = 730705450


class Bear:
    """Class that shows the activity of each bear in the river."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes age and hunger_score."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Age of each bear increased by one each day and decreases each bears' hunger_score by one each day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Adds however many fish each bear eats to the bear's hunger score."""
        self.hunger_score += num_fish
        return None
