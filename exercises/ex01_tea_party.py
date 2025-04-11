"""A program to help plan a cozy tea party."""

__author__: str = "730705450"


def main_planner(guests: int) -> None:
    """Bringing all functions together."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))
    return None


def tea_bags(people: int) -> int:
    """How many tea bags needed."""
    return people * 2


def treats(people: int) -> int:
    """How many treats needed based on number of teas."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """How much tea bags and treats cost altogether."""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
