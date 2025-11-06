"""List utility functions assingment"""

__author__: str = "730912786"


def all(my_list: list[int], number: int) -> bool:
    """Checks if all integers in a list are the same as the given number."""
    if len(my_list) == 0:
        return False
    i: int = 0
    while i < len(my_list):
        if my_list[i] != number:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Returns the largest integer in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 1
    largest: int = input[0]
    while i < len(input):
        if input[i] > largest:
            largest = input[i]
        i += 1
    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if two lists are exactly the same."""
    if len(list1) != len(list2):
        return False
    i: int = 0
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1
    return True

