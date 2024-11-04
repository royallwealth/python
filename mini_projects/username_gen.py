# PYTHON USERNAME GENERATOR 🔑
# Samantha S.

import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# user inputs

print("Welcome to the python username generator 😁 ")
users_name = (input("What is the user's name?\n"))
choice = (input("Would you like numbers included? Type Yes or No\n"))
num = int(input("How many numbers would you like to include?\n"))
theme = (input("What is your favorite season?\n"))

username = []

username.extend(random.choice(users_name))
username.extend(theme)
   
if choice.lower() == "yes":
    for x in range(0, num):
        username.append(random.choice(numbers))
else:
    print('Thank you :)')

print(username)    
new_user = ''.join(username)
print(f"Generated Username: {new_user}")



