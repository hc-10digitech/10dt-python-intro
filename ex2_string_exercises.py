# Python exercises. You need to write code in spots labelled "TODO:" to make the functions pass the tests

def say_hello(name: str) -> str:
    # TODO: Write code to greet the person. Your function needs to return "Hello, <name>!"

    return ""


def double_the_string(s: str):
    # TODO: Write code to give the same string repeated. Your function needs to return the doubled string

    return ""


def reverse_string(s: str):
    # TODO: Write code to reverse the string. Your function needs to return the reversed string

    return ""


# Tests. Don't mess with this code, just run it in the terminal by typing "pytest ex2_string_exercises.py"
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