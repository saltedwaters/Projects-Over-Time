import math, sys
print("------FACTOR FINDER------")
while True:
    number = input("Input a positive whole number (q to quit): ")
    # Requires input number to be positive and whole for code to work.
    if number.upper() == "Q":
        sys.exit()
    elif not number.isdecimal():
        continue
    elif int(number) <= 0:
        continue
    intnum = int(number)
    factors = []

    # Iterates possible factors from 1 up to the square root of the given number inclusive.
    for i in range(1, int(math.sqrt(intnum)) + 1):
        if intnum % i == 0: # Only appends if intnum mod i returns 0, meaning i is a valid factor.
            factors.append(i)
            pair = intnum // i
            if pair != i: # This restricts the appending of duplicates. (ex. 16 / 4. i = 4. pair = 4. Only appends i and not both.
                factors.append(pair) # Appends the factor pair of the appended i (ex. i = 1, 16 // 1 = 16. Both 1 and 16 are appended.
    factors.sort() # Sorts factors by ascending order.

    # The for loop takes each factor in the list and converts to string.
    print(", ".join(str(factor) for factor in factors)) # The join function takes each individual string, and assigned a space and comma after.
    print(f"{number} has {len(factors)} factors")
    print("------------------------")
