#!/usr/bin/python3
"""
Doubly linked data structure
"""

###### Deletion operations performed on a doubly linked list ######
"""
1. Delete the first node in the linked list
    Approach:
    - Point the head to the next node
    - Free unused memory

2. Delete the a given node in the linked list
    Approach:
    - Check if the given node exists, if not terminate the process
    - Change the next pointer of the previous node to point to the next
    - Change the previous pointer of the next node to point to the previous
    - Free the memory of the node to be deleted

3. Delete the last node in the linked list
    Approach:
    - Iterate to the last node
    - Point the previous node to NULL
    - Free unused memory
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

    def deleteNode(self, node):
        """ Delete a given node in the linked list """
        # check if the given node exists
        if node is None:
            print("Can't delete null node")
            return
        
        # set prev if given node is not head
        if node.prev is not None:
            node.prev.next = node.next

        # set next if given node is not tail
        if node.next is not None:
            node.next.prev = node.prev
    
    def deleteHead(self):
        """ Delete the first node in the linked list """
        # check if the list is empty
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None
    
    def deleteTail(self):
        """ Delete the last node in the linked list """
        # check if list is empty
        if self.head is None:
            print("List is empty")
            return
        
        # if list has only one node
        if self.head.next is None:
            self.head = None
            return
        
        # iterate to the last node
        last = self.head
        while last.next:
            last = last.next
        last.prev.next = None

    def printList(self):
        """ Print the linked list """
        current = self.head
        while current:
            print(current.data, end=" <--> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    dll = DoublyLinkedList()
    # insert nodes
    dll.push(10)
    dll.push(20)
    dll.push(30)
    dll.push(40)

    print("Doubly linked list before deletion:")
    dll.printList()

    dll.deleteHead()
    print("\nDoubly linked list after deletion from head:")
    dll.printList()

    dll.deleteTail()
    print("\nDoubly linked list after deletion from tail:")
    dll.printList()

    dll.deleteNode(dll.head.next)
    print("\nDoubly linked list after deletion from a given node:")
    dll.printList()        
    