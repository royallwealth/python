"""
#Rollercoaster
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want to have a photo taken? Type y for Yes and n for No.")
    if wants_photo == "y":
        # Add $3 to their bill
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
"""
#########################################################################
"""
#PIZZA PYTHON

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

#variables for small, medium, or large pizza
bill = 0
#Menu
small = 15
medium = 20
large = 25

#Pizza selection prices
if size == "S":
    bill = small
   # print(f"Small-Pizza: ${bill}")
elif size == "M":
    bill = medium
   # print(f"Medium-Pizza: ${bill}.")
elif size == "L":
    bill = large
    #print(f"Large-Pizza: ${bill}.")

#If you want toppings pepperoni or extra cheese
if pepperoni == "Y" and size == "S":
            bill += 2
           # print(f"Add-Topping: $2 ")
elif pepperoni == "Y" and size == "M":
        bill += 3
        #print(f"Add-Topping: $3 ")
elif pepperoni == "Y" and size == "L":
       bill += 3
       #print(f"Add-Topping: $3 ")

if extra_cheese == "Y":
        bill += 1
        #print(f"Extra-Cheese: $1 ")
print(f"Your final bill is: ${bill}.")
"""
