#!/usr/bin/python3
"""
Singly linked lists data structure
"""

###### Insertion operations performed on a singly linked list ######
"""
1. Insert at the beggining of the linked list
    Approach:
    - Make the first node link to the new node
    - Remove head from the original first node
    - Make the new node as the new head

2. Insert after a given node in the linked list
    Approach:
    - Check if the given node exists, if not terminate the process
    - If the node exists, the element to be inserted is marked as a new node
    - Change pointer of the given node to point to the new node
    - Shift the original next pointer of the given node to the next pointer of new node

3. Insert at the end of the linked list
    Approach:
    - Iterate to the last node in the list
    - Change the pointer of the last node from NULL to the new node
    - Make the pointer of the new node to point to NULL
"""

class Node:
    """ Node definition example """
    def __init__(self, data) -> None:
        """ Initialize the node object """
        self.data = data
        self.next = None

class SinglyLinkedList:
    """ Singly linked list definition """
    def __init__(self) -> None:
        """ Initialize the linked list object """
        self.head = None

    def push(self, new_data) -> None:
        """ Insert at the beggining of the linked list """
        new_node = Node(new_data) # step 1&2
        new_node.next = self.head # step 3
        self.head = new_node # step 4
    
    def insertAfter(self, prev_node, new_data) -> None:
        """ Insert after a given node in the linked list """
        if prev_node is None:
            print("The given previous node must not be null")
            return
        new_node = Node(new_data) # step 1
        new_node.next = prev_node.next # step 2
        prev_node.next = new_node # step 3

    def append(self, new_data) -> None:
        """ Insert at the end of the linked list """
        new_node = Node(new_data)

        # make the new node head if the list is empty
        if self.head is None:
            self.head = new_node
            return
        
        # else iterate to the end
        last = self.head
        while last.next:
            last = last.next
        
        # step 3
        last.next = new_node

    def printList(self):
        """ Prints the linked list """
        current = self.head
        while current:
            print(current.data, end=" --> ")
            current = current.next
        print(None)


if __name__ == "__main__":
    llist = SinglyLinkedList()
    llist.append(6)
    llist.append(5)
    llist.push(7)
    llist.push(1)
    llist.push(10)
    llist.append(4)
    llist.insertAfter(llist.head.next, 8)
    llist.insertAfter(llist.head, 2)

    print("Linked list with insertion operations:")
    llist.printList()
