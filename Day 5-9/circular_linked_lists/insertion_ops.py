#!/usr/bin/python3
"""
Circular linked lists data structure
    - Both circular singly and doubly linked lists have the same operations as
    regular singly and doubly linked lists.
    - The only difference comes in pointing the next pointer of the last node from NULL
    to the first node
    - In circular singly linked list, the last node's next pointer points to the first node
    of the list
    - In circular doubly linked lists, the last node's next pointer points to the first node and the
    first's node previous pointer points to the last node
    
    - In the examples below, I will experiment with circular singly linked lists 
"""

###### Insertion operations performed on a circular linked list ######
"""
1. Insert at the beginning of the linked list
    Approach:
    - Create the new node and populate its data field
    - Set the next pointer of the new node to the current first node
    - Set the pointer of the last node to the new node
    - The new node becomes the head

2. Insert in between nodes in the linked list (before/after given nodes)
    Approach:
    - Create the new node and populate its data field
    - Traverse to the given node
    - Set the next pointer of the node before to the new node and the next pointer
    of the new node to the node after

3. Insert at the end of the linked list
    Approach:
    - Create and populate the new node
    - Set the next pointer of the last node to the new node
    - Set the next pointer of the new node to the first node
    - Set the new node as the last node
"""

class Node:
    """ Node definition """
    def __init__(self, data) -> None:
        """ Initialize the node object """
        self.data = data
        self.next = None

class CircSinglyLinkedList:
    """ Circular singly linked list definition """
    def __init__(self) -> None:
        """ Initialize the linked list object """
        self.head = None
        self.last = None
    
    def push(self, new_data) -> None:
        """ Insert at the beginning of the linked list """
        new_node = Node(new_data)
        if self.head is None:
            self.head = None
            new_node.next = new_node
            self.last = new_node
        
        new_node.next = self.head
        self.last.next = new_node
        self.head = new_node

    def insertBetween(self, prev_node, new_data) -> None:
        """ Insert in between given nodes in the linked list """
        if self.head is None:
            print("The list is empty. Cannot insert between nodes")
            return
        
        new_node = Node(new_data)
        current = self.head
        while current:
            if current.data == prev_node:
                new_node.next = current.next
                current.next = new_node
                # if new node is inserted at the end, update the last pointer
                if current == self.last:
                    self.last = new_node
                return

            current = current.next
            # traverse the entire list if current is head
            if current == self.head:
                print(f"{prev_node} is not present in the list")
                return
            print(f"{prev_node} is not present in the list")

    def append(self, new_data) -> None:
        """ Insert at the end of the list """
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            self.last = new_node
        new_node.next = self.head
        self.last.next = new_node
        self.last = new_node

    def printList(self) -> None:
        """ Print the linled list """
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print(self.head.data)


if __name__ == "__main__":
    clist = CircSinglyLinkedList()

    clist.push(3)
    clist.push(2)
    clist.push(1)

    print("Linked list before insertion:")
    clist.printList()

    clist.insertBetween(3, 4)
    print("Linked list after insertion in between nodes:")
    clist.printList()

    clist.append(5)
    clist.append(6)
    print("Linked list after insertion at end:")
    clist.printList()
