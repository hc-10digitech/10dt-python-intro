# Tests. Don't mess with this code, just run it in the terminal by typing "pytest ex1_number_exercises.py"
def test_add_two_numbers():
    assert add_two_numbers(1, 2) == 3
    assert add_two_numbers(0, 0) == 0
    assert add_two_numbers(-1, 1) == 0
    assert add_two_numbers(-1, -1) == -2
    

def test_multiply_two_numbers():
    assert multiply_two_numbers(1, 2) == 2
    assert multiply_two_numbers(0, 0) == 0
    assert multiply_two_numbers(-1, 1) == -1
    assert multiply_two_numbers(-1, -1) == 1


def test_which_is_greater():
    assert which_is_greater(2, 1) == 2
    assert which_is_greater(0, 0) == 0
    assert which_is_greater(-1, 1) == 1
    assert which_is_greater(-1, -1) == -1
    assert which_is_greater(-10, -20) == -10


def test_difference_between_numbers():
    assert difference_between_numbers(1, 2) == 1
    assert difference_between_numbers(0, 0) == 0
    assert difference_between_numbers(-1, 5) == 6
    assert difference_between_numbers(-1, -1) == 0
    assert difference_between_numbers(5, -1) == 6
    assert difference_between_numbers(1000, 2) == 998

def test_raise_to_power():
    assert raise_to_power(2, 3) == 8
    assert raise_to_power(2, 0) == 1   
    assert raise_to_power(0, 0) == 1
    assert raise_to_power(0, 1) == 0
    assert raise_to_power(3, -1) == 1/3
    assert raise_to_power(3, -2) == 1/9
    assert raise_to_power(-4, 2) == 16
    assert raise_to_power(-2, 3) == -8