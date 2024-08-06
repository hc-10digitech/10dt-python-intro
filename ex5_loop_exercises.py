from time import sleep

def list_of(content, n:int):
    # TODO: Use a loop to return a list of n copies of content
    # Eg. list_of("hello", 3) -> ["hello", "hello", "hello"]
    lst = []
    for i in range(n):
        lst.append(content)
    return lst


def countdown(n: int):
    # TODO: Use a loop to return a string that counts down from n to 0
    # Eg. countdown(3) -> "3 2 1 0"
    count = ""
    for i in range(n, -1, -1):
        count = count + " " + str(i)
    return count.strip()

def sum_of_squares(n: int):
    # TODO: Use a loop to return the sum of the squares of the first n numbers
    # Eg. sum_of_squares(3) -> 14 (1^2 + 2^2 + 3^2 = 14)
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum

def factorial(n: int):
    # TODO: Use a loop to return the factorial of n
    # Eg. factorial(3) -> 6 (3*2*1 = 6)
    if n == 0:
        return 1
    elif n > 0:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact
    else:
        return 0



if __name__ == "__main__":
    # Testing your functions here
    val_in = input("Enter the value you want to create a list of:")
    n_in = int(input("Enter the number of copies in the list:"))
    print(list_of(val_in, n_in)) 

    num_in = int(input("Enter the number for counting down, summing squares and finding factorial:"))
    print("Countdown:")
    print(countdown(num_in))
    sleep(0.5)
    print("Sum of squares:") 
    print(sum_of_squares(num_in)) 
    sleep(0.5)
    print("Factorial:")
    print(factorial(num_in))