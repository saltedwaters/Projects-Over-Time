import sys
while True:
    print("--------PALINDROME CHECKER--------")
    while True:
        try:
            num = input("Enter a number: ")
            if num.upper() == "Q":
                sys.exit()
            num = int(num)
            break
        except Exception:
            print("Input a valid number!")

    def isPalindrome(x):
        if x < 0: # case for negative numbers
            return False
        if x == 0: # case for 0
            return True
        elif x % 10 == 0: # case for multiples of 10
            return False
        result = 0
        # The while loop reverses half the digits. It stops when the original half = reversed half, then returns True. Keeps going if not, then returns False.
        while x > result:
            result = result * 10 + x % 10
            x //= 10
        if x == result or x == result // 10:
            return True
        else:
            return False
        # Case for odd digit amount
        # result = 0, x = 121
        # result = 1, x = 12
        # result = 10 + 2 = 12, stops while loop since x = result
        # Case for even digit amount
        # result = 0, x = 1221
        # result = 1, x = 122
        # result = 10 + 2 = 12, x = 12, stops while loop since x = result

    if isPalindrome(num):
        print(f"The number {num} is a palindrome!")
    else:
        print(f"The number {num} is not a palindrome!")
