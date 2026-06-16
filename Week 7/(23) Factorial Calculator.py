import sys
print("---------------FACTORIAL CALCULATOR---------------")
while True:
    while True:
        try:
            num = input("Enter a number: ")
            if num.upper() == "Q":
                sys.exit()
            num = int(num)
            break
        except Exception:
            print("Input a valid positive integer!")
    if num < 0:
        print("The factorial of a negative number is always undefined.")
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        print(f"{num}! = {result}")

