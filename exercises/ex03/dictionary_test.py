"""This program allows for practice with unit tests"""

__author__: str = "730705450"


import pytest
from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert_edge_empty():
    """Invert an empty dictionary should return empty dictionary."""
    assert invert({}) == {}


def test_invert_use_case_1():
    """Invert a normal dictionary with unique values."""
    assert invert({"a": "z", "b": "y"}) == {"z": "a", "y": "b"}


def test_invert_raises_key_error():
    """Invert with duplicate values should raise KeyError."""
    with pytest.raises(KeyError):
        invert({"a": "x", "b": "x"})


def test_count_edge_empty():
    """Counting an empty list should return empty dict."""
    assert count([]) == {}


def test_count_use_case_1():
    """Counting multiple same items in list."""
    assert count(["a", "a", "b"]) == {"a": 2, "b": 1}


def test_count_use_case_2():
    """Counting all unique items."""
    assert count(["x", "y", "z"]) == {"x": 1, "y": 1, "z": 1}


def test_favorite_color_empty_dict() -> None:
    """Edge case: an empty dictionary should return an empty string."""
    assert favorite_color({}) == ""


def test_favorite_color_simple_case() -> None:
    favorites = {"Alice": "blue", "Bob": "red", "Charlie": "blue"}
    assert favorite_color(favorites) == "blue"


def test_favorite_color_tie_breaker() -> None:
    """Use case: when there is a tie, return the color that was encountered first."""
    favorites = {"Alice": "green", "Bob": "red", "Charlie": "green", "David": "red"}
    assert favorite_color(favorites) == "green"


def test_bin_len_edge_empty():
    """Binning empty list returns empty dictionary."""
    assert bin_len([]) == {}


def test_bin_len_use_case_1():
    """Binning strings of varying lengths."""
    assert bin_len(["hi", "hello", "hey"]) == {2: {"hi"}, 5: {"hello"}, 3: {"hey"}}


def test_bin_len_duplicates():
    """Duplicate strings should not repeat in set."""
    assert bin_len(["a", "a", "ab"]) == {1: {"a"}, 2: {"ab"}}
