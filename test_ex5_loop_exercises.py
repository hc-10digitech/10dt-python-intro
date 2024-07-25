import ex5_loop_exercises as ex5
# Test for the list_of function
def test_list_of():
    assert ex5.list_of("hello", 3) == ["hello", "hello", "hello"]
    assert ex5.list_of("test", 5) == ["test", "test", "test", "test", "test"]
    assert ex5.list_of("python", 0) == []
    assert ex5.list_of("python", 1) == ["python"]

# Test for the countdown function
def test_countdown():
    assert ex5.countdown(3) == "3 2 1 0"
    assert ex5.countdown(5) == "5 4 3 2 1 0"
    assert ex5.countdown(0) == "0"

# Test for the sum_of_squares function
def test_sum_of_squares():
    assert ex5.sum_of_squares(3) == 14
    assert ex5.sum_of_squares(5) == 55
    assert ex5.sum_of_squares(0) == 0

# Test for the factorial function
def test_factorial():
    assert ex5.factorial(3) == 6
    assert ex5.factorial(5) == 120
    assert ex5.factorial(0) == 1
    assert ex5.factorial(20) == 2432902008176640000