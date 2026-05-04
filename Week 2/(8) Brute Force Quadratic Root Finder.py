# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
inputs = True
found = False
while inputs:
    try:
        quadratic_term = float(input("Input quadratic term: "))
        linear_term = float(input("Input linear term: "))
        constant = float(input("Input constant: "))
        inputs = False
    except:
        print("Input a valid number!")

def f(x):
    return quadratic_term*pow(x, 2) + linear_term*x + constant

start = -100
end = 100
step = 0.1
tolerance = 0.00000001
x = start
while x <= end:
    y = f(x)

    if abs(y) < tolerance:
        print(f"solution: x = {round(x, 2)}")
        found = True
    x+=step

if not found:
    print("There is likely no real solution in the range of (-100, 100).")
