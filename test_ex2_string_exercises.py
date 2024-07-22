import ex2_string_exercises as ex2
###
# Tests. Don't mess with this code, just run it in the terminal by typing "pytest ex2_string_exercises.py"
###

def test_hello():
    assert ex2.say_hello("Alice") == "Hello, Alice!"
    assert ex2.say_hello("Bob") == "Hello, Bob!"
    assert ex2.say_hello("Charlie") == "Hello, Charlie!"
    assert ex2.say_hello("") == "Hello, David!"


def test_double_the_string():
    assert ex2.double_the_string("Hello") == "HelloHello"
    assert ex2.double_the_string("Python") == "PythonPython"
    assert ex2.double_the_string("") == ""
    assert ex2.double_the_string("#!#AbC") == "#!#AbC#!#AbC"
    assert ex2.double_the_string("World") == "WorldWorld"
    assert ex2.double_the_string("GitHub Copilot") == "GitHub CopilotGitHub Copilot"
    assert ex2.double_the_string("123") == "123123"
    assert ex2.double_the_string(" ") == "  "
    assert ex2.double_the_string("Python") == "PythonPython"
    assert ex2.double_the_string("") == ""
    assert ex2.double_the_string("#!#AbC") == "#!#AbC#!#AbC"


def test_reverse_string():
    assert ex2.reverse_string("Hello") == "olleH"
    assert ex2.reverse_string("World") == "dlroW"
    assert ex2.reverse_string("Python") == "nohtyP"
    assert ex2.reverse_string("") == ""
    assert ex2.reverse_string("#!#AbC") == "CbA#!#"



def test_count_the_es():
    assert ex2.count_the_es("Hello") == 1
    assert ex2.count_the_es("World") == 0
    assert ex2.count_the_es("Earth") == 1
    assert ex2.count_the_es("eeeee") == 5
    assert ex2.count_the_es("EeEeEe") == 6

