"""File to define River class."""

__author__ = 730705450

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """Shows the activity and interactions between the bears and the fish in the river."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Creates new list for both bear and fish class and then removes each bear that's older than 5, and removes each fish that's older than 3 from the bear and fish class respectively."""
        newB_list[Bear] = self.bears
        newF_list[Fish] = self.fish
        for bear in self.bears:
            if bear.age < 5:
                newB_list.append(bear)
            self.bears = newB_list

        for fish in self.fish:
            if fish.age < 3:
                newF_list.append(fish)
            self.fish = newF_list

        return None

    def remove_fish(self, amount: int):
        """Removes amount of fish in self.fish from the beginning of the list."""
        for num in range(0, amount):
            self.fish.pop(num)
        return None

    def bears_eating(self):
        """If there are 5 or more fish, then the bear eats 3 of them and the 3 fish are removed from the population of fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """If a bear's hunger_score is below 0, then the bear is removed from the list."""
        newB_list2: list[Bear] = self.bears
        for bear in self.bears:
            if bear.hunger_score > 0:
                newB_list2.append(bear)
        self.bears = newB_list2
        return None

    def repopulate_fish(self):
        """Adds 4 fish to the self.fish list for each pair of fish there is."""
        n: int = (len(self.fish) // 2) * 4
        for _ in range(0, n):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Adds 1 bear to the self.bears list for each pair of fish there is."""
        n: int = len(self.bears) // 2
        for _ in range(0, n):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Prints the overview of the population and day in the river."""
        print(f"~~~Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()


def one_river_week(self):
    """Runs through one week in the river."""
    count: int = 0
    while count <= 7:
        self.one_river_day()
        count += 1
    return None
