import sys
while True:
    print("-------------BMI CLASSIFIER-------------")
    print("Type q to quit.")
    while True:
        try:
            height = input("Enter your height in cm: ")
            if height.upper() == "Q":
                sys.exit()
            height = float(height)
            if height <= 0:
                raise ValueError
            weight = input("Enter your weight in kg: ")
            if weight.upper() == "Q":
                sys.exit()
            weight = float(weight)
            if weight <= 0:
                raise ValueError
            height /= 100
            break
        except ValueError:
            print("Input a valid positive number")

    BMI = weight / (height * height)
    def classify(BMI):
        if BMI < 18.5:
            return "Underweight"
        if BMI < 25:
            return "Normal"
        if BMI < 30:
            return "Overweight"
        if BMI < 35:
            return "Obese Class 1"
        if BMI < 40:
            return "Obese Class 2"
        else:
            return "Obese Class 3"

    bmi_range = classify(BMI)
    print(f"Your Body Mass Index (BMI) is {BMI:.2f} ({bmi_range}).")
