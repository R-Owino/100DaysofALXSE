#!/usr/bin/python3
""" Selection sort algorithm """

import random

"""
Steps:
- For each element in the array:
  1. Find the smallest/largest element and swap it with the first element
  2. Find the second smallest/largest element and swap with with the second element in the array
  3. Repeat the steps until all elements are sorted in desired order
"""

def selection_sort_asc(arr):
    """ Selection sort in ascending order """
    if len(arr) == 0:
        return "List is empty"
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def selection_sort_desc(arr):
    """ Selection sort in descending order """
    if len(arr) == 0:
        return "List is empty"
    for i in range(len(arr)):
        max_index = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]
    return arr

# Test cases
# generate random numbers for testing
test_list = []
for _ in range(20):
    test_list.append(random.randint(0, 100))
print(f"Original list: {test_list}")

sort_asc = selection_sort_asc(test_list)
print(f"Ascending order sort: {sort_asc}")

sort_desc = selection_sort_desc(test_list)
print(f"Descending order sort: {sort_desc}")
