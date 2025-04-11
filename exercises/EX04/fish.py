"""File to define Fish class."""

__author__ = 730705450


class Fish:
    """Class that shows the activity of each fish in the water."""

    age: int

    def __init__(self):
        """Initializes age."""
        self.age = 0
        return None

    def one_day(self):
        """Age of each fish increases by one each day."""
        self.age += 1
        return None
