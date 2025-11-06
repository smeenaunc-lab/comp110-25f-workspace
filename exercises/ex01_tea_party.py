def check_first_letter(word: str, letter: str) -> str:
    """Checks if the first letter of a word matches the given letter."""
    if len(letter) != 1:
        return "letter's argument should be one character!"
    elif word[0] == letter:
        return "match!"
    else:
        return "no match!"
