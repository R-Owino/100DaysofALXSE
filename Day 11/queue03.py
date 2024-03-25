#!/usr/bin/python3
"""
Queue data structure
"""
import time
import threading

from collections import deque

###### Implementing queues as a collection ######
"""
Designing a food ordering system where the program will run two threads,

    - Place Order: This thread will be placing an order and inserting that into a queue.
        This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
    - Serve Order: This thread will server the order.
        Also start this thread 1 second after place order thread is started.

"""

class Queue:
    """ Implementing a queue as a collection """
    def __init__(self) -> None:
        """ Initialize the queue object """
        self.queue = deque()

    def is_empty(self) -> bool:
        """ Check if the queue is empty """
        return len(self.queue) == 0

    def enqueue(self, data) -> None:
        """ Add an element to the rear of the queue """
        self.queue.appendleft(data)
        return f"Element {data} added to the rear of the queue"
    
    def dequeue(self) -> None:
        """ Remove an element from the front of the queue """
        if self.is_empty():
            return "Queue is empty, cannot remove element"
        return self.queue.pop()
    
    def peek(self) -> None:
        """ Return the element at the front of the queue """
        return self.queue[-1]

def place_orders(queue) -> None:
    """ Place orders in the queue """
    while True:
        for order in orders:
            queue.enqueue(order)
            print(f"{order} placed in the queue")
            time.sleep(0.5)

def serve_orders(queue) -> None:
    """ Serve orders from the queue """
    time.sleep(1) # start serving after 1 second of placing orders
    while True:
        if not queue.is_empty():
            order = queue.dequeue()
            print(f"{order} served")
        else:
            print("Queue is empty")
        time.sleep(2) # serve an order every 2 seconds

if __name__ == "__main__":
    queue = Queue()
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_orders, args=(queue,))
    t2 = threading.Thread(target=serve_orders, args=(queue,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
