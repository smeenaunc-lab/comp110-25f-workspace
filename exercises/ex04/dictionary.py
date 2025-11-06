"EX04 Dictionary Utility Functions"

__author__: str = "730912786"


def invert(my_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary."""
    result: dict[str, str] = (
        {}
    )  # Initialiaze an empty dictionary to store the inverted key-value pairs
    for (
        key,
        value,
    ) in my_dict.items():  # Iterate through each key-value pair in the input dictionary
        if (
            value in result
        ):  # Check if the value already exists as a key in the result dictionary
            raise KeyError(
                f"Duplicate key found when inverting: {value}"
            )  # Raise error on duplicate keys after inversion
        result[value] = (
            key  # Invert the pair so that the value becomes the key, and the key becomes the value
        )
    return result  # Return the inverted dictionary


def favorite_color(my_dict: dict[str, str]) -> str:
    """Returns the color that appears most frequently in the dictionary."""
    color_count: dict[str, int] = {}  # Dictionary to count occurrences of each color
    for (
        color
    ) in my_dict.values():  # Iterate through all the colors in the input dictionary
        if color in color_count:  # If the color already counted, increment its count
            color_count[color] += 1
        else:
            color_count[color] = 1  # Otherwise, start counting this color with 1
    # Find the color with the highest frequency
    max_count: int = 0
    most_frequent: str = ""
    for name in my_dict:  # Iterate over the original dictionary keys to preserve order
        color = my_dict[name]  # Get the color associated with the current name
        if (
            color_count[color] > max_count
        ):  # If this color's count is greater than max_count found so far...
            max_count = color_count[color]  # Update max_count to new count
            most_frequent = color  # Update the most frequent color accordingly
    return most_frequent  # Return the color that appeared most frequently


def count(values: list[str]) -> dict[str, int]:
    """Counts the occurrences of each string in a list."""
    result: dict[str, int] = {}  # Dictionary to store counts of each unique string
    for item in values:  # Iterate through each item in the list
        if item in result:  # If the item is already counted, increment its count
            result[item] += 1
        else:
            result[item] = 1  # Otherwise, initialize its count to 1
    return result  # Return the dictionary with counts


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Returns a list of words sorted in alphabetical order."""
    result: dict[str, list[str]] = (
        {}
    )  # Dictionary where keys are letters and values are lists of words
    for word in words:  # Iterate through each word in the input list
        key = word[
            0
        ].lower()  # Extract first letter and convert to lowercase to group without being case-sensitive
        if (
            key in result
        ):  # If the key already exists, append the word to the existing list
            result[key].append(word)
        else:
            result[key] = [
                word
            ]  # Otherwise, create a new list with the word as the first element
    return (
        result  # Return the dictionary grouping words by first letter and alphabetized
    )


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    """Updates the attendance log by adding a student to a specific day's list."""
    if (
        day in attendance_log
    ):  # Check if the day already exists in the attendance log dictionary
        if (
            student not in attendance_log[day]
        ):  # Only add if student is not already present
            attendance_log[day].append(student)
    else:  # Otherwise, create a new list for the day with the student
        attendance_log[day] = [student]
