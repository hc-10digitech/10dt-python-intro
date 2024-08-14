from time import sleep

def count_up(n: int):
    # Returns a list of numbers from 0 to n
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list

def counting_by_2(n: int):
    # Returns a list of numbers from 0 to n, counting by 2
    my_list = []
    # You can set the "step" property of range.
    for i in range(0, n, 2):
        my_list.append(i)
    return my_list

def halve_to_one(n: int):
    # Returns a list of numbers from n to 1 (or close to it),
    # halving each time
    my_list = []
    while n >= 1:
        my_list.append(n)
        n = n / 2
    return my_list

if __name__ == "__main__":
    n_in = int(input("Enter the value you want to test:"))
    print(count_up(n_in))
    sleep(0.5)
    print(counting_by_2(n_in))
    sleep(0.5)
    print(halve_to_one(n_in))
    sleep(0.5)
    print("Done!")