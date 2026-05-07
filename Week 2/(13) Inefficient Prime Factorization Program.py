# Query system for positive whole number.
while True:
    try:
        num = int(input("Enter a number: "))
        if num == 0:
            print("Input a nonzero positive number.")
            continue
        if 0 > num:
            print("Input a positive number.")
        else:
            break
    except Exception:
        print("Input a valid nonzero positive number.")

factors = []
prime_factors = []
fullprime = []

# Defines factorize() which obtains the factors of the inputted number.
def factorize(number):
    number = int(number)
    for i in range(1, number + 1): # Loops from 1 till the number inputted itself.
        if not number % i: # If inputted number modulo i yields 0 (not False), it appends. if not, (not True), it skips.
            factors.append(i)

# prine_factorize() obtains only the prime factors from factors list and puts then in prime_factors list.
# The system loops through all the numbers in the factors list and tests if it is divisible with integers: 2 up to the inputted number itself.
def prime_factorize(factors):
    for x in factors: # Loops through all numbers within factors list.
        prime = True # Assumes that the number is prime.
        for y in range(2, factors[-1]): # Loops through y from 2 (first prime factor) up to the number itself.
            if x % y == 0 and x > y: # If x (factor of number) modulo y (number between 2 and input) yields 0, a factor is present, thus prime = False.
                prime = False
                break
        if prime: # Appends if the if statement above is not met (number is prime).
            prime_factors.append(x)


factorize(num)
factors.remove(1) # Removes 1 from the list of prime factors, as it is not a prime number.
prime_factorize(factors)

# System for obtaining the actual count of the prime factors.
def primer(prime_factors):
    divide = num
    factorable = True # Assumes by default that the input number is divisible.
    while factorable:
        for a in prime_factors: # Obtains modulo for each prime factor in the list (input mod a).
            if divide % a == 0: # If a (prime factor) can divide to the input number, append.
                divide /= a # Divides the input number by a, to be utilized again by the for loop.
                fullprime.append(a)
            elif divide % a != 0: # If the number is not divisible by a in prime factor, the next prime factor will be tried.
                continue
        if divide == 1: # After getting divided by the prime factors in the list, if the number turns into 1, the while loop is stop.
            factorable = False

primer(prime_factors)
fullprime.sort()
counts = {}

# If the prime factor b from the fullprime list is in the counts set, it adds +1 to the count, if not, it is set to 1.
for b in fullprime: # This loops till the count of each unique prime factor has been identified.
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
    result = ""
    for digit in str(n):
        result +=superscripts[digit]
    return result

result = ""
# Defines a function to print each corresponding base and exponent in the correct format.
for c in counts:
    result += f"{c}{superscript(counts[c])} x "
finalresult = result.removesuffix("x ")
print(finalresult)
