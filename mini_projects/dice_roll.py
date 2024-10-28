# Imported the random module to use random functions 
import random

# THE DICE ROLL 🎲
# Simulator generates random dice rolls (1-10) 
# Samantha S.


# Created a function named roll_dice with an empty parameter()
# Created a return using the random.randint that was imported from the random module
def roll_dice():
   return random.randint(1, 10)

# Implementing user interaction
# The while true statement is for as long as the game is being used then do this
# followed bythe users input stored in a variable called user_input
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

# This program only produces two option of which consist of "yes" and "no"