#!/usr/bin/python3
""" Bubble sort algorithm """

import random

"""
Steps:
- For each element in a list:
  1. Start from the beggining of the list
  2. Compare every pair of adjacent items and swap them if they're
     in the wrong order - largest element should be bubbled to the end
  3. Repeat until no more swaps are needed and the list is ordered in
     ascending order
"""

def bubble_sort(arr):
    """ Sort using bubble sort """
    if len(arr) == 0:
        return "List is empty"
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test cases
test_list = []
for _ in range(20):
    test_list.append(random.randint(0, 100))
print(f"Original list: {test_list}")

sort = bubble_sort(test_list)
print(f"Sorted list: {sort}")
