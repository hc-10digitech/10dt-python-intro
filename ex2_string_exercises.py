# Python exercises. You need to write code in spots labelled "TODO:" to make the functions pass the tests
from time import sleep
def say_hello(name: str) -> str:
    # TODO: Write code to greet the person. Your function needs to return "Hello, <name>!"

    return ""


def double_the_string(s: str):
    # TODO: Write code to give the same string repeated. Your function needs to return the doubled string

    return ""


def reverse_string(s: str):
    # TODO: Write code to reverse the string. Your function needs to return the reversed string

    return ""


def count_the_es(s: str) -> int:
    # TODO: Write code to count the number of 'e's in the string (upper and lower case).
    #  Your function needs to return the count

    return 0


if __name__ == "__main__":
    # Run each function with your own input to test them
    name_in = input("Enter a string to try: ")
    print("Running say_hello(name):")
    print(f"Output: {say_hello(name_in)}")
    sleep(0.3)
    print("Running double_the_string(s):")
    print(f"Output: {double_the_string(name_in)}")
    sleep(0.3)
    print("Running reverse_string(s):")
    print(f"Output: {reverse_string(name_in)}")
    sleep(0.3)
    print("Running count_the_es(s):")
    print(f"Output: {count_the_es(name_in)}")

