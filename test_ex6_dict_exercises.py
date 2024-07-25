import ex6_dict_exercises as ex6

# Test for the create_alphabet_dict function
def test_create_alphabet_dict():
    assert ex6.create_alphabet_dict(["apple", "banana", "carrot"]) == {'a': 'apple', 'b': 'banana', 'c': 'carrot'}
    assert ex6.create_alphabet_dict(["python", "java", "c"]) == {'p': 'python', 'j': 'java', 'c': 'c'}
    assert ex6.create_alphabet_dict(["hello", "world", "python"]) == {'h': 'hello', 'w': 'world', 'p': 'python'}

# Test for the create_word_length_dict function
def test_create_word_length_dict():
    assert ex6.create_word_length_dict(["apple", "banana", "carrot"]) == {'apple': 5, 'banana': 6, 'carrot': 6}
    assert ex6.create_word_length_dict(["python", "java", "c"]) == {'python': 6, 'java': 4, 'c': 1}
    assert ex6.create_word_length_dict(["hello", "world", "python"]) == {'hello': 5, 'world': 5, 'python': 6}
    assert ex6.create_word_length_dict(["", "!", "22"]) == {'': 0, '!': 1, '22': 2}

# Test for the divisible_by_3_dict function
def test_divisible_by_3_dict():
    assert ex6.divisible_by_3_dict(5) == {1: False, 2: False, 3: True, 4: False, 5: False}
    assert ex6.divisible_by_3_dict(10) == {1: False, 2: False, 3: True, 4: False, 5: False, 6: True, 7: False, 8: False, 9: True, 10: False}
    assert ex6.divisible_by_3_dict(1) == {1: False}
    assert ex6.divisible_by_3_dict(0) == {}