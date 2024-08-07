from time import sleep

def create_alphabet_dict(list_of_words: list) -> dict:
    # TODO: Use a loop to create a dictionary with the first letter of each word as the key and the word as the value
    # Eg. create_alphabet_dict(["apple", "banana", "carrot"]) -> {'a': 'apple', 'b': 'banana', 'c': 'carrot'}
    alphabet_dict = {}

    return alphabet_dict

def create_word_length_dict(list_of_words: list) -> dict:
    # TODO: Use a loop to create a dictionary with the word as the key and the length of the word as the value
    # Eg. create_word_length_dict(["apple", "banana", "carrot"]) -> {'apple': 5, 'banana': 6, 'carrot': 6}
    word_length_dict = {}

    return word_length_dict

def divisible_by_3_dict(n: int) -> dict:
    # TODO: Use a loop to create a dictionary with the numbers from 1 to n as the key 
    # and whether they are divisible by 3 as the value.
    # Eg. divisible_by_3_dict(5) -> {1: False, 2: False, 3: True, 4: False, 5: False}
    divisible_dict = {}

    return divisible_dict


if __name__ == "__main__":
    # Run each function with your own input to test them
    in_str = "X"
    in_lst = []
    while in_str != "":
        in_str = input("Enter a list of words separated by a space. Leave empty once done: ")
        if in_str != "":
            in_lst.append(in_str)
    
    print("Running create_alphabet_dict(list_of_words):")
    print(create_alphabet_dict(in_lst))
    sleep(0.3)

    print("Running create_word_length_dict(list_of_words):")
    print(create_word_length_dict(in_lst))
    sleep(0.3)


    num_in = int(input("Enter a number for divisible by 3: "))
    print("Running divisible_by_3(n):")
    print(f"Output: {divisible_by_3_dict(num_in)}")
    