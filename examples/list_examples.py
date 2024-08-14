from time import sleep

"""
Things to know about lists:
- Lists are ordered collections of items
- Lists can contain any type of data
- The length of a list can be found using the len() function
- Lists can be indexed using square brackets []
- The first element of a list is at index 0
"""

    
def get_third_element(lst: list):
    # Returns the third element in a list. 
    # If the list has less than 3 elements, return None.
    if len(lst) < 3:
        return None
    else:
        return lst[2]
    
def middle_element(lst: list):
    # Returns the middle element of a list. 
    # If the list has an even number of elements, return the "second middle" element.
    
    # len(lst) gets the length of the list
    if len(lst) == 0:
        return None
    elif len(lst) % 2 == 0:
        return lst[len(lst) // 2 - 1]
    else:
        return lst[len(lst) // 2]
    
def get_element_mean(lst: list) -> float:
    # Calculates the mean (average) of the elements in a list.
    # If the list is empty, return None.
    if len(lst) == 0:
        return None
    else:
        sum = 0
        # Calculate the total
        for number  in lst:
            sum += number
        # Mean is the sum divided by the number of elements 
        return sum / len(lst)   
    

if __name__ == "__main__":
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

    print("Running get_third_element(lst):")
    print(f"Integer list Output: {get_third_element(int_lst)}")
    print(f"String list Output: {get_third_element(str_lst)}")
    print("---")
    sleep(0.3)
    print("Running middle_element(lst):")
    print(f"Integer list Output: {middle_element(int_lst)}")
    print(f"String list Output: {middle_element(str_lst)}")
    print("---")
    sleep(0.3)
    print("Running get_element_mean(lst):")
    print(f"Integer list Output: {get_element_mean(int_lst)}")
    print("---")
    
    