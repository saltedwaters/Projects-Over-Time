while True:
    print("------------GCF FINDER------------")
    while True:
        try:
            num1 = int(input("Enter the 1st number: "))
            num2 = int(input("Enter the 2nd number: "))
            if num1 < 0 or num2 < 0:
                print(f"The GCF of {num1} and {num2} is 1.")
            break
        except ValueError:
            print("Input a valid number")


    smaller = min(num1, num2)
    bigger = max(num1, num2)
    for x in reversed(range(1, smaller+1)):
        if smaller % x == 0 and bigger % x == 0:
            print(f"The GCF of {num1} and {num2} is {x}.")
            break
