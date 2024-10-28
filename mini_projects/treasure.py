# TREASURE ISLAND GAME 🎮🎯😁
# Samantha S.

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure and make it out.")
direction = input('You\'re at a crossroad, Do you want to go Left or Right?'
                  ' The road on the "Left" is a gold road and "Right" is an iridecent road.'
                  ' Type "left" or "right"\n').lower()

#create conditional based on choices
if direction == "left": #If the user types left then do this
    choice1 = input('You\'ve come to a lake of roses known as "El Agua de Amour."'
                    ' There is an island with a castle in the middle of the lake.'
                    ' Type "wait" to wait for the boat.'
                    ' Type "swim" to swim across.\n').lower()
    #this is a nested statement within in the if direction == left because left leads to the next question
    #whereas if user picks right, game is over. choice 1 == wait is also nested leads to next question
    #which door? which is nested inside choice2 == wait
    if choice1 == "wait": 
        choice2 = input('You arrive at the castle unharmed.'
                        ' There is the castle entrance with 3 doors. One red,'
                        ' one yellow and one blue. '
                        ' Which color do you choose?\n').lower()
        #this is nested inside choice1 == wait  which also inside of choice2 == pick a color
        if choice2 == "red":
            print("It's a room full of fire, Game over!")
        elif choice2 == "yellow":
            print("You found the treasure and key. You win! Now, GO!")
        elif choice2 == "blue":
            print('You\'ve entered a room full of beasts 3 headed snakes. Game over!')
        else:
            print("You chose a door that doesn't exist. Game Over!")
    else:
        print("You got attacked by an angry big. Game over!")

        #this else statement is for if the user picks "Right" then right off the else states game over
        #as you can see the indentation in the beginning of lines and usually you can tell
        #if the code is nested of not
else:
    print("You fell in to a hole and swallowed up. Game Over.")