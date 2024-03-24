#!/usr/bin/python3
"""
Stacks data structure
"""
from collections import deque

###### Implementing stacks as a collection ######
"""
Given the costly implementation of stacks using lists, it is recommended
to use a deque (double ended queue) for implementing a stack
Deque collections has a handful of ready to use methods to implement a stack
"""

class Stack:
    """ Implementing a stack as a collection """
    def __init__(self) -> None:
        """ Initialize the stack object """
        self.stack = deque()

    def is_empty(self) -> None:
        """ Check if the stack is empty """
        if len(self.stack) == 0:
            return True
        return False
    
    def push(self, data) -> None:
        """ Add an element to the top of the stack """
        self.stack.append(data)
        return f"Element {data} added to the top of the stack"

    def pop(self) -> None:
        """ Remove an element from the top of the stack """
        return self.stack.pop()
    
    def peek(self) -> None:
        """ Return the value of the topmost element in the stack """
        return self.stack[-1]
    
    def reverse_string(self, string) -> None:
        """ Reverses a string using a stack """
        for char in string:
            self.push(char)
        reversed_string = ""
        while not self.is_empty():
            reversed_string += self.pop()
        return f"The string reversed is: {reversed_string}"
    
    def parenthesis_checker(self, string) -> None:
        """ Checks if the parenthesis in a string are balanced """
        for char in string:
            if char == "(" or char == "[" or char == "{":
                self.push(char)
            elif char == ")" or char == "]" or char == "}":
                if self.is_empty():
                    return False
                self.pop()
        if self.is_empty():
            return True
        return False

if __name__ == "__main__":
    stack = Stack()
    # push operations
    print("*****Push operations*****")
    print(stack.push(10))
    print(stack.push(20))
    print(stack.push(30))
    # peek operations
    print("*****Peek operations*****")
    print(stack.peek())
    # pop operations
    print("*****Pop operations*****")
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    # check if stack is empty
    print("*****Check if stack is empty*****")
    print(stack.is_empty())
    # reverse a string
    print("*****Reverse a string*****")
    print(stack.reverse_string("hello"))
    print(stack.reverse_string("We will conquere COVID-19"))
    # check if parenthesis are balanced
    print("*****Check if parenthesis are balanced*****")
    print(stack.parenthesis_checker("({a+b})"))
    print(stack.parenthesis_checker("))((a+b}{"))
    print(stack.parenthesis_checker("((a+b))"))
    print(stack.parenthesis_checker("))"))
    print(stack.parenthesis_checker("[a+b]*(x+2y)*{gg+kk}"))
    