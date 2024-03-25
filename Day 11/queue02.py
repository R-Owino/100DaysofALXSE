#!/usr/bin/python3
"""
Queue data structure
"""

###### Implementing queues using a linked list ######
"""
- Linked lists give us the ability to dynamically create queues
- The operations are still similar to arrays implementation of queues

- Steps to enqueue:
    - Create a new node and populate its data field
    - If the queue is empty, make the new node the head and tail
    then increment the size of the queue by 1
    - Else, set the next pointer of the tail node to point to the new node
    - Set the rear pointer to point to the new node
    - Increment the size of the queue by 1

- Steps to dequeue:
    - Check if the queue is empty
    - If the queue is empty, return an underflow error
    - Else:
        - Store the head node in a temporary variable
        - Set the front pointer to point to the next node
        - Decrement the size of the queue by 1
        - If the queue becomes empty, set the rear pointer to NULL
        - Return the dequeued element

- Steps to peek:
    - Check if the queue is empty
    - If the queue is empty, return an underflow error
    - Else, return the value of the head node
"""

class Node:
    """ Node definition """
    def __init__(self, data) -> None:
        """ Initialize the node object """
        self.data = data
        self.next = None

class Queue:
    """ Implement a queue using a linked list """
    def __init__(self) -> None:
        """ Initialize the queue object """
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self) -> None:
        """ Check if the queue is empty """
        return self.size == 0

    def enqueue(self, data) -> None:
        """ Add an element to the rear of the queue """
        new_node = Node(data)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        return f"Element {data} added to the rear of the queue"

    def dequeue(self) -> None:
        """ Remove an element from the front of the queue """
        if self.is_empty():
            return "Queue is empty, cannot remove element"
        removed_element = self.front.data
        self.front = self.front.next
        self.size -= 1
        return f"Element {removed_element} removed from the front of the queue"

    def peek(self) -> None:
        """ Return the element at the front of the queue """
        if self.front is None:
            return "Queue is empty"
        return f"Element at the front of the queue is: {self.front.data}"
    
    def printQueue(self):
        """ Print the elements of the queue """
        temp = self.front
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print("None")
    

if __name__ == "__main__":
    queue = Queue()

    # enqueue operations
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)

    print("Queue: ", end="")
    queue.printQueue()

    # peek operation
    print(queue.peek())

    # dequeue operations
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    print("Queue: ", end="")
    queue.printQueue()

    # peek operation
    print(queue.peek())
