# 60% UPCAT and 40% High School Grades

# Defines function for input request on score and grades.
def valid_input(parameter, min, max):
    while True: # Checks if input is within prescribed min max.
        try:
            value = float(input(parameter))
            if min <= value <= max:
                return value
            else:
                print(f"Input a valid number between {min} and {max}!")
        except Exception:
            print("Input a valid number!")

# Subtests and grades to undergo input.
lang_prof = float(valid_input("Enter your predicted language proficiency score out of 80: ", 0, 80))
read_comp = float(valid_input("Enter your predicted reading comprehension score out of 80: ", 0, 80))
math = float(valid_input("Enter your predicted mathematics score out of 50: ", 0, 50))
sci = float(valid_input("Enter your predicted science score out of 45: ", 0, 45))
g8 = float(valid_input("Enter your general average in Grade 8: ", 0, 100))
g9 = float(valid_input("Enter your general average in Grade 9: ", 0, 100))
g10 = float(valid_input("Enter your general average in Grade 10: ", 0, 100))
g11 = float(valid_input("Enter your general average in Grade 11: ", 0, 100))

# Calculation of the average of high school grades and UPCAT performance.
hsgrades = ((g8 + g9 + g10 + g11) / 4) * 0.4
gwa = hsgrades / 0.4
admtest = ((lang_prof + read_comp + math + sci) / 255) * 60
final_grade = hsgrades + admtest
print(f"Your high school grades have an average of {gwa:.2f}.")
print(f"You correctly answered {admtest:.2f}% of the questions in the UPCAT.")
print("---------------------------------------------")

# Defines a function for interpolation
def interpolate(final_grade):
    if final_grade < 54:
        return 5.00
    grade_conversion = [
        (54, 5.00),
        (59, 4.00),
        (64, 3.00),
        (69, 2.75),
        (74, 2.50),
        (83, 2.00),
        (86, 1.75),
        (89, 1.50),
        (92, 1.25),
        (100, 1.00)]
    # Interpolation part below. Scans the grade_conversion list till the input (x) is between two numbers.
    # The first number is x1, in which its index is taken note of, and the number above it is x2, which is the given index + 1.
    for i in range(len(grade_conversion)):
        x1, y1 = grade_conversion[i]
        x2, y2 = grade_conversion[i+1]
        x = final_grade
        if x1 <= x < x2:
            y = y1 + (x - x1) * ((y2 - y1) / (x2 - x1)) # Interpolation formula.
            return y
        if x == x1:
            return y1
        if x == x2:
            return y2
UPG = interpolate(final_grade)
print(f"Your estimated UPG is {UPG:.4f}.")




