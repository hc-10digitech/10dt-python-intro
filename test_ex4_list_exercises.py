import pytest
from ex4_list_exercises import length_of_list, get_second_element, get_sum_of_elements, get_last_element

def test_length_of_list():
    # Test with an empty list
    assert length_of_list([]) == 0

    # Test with a list of 1
    assert length_of_list([1]) == 1

    # Test with a list of integers
    assert length_of_list([1, 2, 3, 4, 5]) == 5

    # Test with a list of strings
    assert length_of_list(["apple", "banana", "cherry"]) == 3

def test_get_second_element():
    # Test with an empty list
    assert get_second_element([]) is None

    # Test with a list of integers
    assert get_second_element([1, 2, 3, 4, 5]) == 2

    # Test with a list of 2 items
    assert get_second_element([1, 0]) == 0
    # Test with a list of strings
    assert get_second_element(["apple", "banana", "cherry"]) == "banana"

def test_get_sum_of_elements():
    # Test with an empty list
    assert get_sum_of_elements([]) == 0

    # Test with a list of integers
    assert get_sum_of_elements([1, 2, 3, 4, 5]) == 15

    # Test with a list of negative integers
    assert get_sum_of_elements([-1, -2, -3, -4, -5]) == -15

def test_get_last_element():
    # Test with an empty list
    assert get_last_element([]) is None

    # Test with a list of one
    assert get_last_element([5]) == 5

    # Test with a list of integers
    assert get_last_element([1, 2, 3, 4, 5]) == 5

    # Test with a list of strings
    assert get_last_element(["apple", "banana", "cherry"]) == "cherry"