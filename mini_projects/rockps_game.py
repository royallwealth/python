# Imported the random module to use random functions 
import random 

# ROCK, PAPER, SCISSORS GAME 🎮🎯😁
# Samantha S.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
Rock
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
Paper
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
Scissors
'''

print('Welcome to the game of "Rock, Paper, Scissors 🎮🎯" ')
print('Let the games begin 😁')

# Stored the images in a list
# Created an input for users choice and converted to an int because it's
# automatically read as a string, so we must do type conversion.

game_images = [rock, paper, scissors]
users_choice = int(input('What do you choose? Type 0 for Rock, Type 1 for Paper, or Type 2 for Scissors:\n '))

# Printed game images and passed the list in square brackets for everytime
# the user makes a choice the image will print.

print(game_images[users_choice])

# Created a variable that stores the computers random choice using .randint from the random module
# Everything that happens after the variables created is what will take place.
# Printed game images and passed the computers random choice variable in square brackets for everytime
# the computer choice is used; the images will also print.

computer_choice = random.randint(0, 2)
print("Computer Chose: ")
print(game_images[computer_choice])

# Created the logic of the game 
# Line 68 to Line 69: is for if the user inputs a value that exceeds the values asked for
# Line 70 to Line 71: is an elif statement if user inputs 0 for rock and computer is 2; then you won!
# Line 72 to Line 73: an elif if the computer picks rock and user picks 2; then you lost!
# Line 74 to Line 75: is an elif if the computers choice is greater than users choice; you lose!
# Line 76 to Line 77: is an elif if the users choice is greater than computers choice choice; you won!
# Line 78 to Line 79: is an elif if the user and computer choice is the same; then it's a draw

if users_choice >= 3 or users_choice < 0:
    print("Invalid Entry")
elif users_choice == 0 and computer_choice == 2:
    print("You Won 🎉")
elif computer_choice == 0 and users_choice == 2:
    print("You Lose!")
elif computer_choice > users_choice:
    print("Game Over, You Lost 👎🏽")
elif users_choice > computer_choice:
    print("You Won!")
elif users_choice == computer_choice:
    print("Issa Draw")