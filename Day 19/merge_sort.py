#!/usr/bin/python3
""" Merge sort algorithm """

import random

"""
Steps:
1. Divide the element into two halves
2. Call merge sort recursively on the two halves
3. Merge the sorted halves into one sorted array
"""

def merge_sort(arr: list) -> list:
    """ Merge sort implementaton """
    if len(arr) < 2:
        return arr
    
    # define the sub-arrays
    left_arr = arr[:len(arr)//2]
    right_arr = arr[len(arr)//2:]

    # recursively call mersge sort on the sub-arrays
    merge_sort(left_arr)
    merge_sort(right_arr)

    # merge the sub-arrays
    i = 0 # left most item in left_arr
    j = 0 # left most item in right_arr
    k = 0 # index in the merged array

    while i < len(left_arr) and j < len(right_arr):
        # compare the left items
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    # transfer leftover items in the left_arr to merged arr
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    # transfer leftover items in the right_arr to merged arr
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

    return arr 

# Test cases
test_list = []
for _ in range(10):
    test_list.append(random.randint(0, 100))
print(f"Original list: {test_list}")

sorted = merge_sort(test_list)
print(f"Sorted array: {sorted}")
