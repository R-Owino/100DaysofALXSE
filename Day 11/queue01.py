#!/usr/bin/python3
"""
Queue data structure
"""

###### Implementing queues as an array ######
"""
- The main operations in a queue are enqueue, dequeue and peek

- Steps to enqueue:
    - Check if the queue is full
    - If the queue is full, return an overflow error
    - Else, increment the rear pointer to point to the next available empty space
    - Add the element to the queue where the rear pointer is
    - Return the element that was enqueued

- Steps to dequeue:
    - Check if the queue is empty
    - If the queue is empty, return an underflow error
    - Else, access the element at the front of the queue, where the front pointer is pointing
    - Increment the front pointer to point to the next element
    - Return the dequeued element

- Steps to peek:
    - Check if the queue is empty
    - If the queue is empty, return an underflow error
    - Else, return the element where the front pointer is pointing
"""

class Queue:
    def __init__(self, capacity) -> None:
        """ Initialize the queue object """
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_full(self) -> None:
        """ Check if the queue is full """
        return self.size == self.capacity

    def is_empty(self) -> None:
        """ Check if the queue is empty """
        return self.size == 0

    def enqueue(self, data) -> None:
        """ Add an element to the rear of the queue """
        if self.is_full():
            return "Queue is full, cannot add element"
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data
        self.size += 1
        return f"Element {data} added to the rear of the queue"
    
    def dequeue(self) -> None:
        """ Remove an element from the front of the queue """
        if self.is_empty():
            return "Queue is empty, cannot remove element"
        removed_element = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return f"Element {removed_element} removed from the front of the queue"

    def peek(self) -> None:
        """ Return the element at the front of the queue """
        if self.is_empty():
            return "Queue is empty"
        return f"Element at the front of the queue is: {self.queue[self.front]}"
    

if __name__ == "__main__":
    queue = Queue(5)
    # enqueue operations
    print(queue.enqueue(1))
    print(queue.enqueue(2))
    print(queue.enqueue(3))
    print(queue.enqueue(4))
    print(queue.enqueue(5))
    print(queue.enqueue(6)) # attempt to enqueue to a full queue

    # peek and dequeue operations
    print(queue.peek())
    print(queue.dequeue())
    print(queue.peek())
    print(queue.dequeue())
    print(queue.peek())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue()) # attempt to dequeue from an empty queue
    print(queue.peek())
