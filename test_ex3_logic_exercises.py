import pytest
from ex3_logic_exercises import is_bigger_than_100, is_even, is_even_and_bigger_than_100, includes_e, hot_cold_mild

def test_is_bigger_than_100():
    assert is_bigger_than_100(101) == True
    assert is_bigger_than_100(100) == False
    assert is_bigger_than_100(99) == False

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True

def test_is_even_and_bigger_than_100():
    assert is_even_and_bigger_than_100(102) == True
    assert is_even_and_bigger_than_100(101) == False
    assert is_even_and_bigger_than_100(99) == False

def test_includes_e():
    assert includes_e("Hello") == True
    assert includes_e("World") == False
    assert includes_e("Python") == True

def test_is_hot():
    assert hot_cold_mild(35) == "hot"
    assert hot_cold_mild(30) == "hot"
    assert hot_cold_mild(25) == "mild"
    assert hot_cold_mild(29) == "mild"
    assert hot_cold_mild(15) == "mild"
    assert hot_cold_mild(10) == "cold"
    assert hot_cold_mild(14) == "cold"
