import random

# GUESSING GAME 🤔
# Samantha S.

print("""
             ________
        _jgN########Ngg_
      _N##N@@""  ""9NN##Np_
     d###P            N####p
     "^^"              T####
                       d###P
                    _g###@F
                 _gN##@P
               gN###F"
              d###F
             0###F
             0###F
             0###F
             "NN@'

              ___
             q###r
              ""
      """)

print("Welcome to the guessing game.")
print("Guess a number 1 through 10")

random_integer = random.randint(1, 10)
users_guess = int(input("What number would you like to choose? Pick a number from 1 to 10\n"))

if users_guess == random_integer:
    print("Good Guess, You Won!")
elif users_guess > random_integer:
    print("Too High! 📈")
else:
    print("Too Low! 📉")

# Restart the game without loops
restart = input("Play Again? Yes or No?\n").lower()

if restart == "yes":
    print("Starting new game...")
else:
    print("Game Over! See You Next Time :)")

# This gussing game does not contain loops yet
# will revise soon