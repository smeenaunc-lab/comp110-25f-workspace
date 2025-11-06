"""COMP110 Exercise 2: Wordle"""

__author__: str = "730912786"

WHITE_BOX: str = "\U00002b1c"
GREEN_BOX: str = "\U0001f7e9"
YELLOW_BOX: str = "\U0001f7e8"


def input_guess(expected_length: int) -> str:
    """Makes sure the word that the user inputs is the correct length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def contains_char(word: str, single_character: str) -> bool:
    """Checks if a charater is found in the word that the player guessed."""
    assert len(single_character) == 1, f"len('{single_character}') is not 1"
    i: int = 0
    while i < len(word):
        if word[i] == single_character:
            return True
        else:
            i = i + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Shows emoji boxes based on correct guesses of letters."""
    assert len(guess) == len(secret), "Guess must be the same length as secret"
    result: str = ""
    i: int = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            result = result + GREEN_BOX
        elif contains_char(secret, guess[i]) == True:
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
        i = i + 1
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    won: bool = False
    while turn < 7 and won == False:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            won = True
        else:
            turn = turn + 1
    if won == True:
        print(f"You won in {turn}/6 turns!")
    else:
        print(f"X/6 - Sorry, try again tomorrow!")

    if __name__ == "__main__":
        main(secret="codes")
