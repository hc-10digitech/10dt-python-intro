from time import sleep

def length_of_list(lst: list) -> int:
    #TODO: Write code to return the length of the list given as a parameter

    return len(lst)

def get_second_element(lst: list):
    # TODO: Write code to return the second element of the list given as a parameter
    if len(lst) < 2:
        return None
    return lst[1]

def get_sum_of_elements(lst: list) -> int:
    # TODO: Write code to return the sum (total) of all elements in the list given as a parameter
    sum = 0
    for i in lst:
        sum += i
    return sum

def get_last_element(lst: list):
    # TODO: Write code to return the last element of the list given as a parameter
    return lst[-1] if len(lst) > 0 else None


if __name__ == "__main__":
    # Run each function with your own input to test them
    print("First we need a list of integers.")
    input_val = ""
    int_lst = []
    while input_val != "done":
        input_val = input("Enter an integer to add to the list, or type 'done' to finish: ")
        if input_val != "done":
            # Add the integer to the list
            int_lst.append(int(input_val))
    print(f"Your integer list: {int_lst}")

    print("Now we need a list of strings.")
    input_val = ""
    str_lst = []
    while input_val != "done":
        input_val = input("Enter a string to add to the list, or type 'done' to finish: ")
        if input_val != "done":
            # Add the string to the list
            str_lst.append(input_val)
    print(f"Your string list: {str_lst}")

    print("Running length_of_list(lst):")
    print(f"Integer list Output: {length_of_list(int_lst)}")
    print(f"String list Output: {length_of_list(str_lst)}")
    print("---")
    sleep(0.3)
    print("Running get_second_element(lst):")
    print(f"Integer list Output: {get_second_element(int_lst)}")
    print(f"String list Output: {get_second_element(str_lst)}")
    print("---")
    sleep(0.3)
    print("Running get_sum_of_elements(lst):")
    print(f"Integer list Output: {get_sum_of_elements(int_lst)}")
    print("---")
    sleep(0.3)
    print("Running get_last_element(lst):")
    print(f"Integer list Output: {get_last_element(int_lst)}")
    print(f"String list Output: {get_last_element(str_lst)}")
    print("---")
    sleep(0.3)
