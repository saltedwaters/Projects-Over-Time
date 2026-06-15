import sys
import time
while True:
    while True:
        print("-------------OPTIMIZED √N METHOD-------------")
        print("Type q to quit.")
        try:
            num = input("Enter the 1st number: ")
            start_time = time.perf_counter()
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
    print(prime_factors(num))
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"The optimized √n method took approximately {execution_time:.4f} seconds.")

    while True:
        print("-------------TRIAL DIVISION METHOD-------------")
        try:
            num = int(input("Enter a number: "))
            start_time1 = time.perf_counter()

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
        for i in range(1, number + 1):  # Loops from 1 till the number inputted itself.
            if not number % i:  # If inputted number modulo i yields 0 (not False), it appends. if not, (not True), it skips.
                factors.append(i)


    # prine_factorize() obtains only the prime factors from factors list and puts then in prime_factors list.
    # The system loops through all the numbers in the factors list and tests if it is divisible with integers: 2 up to the inputted number itself.
    def prime_factorize(factors):
        for x in factors:  # Loops through all numbers within factors list.
            prime = True  # Assumes that the number is prime.
            for y in range(2, factors[-1]):  # Loops through y from 2 (first prime factor) up to the number itself.
                if x % y == 0 and x > y:  # If x (factor of number) modulo y (number between 2 and input) yields 0, a factor is present, thus prime = False.
                    prime = False
                    break
            if prime:  # Appends if the if statement above is not met (number is prime).
                prime_factors.append(x)


    factorize(num)
    factors.remove(1)  # Removes 1 from the list of prime factors, as it is not a prime number.
    prime_factorize(factors)


    # System for obtaining the actual count of the prime factors.
    def primer(prime_factors):
        divide = num
        factorable = True  # Assumes by default that the input number is divisible.
        while factorable:
            for a in prime_factors:  # Obtains modulo for each prime factor in the list (input mod a).
                if divide % a == 0:  # If a (prime factor) can divide to the input number, append.
                    divide /= a  # Divides the input number by a, to be utilized again by the for loop.
                    fullprime.append(a)
                elif divide % a != 0:  # If the number is not divisible by a in prime factor, the next prime factor will be tried.
                    continue
            if divide == 1:  # After getting divided by the prime factors in the list, if the number turns into 1, the while loop is stop.
                factorable = False


    primer(prime_factors)
    fullprime.sort()
    print(fullprime)
    end_time1 = time.perf_counter()
    execution_time1 = end_time1 - start_time1
    print(f"The optimized √n method took approximately {execution_time1:.4f} seconds.")
    saved_time = execution_time1 - execution_time
    print(f"The saved time was {saved_time:.4f} seconds. ")







