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
- The last node in the linked list becomes the top of the stack (rem LIFO)

- Steps to push:
    - First, create a node and allocate memory to it
    - If the list is empty, push the node as the first node in the list. This will assign a value to the
    data part of the node and give NULL to the address part
    - If the list already has some nodes, add the new node to the beginning
"""