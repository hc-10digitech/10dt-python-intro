from time import sleep

def is_bigger_than_100(n: int) -> bool:
    # TODO: Write code to check if the number is bigger than 100. 
    # Your function needs to return True if it is, False otherwise
    return n > 100
    

def is_even(n: int) -> bool:
    # TODO: Write code to check if the number is even. 
    # Your function needs to return True if it is, False otherwise

    return n % 2 == 0

def is_even_and_bigger_than_100(n: int) -> bool:
    # TODO: Write code to check if the number is even AND it is bigger than 100.
    # Your function needs to return True both conditions are met, otherwise return False

    return is_even(n) and is_bigger_than_100(n)

def includes_e(s: str) -> bool:
    # TODO: Write code to check if the string contains the letter 'e' (upper or lower case).
    # Your function needs to return True if it does, False otherwise

    return "e" in s.lower()

def hot_cold_mild(temp: int) -> str:
    # TODO: Write code to check if the temperature is hot, cold or mild. 
    # If the temperature is 30 or more, return "hot". If the temperature is below 15, return "cold".
    # Otherwise return "mild"
    if temp < 15:
        return "cold"
    elif temp < 30:
        return "mild"
    else: 
        return "hot"


if __name__ == "__main__":
    # Run each function with your own input to test them
    num_in = int(input("Enter a number to try: "))
    print("Running is_bigger_than_100(n):")
    print(f"Output: {is_bigger_than_100(num_in)}")
    sleep(0.3)
    print("Running is_even(n):")
    print(f"Output: {is_even(num_in)}")
    sleep(0.3)
    print("Running is_even_and_bigger_than_100(n):")
    print(f"Output: {is_even_and_bigger_than_100(num_in)}")
    sleep(0.3)
    string_in = input("Enter a string to try: ")
    print("Running includes_e(s):")
    print(f"Output: {includes_e(string_in)}")
    sleep(0.3)
    temp_in = int(input("Enter a temperature to try: "))
    print("Running hot_cold_mild(temp):")
    print(f"Output: {hot_cold_mild(temp_in)}")
    sleep(0.3)