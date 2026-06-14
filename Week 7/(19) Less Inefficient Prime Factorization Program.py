import sys

while True:
    print("-------------PRIME FACTORS FINDER-------------")
    print("Type q to quit.")
    while True:
        try:
            num = input("Enter the 1st number: ")
            if num.upper() == "Q":
                sys.exit()

            num = int(num)
            if num < 0:
                sign = -1
            else:
                sign = 1
            num = abs(num)
            break
        except ValueError:
            print("Input a valid number")

    def prime_factors(n):
            n = abs(n)
            factors = []
            divisor = 2
            # divides the number by 2 until it is no longer divisible by 2, then it will divide by 3 and so on and so forth.
            while divisor * divisor <= n:
                while n % divisor == 0:
                    factors.append(divisor)
                    n //= divisor
                divisor += 1

            if n > 1:
                factors.append(n)
            return factors
    pfactors= prime_factors(num)
    counts = {}

    for b in pfactors:  # This loops till the count of each unique prime factor has been identified.
        if b in counts:
            counts[b] += 1
        else:
            counts[b] = 1

    superscripts = {
        "1": "¹",
        "2": "²",
        "3": "³",
        "4": "⁴",
        "5": "⁵",
        "6": "⁶",
        "7": "⁷",
        "8": "⁸",
        "9": "⁹"}

    # Defines a function to be able to print the exponents in superscript format.
    def superscript(n):
        if n == 1:
            return ""
        result = ""
        for digit in str(n):
            result += superscripts[digit]
        return result

    result = ""
    # Defines a function to print each corresponding base and exponent in the correct format.
    for i in counts:
        result += f"{i}{superscript(counts[i])} x "
    if num == 0:
        print("The number 0 has no prime factors")
    elif num == 1:
        print("The number 1 has no prime factors")
    elif sign == -1:
        result += "-1"
        print(f"Prime Factors: {result}")
    elif sign == 1:
        finalresult = result.removesuffix("x ")
        print(f"Prime Factors: {finalresult}")


