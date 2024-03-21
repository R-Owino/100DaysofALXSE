#!/usr/bin/python3
"""
Doubly linked data structure
"""

###### Search operations performed on a doubly linked list ######
"""
Just like in singly linked lists, an element can be searched iteratively or recursively
1. Iterative search
    Approach:
    - Start from the head
    - Traverse the linked list
    - If the current value is equal to the key being searched, return True
    - Otherwise, move to next node
    - If the end of the linked list is reached and the key is not found, return False

2. Recursive search
    Approach:
    - Start from the head
    - If head is NULL, return False
    - If the current value is equal to the key being searched, return True
    - Else recursively search in the next node
"""

class Node:
    """ Node definition """
    def __init__(self, data) -> None:
        """ Initialize the node object """
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    """ Doubly linked list definition """
    def __init__(self) -> None:
        """ Initialize the linked list object """
        self.head = None
    
    def push(self, new_data):
        """ Insert at the beggining of the linked list """
        new_node = Node(new_data)

        # set next of new node as head and prev as null
        new_node.next = self.head
        new_node.prev = None

        # change prev of head node to new node
        if self.head is not None:
            self.head.prev = new_node
        
        # set new node as head
        self.head = new_node

    def iterativeSearch(self, key) -> bool:
        """ Iteratively seach for an element in the linked list """
        current = self.head
        while current:
            if current.data == key:
                return True # key found
            current = current.next
        return False # key not found
    
    def recursiveSearch(self, node, key) -> bool:
        """ Recursively search for an element in the linked list """
        # base case: if node is None or key is found
        if node is None:
            return False
        if node.data == key:
            return True
        
        # recursivley search in the next node
        return self.recursiveSearch(node.next, key)
 

if __name__ == "__main__":
    dll = DoublyLinkedList()
    x = int(input("Enter the element to be searched in the linked list: "))

    dll.push(10)
    dll.push(24)
    dll.push(43)
    dll.push(54)
    dll.push(67)
    dll.push(78)

    if dll.iterativeSearch(x):
        print(f"{x} is present in the linked list")
    print(f"{x} is not present in the linked list")

    if dll.recursiveSearch(dll.head, x):
        print(f"{x} is present in the linked list")
    print(f"{x} is not present in the linked list")
