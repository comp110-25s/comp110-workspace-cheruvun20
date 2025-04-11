"""A game of Wordle with up to 6 guesses"""

__author__: str = "730705450"


def contains_char(string_search: str, single_letter: str) -> bool:
    """This is a function that tests whether the character inputted is found in the target word"""
    assert len(single_letter) == 1, f"len({single_letter}) is not 1"
    idx: int = 0
    while idx < len(string_search):
        if string_search[idx] == single_letter:
            return True
        idx = idx + 1
    return False


def emojified(guess: str, secret: str) -> str:
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret), "Guess must be same length as secret"
    idx: int = 0
    string: str = ""
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            string = string + GREEN_BOX
        elif contains_char(secret, guess[idx]):
            string = string + YELLOW_BOX
        else:
            string = string + WHITE_BOX
        idx = idx + 1
    return string


def input_guess(expected_length: int) -> str:
    guess = input(f"Enter a {expected_length} character word")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again!")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    secret_length: int = len(secret)
    user_turn: int = 0
    current_guess: str = ""

    while user_turn < 6:
        user_turn += 1
        print(f"=== Turn {user_turn}/6 ===")
        current_guess = input_guess(secret_length)
        print(emojified(current_guess, secret))
        if current_guess == secret:
            print(f"You won in {user_turn}/6 turns!")
            return

    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")