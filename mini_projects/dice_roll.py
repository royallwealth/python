import random

# The Dice Rolling Simulator generates random 
# dice rolls (1-10) 

def roll_dice():
   return random.randint(1, 10)

# Implementing user interaction

while True:
    user_input = input("Do you want to roll the dice? (yes/no): ").lower()
    if user_input == "yes":
        result = roll_dice()  # Call the roll_dice function
        print(f"You rolled a {result}")  # Print the result
    elif user_input == "no":
        print("Thanks for playing!") # Exits the loop and ends the program
        break
    else:
        print("Please enter 'yes' or 'no'.")

