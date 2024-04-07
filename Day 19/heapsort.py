#!/usr/bin/python3
""" Heap sort algorithm """

import random

"""
Steps:
1. Create a max heap from the input data.
  - In a max heap, for any given node i, the value of i is greater than
    or equal to the value of its children
2. Swap the first (largest) element with the last element
  - Largest item is stored in the root of the heap
  - Replace it with the last item of the heap then reduce the size of the heap by 1
3. Heapify the root of the tree
  - Re-arrange the heap so that the largest element is at the root
  - Repeat step 2 while the size of the heap is greater than 1
"""

def heapify(arr, n, i):
    """ Arrange the elements of an array into a max heap """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    """ Heap sort implementation """
    if len(arr) == 0:
        return "List is empty"
    if len(arr) < 2:
        return arr
    
    n = len(arr)

    # Build the max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

# test case
test_list = []
for _ in range(17):
    test_list.append(random.randint(0, 100))
print(f"Original list: {test_list}")

sorted = heapsort(test_list)
print(f"Sorted list: {sorted}")
