"""EX05 Dictionary Unit Tests"""

__author__:str = "730912786"

#Import functions from ex04
from exercises.ex04.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest #Needed for testing exceptions

"""Unit tests for dictionary functions."""

"""Invert function tests.""" #Three unit tests for invert
def test_invert_basic1() -> None:
    """Test invert more than one unique key values."""
    data = {'a': '1', 'b': '2', 'c': '3'}
    #Each key-value pair should be swapped so that keys become values and values become keys
    assert invert(data) == {'1': 'a', '2': 'b', '3': 'c'}
def test_invert_basic2() -> None:
    """Test invert with only one key value pair."""
    data = {'x': 'y'}
    # Single key-value pair should be swapped
    assert invert(data) == {'y': 'x'}
def test_invert_keyerror() -> None:
    """Test that invert raises KeyError on duplicate values."""
    data = {'a': '1', 'b': '2', 'c': '1'}
    # Expect KeyError because '1' would become a duplicate key after inversion
    with pytest.raises(KeyError):
        invert(data)    
    
"""favorite_color function tests.""" #Three unit tests for favorite_color
def test_favorite_color_mostcommon() -> None:
    """Test that favorite_color returms most common color."""
    data = {'Sarah': 'green', 'Carol': 'purple', 'John': 'green'}
    #'green' appears most frequently and should be returned
    assert favorite_color(data) == 'green'
def test_favorite_color_empty() -> None:
    """Test that favorite_color returns empty string for empty dict."""
    data = {}
    #An empty dictionary should return an empty string
    assert favorite_color(data) == ''
def test_favorite_color_tie() -> None:
    """Test that favorite_color returns first color in case of tie."""
    data = {'Sarah': 'green', 'Carol': 'purple', 'John': 'red'}
    #All the colors appear once, so 'green' should be returned since it appears first
    assert favorite_color(data) == 'green'

"""count function tests.""" #Three unit tests for count
def test_count_basic() -> None:
    """Test count with multiple occurrences."""
    data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    #Function should count occurrences of each string correctly
    assert count(data) == {'apple': 3, 'banana': 2, 'orange': 1}
def test_count_empty() -> None:
    """Test count with empty list."""
    data = []
    #Function should return empty dictionary for empty list
    assert count(data) == {}
def test_count_single() -> None:
    """Test count with single occurrence of each item."""
    data = ['apple', 'banana', 'orange']
    #Function should count each string as occurring once
    assert count(data) == {'apple': 1, 'banana': 1, 'orange': 1}

"""alphabetizer function tests.""" #Three unit tests for alphabetizer
def test_alphabetizer_basic() -> None:
    """Test words are organized by first letter."""
    data = ['banana', 'apple', 'apricot', 'blueberry', 'cherry']
    #Words should be grouped into lists by their starting letter and maintain order
    assert alphabetizer(data) == {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
def test_alphabetizer_case() -> None:
    """Test alphabetizer is case insensitive."""
    data = ['Banana', 'apple', 'Apricot', 'blueberry', 'Cherry']
    #Grouping should not be affected by capitalization
    assert alphabetizer(data) == {'a': ['apple', 'Apricot'], 'b': ['Banana', 'blueberry'], 'c': ['Cherry']}
def test_alphabetizer_empty() -> None:
    """Test alphabetizer with empty list."""
    data = []
    #Empty list should return empty dictionary
    assert alphabetizer(data) == {}

"""update_attendance function tests.""" #Three unit tests for update_attendance
def test_update_attendance_basic() -> None:
    """Test update_attendance adds new student with attendance."""
    data = {"Monday": [Sarah]}
    #Carol should be added to Monday's attendance list
    update_attendance(data, "Monday", "Carol")
    assert data == {"Monday": [Sarah, Carol]}
def test_update_attendance_new_day() -> None:
    """Test update_attendance adds new day with student."""
    data = {"Monday": [Sarah]}
    #Tuesday should be created with Carol in its attendance list
    update_attendance(data, "Tuesday", "Carol")
    assert data == {"Monday": [Sarah], "Tuesday": [Carol]}
def test_update_attendance_existing_student() -> None:
    """Test update_attendance does not duplicate existing student."""
    data = {"Monday": [Sarah]}
    #Sarah is already in Monday's attendance list, so no change should occur
    update_attendance(data, "Monday", "Sarah")
    assert data == {"Monday": [Sarah]}
