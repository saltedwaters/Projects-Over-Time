while True:
   p = float(input("Input your principal value: "))
   if p <= 0:
       print("Invalid principal value")
   else:
       break
while True:
   r = float(input("Input your interest rate in %: "))
   if r <= 0:
       print("Invalid interest rate")
   else:
       break
while True:
   n = float(input("Input your duration (in years): "))
   if n <= 0:
       print("Invalid duration")
   else:
       break
while True:
   m = int(input("Input your frequency of conversion: "))
   if m <= 0:
       print("Invalid frequency of conversion")
   else:
       break
#The lines below set the text to be displayed in the print statement
if m == 1:
   a = "yearly"
elif m == 2:
   a = "semi-annually"
elif m == 4:
   a = "quarterly"
elif m == 12:
   a = "monthly"
elif m == 52:
   a = "weekly"
elif m == 365:
   a = "daily"
else:
   cc = m*n
   a = f"{cc} times"


f = p * pow((1 + (r/100)/m), m*n) #compound interest formula


print(f"With a principal value of ${p}, a loan compounded {a} over {n} years will have a future value of ${f:.2f}")
print(f"Future value = ${f:.2f}.")
