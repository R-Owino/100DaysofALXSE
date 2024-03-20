#!/usr/bin/python3
"""
Doubly linked data structure
"""

###### Insertion operations performed on a doubly linked list ######
"""
1. Insert at the beggining of the linked list
    Approach:
    - Allocate memory for the new node and populate its data field
    - Set previous pointer of the new node to NULL
    - If the list is empty:
        - Set the new node as the head
        - Set the next pointer to NULL
    - Else:
        - Set the next pointer of the new node to current head
        - Set previous pointer of current head to point to new node
        - Update head pointer to point to new node

2. Insert after a given node in the linked list
    Approach:
    - Create the new node to be inserted and populate its data field
    - Point the next of the new node to the next of the given node
    - Point the previous of the new node to the given node
    - Set the next of the given node's next node to the new node

3. Insert before a given node in the linked list
    Approach:
    - Create the new node to be inserted and populate its data field
    - Point the previous of the new node to the previous of the given node
    - Set the previous of the given node's previous node to the new node
    - Point the next of the new node to the given node
    - Set the next pointer of the previous of the new node to the new node

4. Insert at the end of the linked list
    Approach:
    - Create the new node and populate its data field
    - Set the next pointer of the new node to NULL
    - If the list is empty, set the new node as head
    - Else, traverse to the end of the list
    - Set the next pointer of the last node to the new node
    - Set the previous pointer of the new node to the last node
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

    def insertAfter(self, prev_node, new_data):
        """ Insert after a given node in the linked list """

        # check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must not be null")
            return
        
        # create the new node
        new_node = Node(new_data)

        # set next of new node as next of prev_node
        new_node.next = prev_node.next

        # set the next of prev_node as new_node
        prev_node.next = new_node

        # set prev of new_node as prev_node
        new_node.prev = prev_node

        # set prev of new_node's next node as new_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def insertBefore(self, next_node, new_data):
        """ Insert before a given node in the linked list """

        # check if the given next_node exists
        if next_node is None:
            print("The given next node must not be null")
            return
        
        # create the new node
        new_node = Node(new_data)

        # set prev of new node as prev of next_node
        new_node.prev = next_node.prev
        
        # set the prev of next_node as new_node
        next_node.prev = new_node
        
        # set next of new_node as next of next_node
        new_node.next = next_node

        # set prev of new_node's next node as new_node
        if new_node.prev is not None:
            new_node.prev.next = new_node
        else:
            self.head = new_node

    def append(self, new_data):
        """ Insert at the end of the linked list """

        # create the new node
        new_node = Node(new_data)
        last = self.head

        # set next of new_node as null
        new_node.next = None

        # if the list is empty, set the new node as head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        
        # else traverse to the end
        while(last.next is not None):
            last = last.next

        # change the next of last node
        last.next = new_node

        # set prev of new node as last node
        new_node.prev = last

    def printList(self):
        """ Print the linked list """
        current = self.head
        while current:
            print(current.data, end=" <--> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(6)
    dll.push(7)
    dll.push(1)
    dll.append(4)

    print("Doubly linked list before insertion:")
    dll.printList()

    dll.insertBefore(dll.head.next, 8)
    print("\nDoubly linked list after insertion before a given node:")
    dll.printList()

    dll.insertAfter(dll.head, 5)
    print("\nDoubly linked list after insertion after a given node:")
    dll.printList()
