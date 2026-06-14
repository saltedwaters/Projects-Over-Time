import sys
# This program find the LCM of the two inputted numbers through their prime factors.
while True:
    print("-------------LCM FINDER-------------")
    print("Type q to quit.")
    while True:
        try:
            num1 = input("Enter the 1st number: ")
            if num1.upper() == "Q":
                sys.exit()
            num2 = input("Enter the 2nd number: ")
            if num2.upper() == "Q":
                sys.exit()
            num1 = abs(int(num1))
            num2 = abs(int(num2))
            if num1 == 0 or num2 == 0:
                print(f"The LCM of {num1} and {num2} is 0.")
                sys.exit()
            break
        except ValueError:
            print("Input a valid number")

    def prime_factors(n):
        n = abs(n)
        factors = []
        divisor = 2
        # divides the number by 2 until it is no longer divisible by 2, then it will divide by 3 and so on and so forth.
        while pow(divisor, 2) <= n:
            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor
            divisor += 1

        if n > 1:
            factors.append(n)
        return factors

    pfactors1 = prime_factors(num1)
    pfactors2 = prime_factors(num2)

    counts1 = {}
    counts2 = {}

    # the following 2 for loops append the factors (key) and their quantity (value) into a dictionary (key value pair)
    for i in pfactors1:
        if i in counts1:
            counts1[i] += 1
        else:
            counts1[i] = 1

    for i in pfactors2:
        if i in counts2:
            counts2[i] += 1
        else:
            counts2[i] = 1

    lcmcounts = {}
    # copies all the key value pairs in counts1 into lcmcounts
    for key in counts1:
        lcmcounts[key] = counts1[key]

    # adds all key value pairs (replaces if the same) of counts2 into lcm counts
    for key in counts2:
        if key in lcmcounts: #if the factor (key) is already in lcmcounts, it will be replaced if the amount of a same factor (value) in counts2 is higher than it
            lcmcounts[key] = max(lcmcounts[key], counts2[key])
        else:
            lcmcounts[key] = counts2[key]

    # multiplies all keys with their respective values (factors and amount).
    result = 1
    for key in lcmcounts:
        value = lcmcounts[key]
        result *= key ** value # multiplies each key * value product with the other products

    print(f"The LCM of {num1} and {num2} is {result}.")



