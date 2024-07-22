###
# Tests. Don't mess with this code, just run it in the terminal by typing "pytest ex2_string_exercises.py"
###

def test_hello():
    assert say_hello("Alice") == "Hello, Alice!"
    assert say_hello("Bob") == "Hello, Bob!"
    assert say_hello("Charlie") == "Hello, Charlie!"
    assert say_hello("") == "Hello, David!"


def test_double_the_string():
    assert double_the_string("Hello") == "HelloHello"
    assert double_the_string("World") == "WorldWorld"
    assert double_the_string("Python") == "PythonPython"
    assert double_the_string("") == ""
    assert double_the_string("#!#AbC") == "#!#AbC#!#AbC"


def test_reverse_string():
    assert reverse_string("Hello") == "olleH"
    assert reverse_string("World") == "dlroW"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""
    assert reverse_string("#!#AbC") == "CbA#!#"



def test_count_the_es():
    assert count_the_es("Hello") == 1
    assert count_the_es("World") == 0
    assert count_the_es("Earth") == 1
    assert count_the_es("eeeee") == 5
    assert count_the_es("EeEeEe") == 6

