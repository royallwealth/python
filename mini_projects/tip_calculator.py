# TIP CALCULATOR 🧮
# Samantha S.

# creating a restaurant tip calculator
# creating the user input variables lines 4-6
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# storing the calculating with the formula to calculate the tip, 
# the bill and the split per person
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people

# using python's built-in round in line 16 function to 
# round two decimal places. This function
# takes two parameters
final_amount = round(bill_per_person, 2)

# using f string which is a template literal
print(f"Each person should pay ${final_amount}")