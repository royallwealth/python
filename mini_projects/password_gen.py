# PYTHON PASSWORD GENERATOR 🔑
# Samantha S.

# The random module lets us use functions like random.choice() 
# to randomly pick items from a list, which is essential for generating 
# a random password.

import random

# These lists store all possible letters, numbers, and symbols that
# can be used in the password.

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# To create a password based on the user's requirements, we need to know how 
# many letters, symbols, and numbers they want. By converting the inputs 
# to integers, we can use these values to control the number of random 
# selections in each category.

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# We use password_chars as a place to store all the selected letters, 
# symbols, and numbers.

password_chars = []

# Each for loop runs as many times as the user specified. Inside each loop:
# random.choice() randomly selects an item from letters, symbols, or numbers.
# password_chars.append(...) adds that random choice to the password_chars list.
# By doing this, we get exactly the right number of letters, symbols, and 
# numbers in the password, as requested by the user.

for _ in range(nr_letters):
    password_chars.append(random.choice(letters))

for _ in range(nr_symbols):
    password_chars.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_chars.append(random.choice(numbers))

# This random.shuffle is from the random module and the characters 
# in password_chars for a more randomized final password.

random.shuffle(password_chars)

# ''.join(password_chars) combines all items in password_chars into a 
# single string.

new_password = ''.join(password_chars)

# print the final password
print(f"Your New Password is: {new_password}")