temp = float(input("Input the temperature: ")) #Input temperature to be converted


while True: #This loop haves you input the unit of the temperature you entered.
   unit = input("What temperature unit is it in (F, C, K): ").strip().upper() #The .strip().upper() converts the input into a capital letter for the whole code to use.
   if unit not in ("F", "C", "K"): #If unit inputted is not within the list, invalid unit is displayed and then it loops.
       print("Input a valid temperature unit.")
   else:
       print(f"Your temperature is {temp}°{unit}")
       break


while True:
   converted_unit = input("What temperate unit do you want to convert it to?: ").strip().upper() #Input the unit to convert to.
   if converted_unit not in ("F", "C", "K"):
       print("Input a valid temperature unit.")
   elif unit == converted_unit:
       print("Input a different temperature unit.")
   else:
       break
#The series of if and elif statements below are the whatevers for temperature conversion.
if unit == "C" and converted_unit == "F":
   answer = 9/5 * temp + 32
elif unit == "C" and converted_unit == "K":
   answer = temp + 273.15
elif unit == "F" and converted_unit == "C":
   answer = 5/9 * (temp - 32)
elif unit == "F" and converted_unit == "K":
   answer = 5 / 9 * (temp - 32) + 273.15
elif unit == "K" and converted_unit == "C":
   answer = temp - 273.15
elif unit == "K" and converted_unit == "F":
   answer = (temp - 273.15) * 9/5 + 32


print(f"{temp}°{unit} = {answer:.2f}°{converted_unit}")
