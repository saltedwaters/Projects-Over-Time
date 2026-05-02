import time
while True: #this loop makes it so that you have to input a positive number to proceed
   t = int(input("Enter time in seconds: "))
   if t <= 0:
       print("Input a number greater than zero.")
   else:
       break


for x in reversed(range(1, t+1)): # after time (t) is inputted, this loop counts down from t to 1.
   seconds = x % 60 # seconds variable. example: 90 mod 60 = 30. thus 30 seconds
   minutes = int(x / 60) % 60 # minutes variable. example: int(90/60) = 1, 1 mod 60 = 1. thus 1 minute.
   hours = int(x / 3600) % 3600 # hours variable, same concept.
   print(f"{hours:02d}:{minutes:02d}:{seconds:02d}") # :02d dictates the amount of digits.
   time.sleep(1)


print("Time's up!")
