#!/usr/bin/python3
"""
Queue data structure
"""
import time
from queue03 import Queue

"""
Program that prints binary numbers from 1-10 using queues
"""

def print_binary_numbers():
    """ Print binary numbers from 1 to 10 using Queue """
    queue = Queue()
    queue.enqueue("1")

    for _ in range(10):
        binary_number = queue.dequeue()
        print(binary_number)

        queue.enqueue(binary_number + "0")
        queue.enqueue(binary_number + "1")

        time.sleep(1)  # delay for 1 second between each iteration

if __name__ == "__main__":
    print_binary_numbers()
