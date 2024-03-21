#!/usr/bin/python3
"""
Singly linked lists data structure
"""

###### Delete operations performed on a singly linked list ######
"""
1. Delete the first node in the linked list
    Approach:
    - Point the head to the next node
    - Free unused memory

2. Delete the last node in the linked list
    Approach:
    - Iterate to the last node
    - Point the previous node to NULL
    - Free unused memory

3. Delete a given node in the linked list
    Approach:
    - Check if the given node exists, if not terminate the process
    - Keep track of the pointer before and after the node to delete
    - Change the next pointer of the previous node to point to the next
    pointer of the node to be deleted
    - Free the memory of the node to be deleted
"""

class Node:
    """ Node definition """
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
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, position) -> None:
        """ Delete a given node in the linked list """
        if self.head is None or position < 0:
            print("Invalid position")
            return
        if position == 0:
            self.head = self.head.next
            return
        temp = self.head
        for _ in range(position - 1):
            temp = temp.next
            if temp is None:
                return
        temp.next, temp = temp.next.next, temp.next.next

    def deleteHead(self) -> None:
        """ Delete the first node in the linked list """
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    def deleteTail(self) -> None:
        """ Delete the last node in the linked list """
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        prev = None
        current = self.head
        while current.next:
            prev = current
            current = current.next
        prev.next = None

    def printList(self) -> None:
        """ Prints the linked list """
        current = self.head
        while current:
            print(current.data, end=" --> ")
            current = current.next
        print(None)


if __name__ == "__main__":
    llist = SinglyLinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.push(6)

    print("Linked list before deletion:")
    llist.printList()

    # delete from beginning
    llist.deleteHead()
    print("Linked list after deleting from beginning:")
    llist.printList()

    # delete from head
    llist.deleteTail()
    print("Linked list after deleting from end:")
    llist.printList()

    # delete at a given position
    llist.deleteNode(2)
    print("Linked list after deleting at a given position:")
    llist.printList()
