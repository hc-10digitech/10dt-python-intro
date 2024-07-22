from time import sleep
# Python exercises. You need to write code in spots labelled "TODO:"
def add_two_numbers(a: int, b: int) -> int:
    # TODO: Write code to add a and b. Your function needs to "return" the correct sum (instead of 0)

    return 0


def subtract_two_numbers(a: int, b: int) -> int:
    # TODO: Write code to subtract b from a. Your function needs to "return" the correct difference

    return 0


def multiply_two_numbers(a: int, b: int) -> int:
    # TODO: Write code to multiply a and b. Your function needs to "return" the correct product (instead of 0)

    return 0

def which_is_greater(a: int, b: int) -> int:
    # TODO: Write code to find which number is greater. Your function needs to "return" the greater number

    return a

def difference_between_numbers(a: int, b: int) -> int:
    # TODO: Write code to find the difference between a and b. Your function needs to "return" the correct difference
    # Note: The difference should be positive, so check which is bigger

    return 0

def raise_to_power(base, power):
    # TODO: Write code to raise the base to the power.

    return 0


if __name__ == "__main__":
    # Run each function with your own input to test them
    a = input("Enter the value for a: ")
    b = input("Enter the value for b: ")
    print("Running add_two_numbers(a, b):")
    print(f"Output: {add_two_numbers(a, b)}")
    sleep(0.3)
    print("Running subtract_two_numbers(a, b):")
    print(f"Output: {subtract_two_numbers(a, b)}")
    sleep(0.3)
    print("Running multiply_two_numbers(a, b):")
    print(f"Output: {multiply_two_numbers(a, b)}")
    sleep(0.3)
    print("Running which_is_greater(a, b):")
    print(f"Output: {which_is_greater(a, b)}")
    sleep(0.3)
    print("Running difference_between_numbers(a, b):")
    print(f"Output: {difference_between_numbers(a, b)}")
    sleep(0.3)
    print("Running raise_to_power(base, power):")
    print(f"Output: {raise_to_power(a, b)}")
    