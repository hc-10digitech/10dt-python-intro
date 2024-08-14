from time import sleep

def create_last_letter_dict(list_of_words: list) -> dict:
    # Creates a dictionary with the last letter of the word as the key
    # and the word as the value
    last_letters = {}
    for word in list_of_words:
        # Get the last letter of the word
        letter = word[-1]
        # Add the word to the dictionary with the last letter as the key
        last_letters[letter] = word

    return last_letters

def number_of_vowels_dict(list_of_words: list) -> dict:
    # Creates a dictionary with the word as the key and the number of vowels in the word as the value
    vowel_counts = {}
    for word in list_of_words:
        # Count the number of vowels in the word
        count = 0
        for letter in word:
            if letter.lower() in "aeiou":
                count += 1
        # Add the word to the dictionary with the vowel count as the key
        vowel_counts[word] = count

    return vowel_counts


def prime_number_dict(n: int) -> dict:
    # Creates a dictionary with the numbers from 1 to n as the key
    # and whether they are prime as the value
    prime_numbers = {}

    # Loop through the numbers from 1 to n
    for num in range(1, n+1):
        # Check if the number is prime
        is_prime = True
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
        else:
            is_prime = False
        # Add the number to the dictionary with whether it is prime as the value
        prime_numbers[num] = is_prime

    return prime_numbers


if __name__ == "__main__":
    # Run each function with your own input to test them
    in_str = "X"
    in_lst = []
    while in_str != "":
        in_str = input("Enter a list of words separated by a space. Leave empty once done: ")
        if in_str != "":
            in_lst.extend(in_str.split())

    print("Running create_last_letter_dict(list_of_words):")
    print(create_last_letter_dict(in_lst))
    sleep(0.3)

    print("Running number_of_vowels_dict(list_of_words):")
    print(number_of_vowels_dict(in_lst))
    sleep(0.3)


    num_in = int(input("Enter a number for prime number: "))
    print("Running prime_number_dict(n):")
    print(f"Output: {prime_number_dict(num_in)}")