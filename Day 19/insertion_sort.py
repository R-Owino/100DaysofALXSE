#!/usr/bin/python3
""" Insertion sort algorithm """

import random

"""
Steps:
- For each element in the array:
  1. Assume the fisrt item is already in the sorted section of the list
  2. Start from the second element and compare it with the first
  3. If it is larger than the first, leave it as it is
  4. If it is smaller, move it to its correct position in the sorted list
  5. Repeat until all elements are sorted in desired order
"""

def insertion_sort(array: list) -> list:
    """ Sort array using insertion sort algorithm """

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

# Test case
# generate random numbers for testing
test_list = []
for _ in range(20):
    test_list.append(random.randint(0, 100))
print(f"Original list: {test_list}")

sort = insertion_sort(test_list)
print(f"Sorted list: {sort}")
