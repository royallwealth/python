import random

#ROCK, PAPER, SCISSORS GAME 🎮🎯😁
#Samantha S.

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

game_images = [rock, paper, scissors]
users_choice = int(input('What do you choose? Type 0 for Rock, Type 1 for Paper, or Type 2 for Scissors:\n '))
computer_choice = random.randint(0, 2)
print(game_images[users_choice])

computer_choice = random.randint(0, 2)
print(f"Computer Chose: ")
print(game_images[computer_choice])

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