#!/usr/bin/python3
"""
In this script, I will explore control structures
"""

"""
if statement
 - if statements are conditional statements, i.e
   they are used to make decisions
 - if one condition is not met, execute the next statement
"""
temperature = int(input("Enter temperature in Celsius: "))

if temperature < 0:
    print("It is freezing outside!")
elif temperature > 25:
    print("It is quite hot outside!")
else:
    print("It is comfortable outside!")


"""
for loop
 - Python's for statement  iterates over the items of any sequence (a list or a string), 
   in the order that they appear in the sequence
"""
words = ["cat", "window", "defenestrate"]
for w in words:
    print(w, len(w))


"""
while loop
 - Using while loops, we can execute a block of code as long as a condition is true
"""
# print i as long as it is less than 5
i = 1
while i <= 5:
    print(i)
    i += 1

print("-" * 10)



"""
break and continue statements
 - The break statement can be used to stop the loop 
   before it has looped through all the items
 - The continue statement can be used to skip the rest of the code
"""
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
    if i == 7:
        break
