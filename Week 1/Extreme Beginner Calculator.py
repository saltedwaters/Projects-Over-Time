while True: #This loop encompasses the system that lets you pick the operator, as well as the first and second number.
   while True: #This nested while loop lets you choose the operator to be used.
       operator = input("Input the operator to be used (+, -, *, /): ")
       if operator in ["+", "-", "*", "/"]: #If the operator chosen is within the list, the loop breaks then the numbers are to be picked.
           break
       else: #If the user inputs an operator not within the list above, the user is prompted to try again and a message is displayed that states that a valid operator must be inputted.
           print("Input a valid operator!")
   first_number = float(input("Input the first number: ")) #Input first number
   second_number = float(input("Input the second number: ")) #input second number
   if operator == "/" and second_number == 0: #If division is picked and the second number is 0, undefined is printed and the loop goes back to the point where you pick an operator.
       print("undefined")
   else: #This loop breaks when the operator is valid, and there is no division by zero.
       break


if operator == "+":
   answer = first_number + second_number
elif operator == "-":
   answer = first_number - second_number
elif operator == "*":
   answer = first_number * second_number
elif operator == "/":
   answer = first_number / second_number
print(f"{answer}")