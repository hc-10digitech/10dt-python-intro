def is_smaller_than_20(n: int) -> bool:    
    if n < 20:
        return True
    else:
        return False
    
    
    
def is_odd(n: int) -> bool:
    if n % 2 == 1:
        return True
    else:
        return False
    
def is_odd_and_smaller_than_20(n: int) -> bool:
    if n % 2 == 1 and n < 20:
        return True
    else:
        return False
    
def pass_fail_close(n: int) -> str:
    if n >= 50:
        return "Pass"
    elif n >= 40:
        return "Close - Resubmit"
    else:
        return "Fail"
    
def is_vowel(charac: str) -> bool:
    if charac.lower() in "aeiou":
        return True
    else: 
        return False
    
if __name__ == "__main__":
    while True:
        print("Menu:")
        print("1. Check if a number is smaller than 20")
        print("2. Check if a number is odd")
        print("3. Check if a number is odd and smaller than 20")
        print("4. Check if a number is pass, fail, or close")
        print("5. Check if a character is a vowel")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            num = int(input("Enter a number: "))
            result = is_smaller_than_20(num)
            print("**********")
            print(f"The number {num} is smaller than 20: {result}")
            print("**********")
        elif choice == "2":
            num = int(input("Enter a number: "))
            result = is_odd(num)
            print("**********")
            print(f"The number {num} is odd: {result}")
            print("**********")
        elif choice == "3":
            num = int(input("Enter a number: "))
            result = is_odd_and_smaller_than_20(num)
            print("**********")
            print(f"The number {num} is odd and smaller than 20: {result}")
            print("**********")
        elif choice == "4":
            num = int(input("Enter a number: "))
            result = pass_fail_close(num)
            print("**********")
            print(f"The number {num} is: {result}")
            print("**********")
        elif choice == "5":
            char = input("Enter a character: ")
            result = is_vowel(char)
            print("**********")
            print(f"The character {char} is a vowel: {result}")
            print("**********")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")