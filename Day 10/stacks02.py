#!/usr/bin/python3
"""
Stacks data structure
"""

###### Implementing stacks as an linked list ######
"""
- When using arrays to implement a stack we have to pre-define the number of elements the stack will have
- While this is good in some cases, we might need the stack to be dynamic to take in more elements
- In this case, we can use a linked list
- When using linked lists to implement a stack, the stack is contained in non-contigous memory
- The last element to be inserted will be the one accessible i.e the top

- Steps to push:
    - Check if the list is empty or not
    - Create a node and allocate memory to it
    - If the list is empty, push the node as the first node in the list. This will assign a value to the
    data part of the node and give NULL to the address part
    - If the list already has some nodes, add the new node to the beginning. To do this, assign the element to
    the address field of the new node and make a new node, which will be the list's top
    - If the list is full, return appropriate message

- Steps to pop:
    - Check if the list is empty, return NULL if it is
    - If there's only one node in the list, remove the head and return NULL
    - If there are more nodes, create a temp node and set it to the head
    - Set the head to the next node
    - Set the address field of the temp node to NULL

- Steps to peek:
    - Check if the list is empty, return NULL if it is
    - Else, return the value of the head
"""

class Node:
    """ Node definition """
    def __init__(self, data) -> None:
        """ Initialize the node object """
        self.data = data
        self.next = None

class Stack:
    """ Implementing a stack as an linked list """
    def __init__(self):
        """ Initialize the stack object """
        self.head = None

    def is_empty(self) -> None:
        """ Check if the stack is empty """
        if self.head is None:
            return True
        return False
    
    def push(self, data) -> None:
        """ Add an element to the top of the stack """
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        return f"Element {data} added to the top of the stack"
    
    def pop(self) -> None:
        """ Remove an element from the top of the stack """
        if self.is_empty():
            return "Stack is empty, cannot remove element"
        elif self.head.next is None:
            removed_element = self.head.data
            self.head = None
            return f"Element {removed_element} removed from the stack"
        else:
            removed_element = self.head.data
            self.head = self.head.next
            return f"Element {removed_element} removed from the stack"
        
    def peek(self) -> None:
        """ Return the value of the topmost element in the stack """
        if self.is_empty():
            return "Stack is empty"
        return f"Value of the topmost element in the stack is: {self.head.data}"
    

if __name__ == "__main__":
    stack = Stack()

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
