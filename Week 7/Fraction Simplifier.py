import sys
text = "a" # purely for prompt purposes
while True:
    while True:
        try: # try except block for input of proper fraction
            strfrac = input(f"Enter {text} fraction (x/y), where y ≠ 0 (q to quit): ")
            if strfrac == "q":
                sys.exit()
            numerator, denominator = strfrac.split("/")
            numerator = int(numerator)
            denominator = int(denominator)

            if denominator == 0:
                raise ZeroDivisionError
            if numerator == 0:
                print(f"The fraction is simplified to 0.")
                sys.exit()
            break
        except ZeroDivisionError:
            print("Please enter a fraction where the denominator is not 0.")
        except ValueError:
            print("Please enter a numerical value in the correct format! ")

# determines if the fraction inputted is positive or negative
    if (numerator < 0) ^ (denominator < 0):
        sign = -1
    else:
        sign = 1

    numerator = abs(numerator)
    denominator = abs(denominator)

    factors_num = []
    factors_den = []
    # for loops for identifying all the factors
    for i in range(1, numerator + 1):
        if numerator % i == 0:
            factors_num.append(i)

    for i in range(1, denominator + 1):
        if denominator % i == 0:
            factors_den.append(i)

    # greatest common factor identification
    GCF = max(set(factors_num) & set(factors_den))
    simplified_num = numerator // GCF
    simplified_den = denominator // GCF
    result = f"{simplified_num}/{simplified_den}"

    # addition of negative sign based on sign polarity
    if sign == -1:
        result = "-" + result
    if GCF == 1:
            print(f"The fraction {result} cannot be simplified further.")
    else:
        print(f"The simplified version of {strfrac} is {result}.")
    text = "another"


