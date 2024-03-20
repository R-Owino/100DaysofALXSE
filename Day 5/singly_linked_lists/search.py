#!/usr/bin/python3
"""
Singly linked lists data structure
"""

###### Search operation in a singly linked list ######
"""
We can search for an element in an linked list iteratively or recursively
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
    def __init__(self, data):
        """ Initialize the node object """
        self.data = data
        self.next = None

class SinglyLinkedList:
    """ Singly linked list definition """
    def __init__(self):
        """Initialize the linked list object """
        self.head = None
    
    def push(self, new_data) -> None:
        """ Insert at the beggining of the linked list """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def iterativeSearch(self, key) -> bool:
        """ Search for an element in an linked list iteratively """
        current = self.head
        
        # Traverse the linked list until current is not NULL
        while current is not None:
            if current.data == key:
                return True # element found
            current = current.next
        return False # element not found
    
    def recursiveSearch(self, head, key) -> bool:
        """ Search for an element in an linked list recursively """
        # head is our base case
        if head is None:
            return False
        
        # if key is present in the head, return True
        if head.data == key:
            return True
        
        # else recursively search in the next node
        return self.recursiveSearch(head.next, key)
    

if __name__ == "__main__":

    # initialize the linked list
    llist = SinglyLinkedList()
    x = int(input("Enter the element to be searched in the linked list: "))

    llist.push(11)
    llist.push(21)
    llist.push(13)
    llist.push(30)
    llist.push(45)

    if llist.iterativeSearch(x):
        print(f"{x} is present in the linked list")
    else:
        print(f"{x} is not present in the linked list")

    if llist.recursiveSearch(llist.head, x):
        print(f"{x} is present in the linked list")
    else:
        print(f"{x} is not present in the linked list")
