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

###### Delete operations performed on a circular linked list ######
"""
1. Delete the first node in the linked list
    Approach:
    - Point the head to the next node
    - If there's no next node, free the space
    - Else, set the pointer of the last node to point to the next node to complete the circle

2. Delete a node between nodes
    Approach:
    - Traverse to the given node
    - Point the next of the previous node to the next node
    - Free the memory of the node to be deleted

3. Delete the last node in the linked list
    Approach:
    - Traverse to the last node
    - Point the next of the second last node to the first node
    - Free the memory of the deleted node
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

    def deleteHead(self) -> None:
        """ Delete the first node in the linked list """
        if self.head is None:
            print("List is empty")
            return
        # check if the list has only one node
        if self.head.next == self.head:
            self.head = None
            self.last = None
        else:
            self.last.next = self.head.next
            self.head = self.head.next

    def deleteTail(self) -> None:
        """ Delete the last node in the linked list """
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        # Traverse until the second last node
        while current.next.next != self.head:
            current = current.next
        # Update the last node and disconnect it from the list
        self.last = current
        self.last.next = self.head

    def deleteNode(self, prev_node) -> None:
        """ Delete a given node in the linked list """
        current = self.head
        # check if head is to be deleted
        if current.data == prev_node:
            if current.next == self.head:
                self.head = None
                self.last = None
            else:
                self.last.next = current.next
                self.head = current.next
            return

        # search for the node to be deleted
        while current.next.data != prev_node:
            current = current.next
            # reached the end of the list
            if current.next == self.head:
                print(f"{prev_node} is not present in the list")
                return
        # if current.next is the last node
        if current.next == self.last:
            self.last = current
        current.next = current.next.next
    
    def printList(self) -> None:
        """ Print the linked list """
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" --> ")
            current = current.next
            if current == self.head:
                break
        print(self.head.data)


if __name__ == "__main__":
    cll = CircSinglyLinkedList()
    
    # Insert nodes
    cll.push(5)
    cll.push(4)
    cll.push(3)
    cll.push(2)
    cll.push(1)

    print("Circular linked list:")
    cll.printList()

    # Delete the first node
    cll.deleteHead()
    print("\nLinked list after deleting the first node:")
    cll.printList()

    # Delete a node between nodes
    cll.deleteNode(3)
    print("\nLinked list after deleting a node between nodes:")
    cll.printList()

    # Delete the last node
    cll.deleteTail()
    print("\nLinked list after deleting the last node:")
    cll.printList()
