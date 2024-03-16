#!/usr/bin/python3
"""
In this script, I will explore the Python syntax
"""

"""
Python identifiers
 - Python identifiers must start with a letter or the underscore character
 - They can contain only letters, digits, and the underscore character
"""

valid_identifier = "abc123_"
invalid_identifier = "123abc"
print(valid_identifier)
print(invalid_identifier) # raises SyntaxError

"""
Python lines and indentation
 - Python lines can be indented using the four spaces or one tab
 - Python lines must end with a new line character
 - Indentation is required for Python code blocks, this is rigidly enforced
"""
example1 = input("Enter True or False: ")
if example1 == True:
    print("Hello, World!")
else:
    print("Goodbye, World!")

# This will raise SyntaxError
example2 = input("Enter True or False: ")
if example2 == True:
    print("Hello, World!")
        print("Learning DSA")
else:
    print("Goodbye, World!")
        print("This is not going well")

# This will raise IndentationError
example3 = input("Enter True or False: ")
if example3 == True:
print("Hello, World!")
print("Learning DSA")
else:
print("Goodbye, World!")

"""
Multiline statements on a single line
 - The semicolon allows us to write multiple statements on a single line
 as long as none of the statements starts a new code block
"""
import sys; x = sys.version; sys.stdout.write(x + '\n')
