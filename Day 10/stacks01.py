#!/usr/bin/python3
"""
Stacks data structure
"""

###### Implementing stacks as an array ######
"""
- When implementing a stack as an array, the stack takes the form of ann array
- The elements in the stack are indexed
- The only difference is all operations happen from the top
- The main operations are push(add), pop(remove) and peek(return without removing)

- Steps to push:
    - Using a variable, check if the stack is full and return appropriate message
    - Else, add the element to the top of the stack
    - Return the element that was pushed

- Steps to pop:
    - Using a variable, check if the stack is empty and return appropriate message
    - Store the topmost value in the stack in a variable
    - Decrement the first variable by 1 to remove the topmost value
    - Return the removed value

- Steps to peek:
    - Using a variable, check if the stack is empty and return appropriate message
    Else, return the value of the topmost element
"""

class Stack:
    """ Implementing a stack as an array """
    def __init__(self, capacity) -> None:
        """ Initialize the stack object """
        self.capacity = capacity
        self.stack = []
        self.top = -1

    def is_full(self) -> None:
        """ Check if the stack is full """
        if self.top == self.capacity - 1:
            return True
        return False
    
    def is_empty(self) -> None:
        """ Check if the stack is empty """
        if self.top == -1:
            return True
        return False
    
    def push(self, data) -> None:
        """ Add an element to the top of the stack """
        if self.is_full():
            return "Stack is full, cannot add element"
        self.top += 1
        self.stack.append(data)
        return f"Element {data} added to the top of the stack"
    
    def pop(self) -> None:
        """ Remove an element from the top of the stack """
        if self.is_empty():
            return "Stack is empty, cannot remove element"
        removed_element = self.stack.pop()
        self.top -= 1
        return f"Element {removed_element} removed from the stack"
    
    def peek(self) -> None:
        """ Return the topmost element in the stack """
        if self.is_empty():
            return "Stack is empty"
        return f"Top element in the stack is: {self.stack[self.top]}"
    

if __name__ == "__main__":
    stack = Stack(5)
    # push operation
    print(stack.push(10))
    print(stack.push(20))
    print(stack.push(30))
    print(stack.push(40))
    print(stack.push(50))
    print(stack.push(60)) # attempt to push to a full stack

    # peek operation
    print(stack.peek())

    # pop operation
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop()) # attempt to pop from an empty stack
