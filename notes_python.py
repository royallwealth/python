## If/elif/else
"""
if <condition 1 is true>
    <do A>
elif <condition 2 is true>
    <do B>
else
    <do C>
# Nested if statements
if <condition 1 is true>
    <do A>
    if <condition 2 is true>
        <do B>
        if <condition 3 is true>
            <do C>
# Multiple if statements
if <condition 1 is true>
    <do A>
if <condition 2 is true>
    <do B>
if <condition 3 is true>
    <do C>
"""

#creating random choices
"""
#using import random to use the modules in random
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#option 1
print(random.choice(friends))

#option 2
random_index = random.randint(0, 4)
print(friends[random_index])
"""

#creating a nested list that combines the two lists together
"""
#adding a list within a list is called a nested list

fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"] #this is added to the fruits list when storing in a variable

#like this, this combines the list
dirty_dozen = [fruits, veg] 
print(dirty_dozen)
"""