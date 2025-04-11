"""This program allows for practice with dictionary functions"""

__author__: str = "730705450"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Ïnverts keys and values of a dictionary."""
    result = {}
    for key, value in d.items():
        if value in result:
            raise KeyError(f"Duplicate key when inverting: {value}")
        result[value] = key
    return result


def count(values: list[str]) -> dict[str, int]:
    """Counts the frequency of each string in the list."""
    result = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def favorite_color(favorites: dict[str, str]) -> str:
    """Returns the color that appears most frequently."""
    color = list(favorites.values())
    if not color:
        return ""
    color_count = count(color)
    max_count = max(color_count.values())
    for color in color_count:
        if color_count[color] == max_count:
            return color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Bins strings by their length into a dictionary."""
    result: dict[int, set[str]] = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = set()
        result[length].add(word)
    return result
