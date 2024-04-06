#!/usr/bin/python3
""" Quick sort algorithm """

import random

"""
Steps:
1. Using the median of medians algorithm, find the pivot element
2. Partition the array using the pivot element
3. Call quicksort recursively on the two halves
4. Merge the two halves
"""

def quicksort(arr):
    """ 
    Quick sort implementation 
    - Divides the array into 3 parts:
        - less than pivot
        - equal to pivot
        - greater than pivot
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = select_pivot(arr)
        less = [x for x in arr if x < pivot]
        equal = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return quicksort(less) + equal + quicksort(greater)

def select_pivot(arr):
    """ select the pivot element using the median of medians algorithm """
    if len(arr) <= 5:
        return sorted(arr)[len(arr) // 2]
    sublists = [sorted(arr[i:i+5]) for i in range(0, len(arr), 5)]
    medians = [sl[len(sl) // 2] for sl in sublists]
    return select_pivot(medians)

# Test case
test_list = []
for _ in range(17):
    test_list.append(random.randint(0, 100))
print(f"Original list: {test_list}")

sorted = quicksort(test_list)
print(f"Sorted list: {sorted}")
