attempt = 1  # setup for ordinal numbers
calc = []  # location of numbers and operations


def order(n):  # function for inducing ordinal suffices
    if 10 <= n % 100 <= 20:  # if n is above or equal to 10 and below and equal to 20, have suffix "th". If number is higher, modulo 10 is taken
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10,
                                                 "th")  # if ones digit of number is 1, 2, or 3, use appropriate suffix. Higher numbers done through modulo
    return f"{n}{suffix}"


start = True

while start:  # loop for choosing numbers and operations
    try:
        num = float(input(f"Enter the {order(attempt)} number: "))
        while True:  # loop for choosing operation.
            op = input("Enter the operation to be used (+, -, *, /) (q to quit): ")
            if op.upper() == "Q":  # if q is typed for operation, the last number inputted is appended to the calc []
                calc.append(num)
                start = False
                break
            elif op not in ["+", "-", "*", "/"]:  # if user input not within the given set, prints "invalid operator"
                print("Input a valid operator!")
            else:  # appends number and operator at last loop
                calc.append(num)
                calc.append(op)
                attempt += 1
                break
    except ValueError:
        print("Input a valid number!")
    except Exception:
        print("Something went wrong!")
    print(calc)

# this loop searches the tuple for multiplication and division operators and performs the operation
i = 0
while i < len(calc):
    if calc[
        i] == "*":  # if "*" is found at a certain index, the item before and after it is utilized to perform multiplication.
        calc[i - 1:i + 2] = [calc[i - 1] * calc[i + 1]]
        i -= 1  # subtracts index by 1 to account for the lesser items after operation
    elif calc[
        i] == "/":  # if "/" is found at a certain index, the item before and after it is utilized to perform division.
        calc[i - 1:i + 2] = [calc[i - 1] / calc[i + 1]]
        i -= 1
    else:
        i += 1

# this loop searches the tuple for addition and subtraction operators and performs the operation
i = 0
while i < len(calc):
    if calc[
        i] == "+":  # if "+" is found at a certain index, the item before and after it is utilized to perform addition.
        calc[i - 1:i + 2] = [calc[i - 1] + calc[i + 1]]
        i -= 1
    elif calc[
        i] == "-":  # if "-" is found at a certain index, the item before and after it is utilized to perform subtraction.
        calc[i - 1:i + 2] = [calc[i - 1] - calc[i + 1]]
        i -= 1
    else:
        i += 1

print(f"The answer is {calc[0]}.")


