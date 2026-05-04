cart = [] # The items, price, and quantities are inputted in this cart tuple.
total = 0
while True: #This loops the whole program, from the selection of the items till the quantities till "q" is inputted.
   item = input("Enter the item you want to buy (q to quit): ")
   if item.upper() == "Q":
       break
   else:
       while True: # This loops the selection of the price, If the price inputted is negative, it loops.
           price = float(input("Enter the price of the item: "))
           if price < 0:
               print("Price cannot be negative.")
               continue
           else: # It cannot loop for letters however
               break
       while True:
           quantity = int(input("Enter the quantity of the item: "))
           if quantity < 0:
               print("Quantity cannot be negative.")
               continue
           else:
               break
       cart.append((item, price, quantity))
print("-------YOUR SHOPPING CART -------")
for item, price, quantity in cart:
   if quantity > 1:
       print(f"{quantity} {item}/s : ${price}")
   else:
       print(f"{quantity} {item} : ${price}")
   total +=(price * quantity)
print(f"Your total is ${total}")
# Note that item, price, quantity are in 1 tuple [], however are easily separable.
# Note that total += price is the correct format.
