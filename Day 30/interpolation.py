#!/usr/bin/python3
""" Interpolation search algorithm """

import random
from typing import List, Optional

"""
Steps:
1. Start the search from the middle of the list
2. If it is a match, return the index of the item, and exit
3. If it is not a match, probe position
4. Divide the list using probing formula and find the new middle 
5. If data is greater than middle, search in higher sub-list
6. If data is smaller than middle, search in lower sub-list
7. Repeat until a match is found, and return the index of the item
8. If no match is found, return -1
"""

def interpolation_search(arr: List[int], key: int) -> Optional[int]:
    """
    Implementation of interpolation search algorithm

    Args:
        arrr - a list of integers
        key - target element

    Returns:
        index of the target element, else -1
    """
    left = 0
    right = len(arr) - 1

    while left <= right and key >= arr[left] and key <= arr[right]:
        # probe the position of the key
        pos = left + ((key - arr[left]) * (right - left)) // (arr[right] - arr[left])

        # if there is a match return the index of current element
        # else move the search to the left or right subarrays
        if arr[pos] == key:
            return pos
        elif arr[pos] < key:
            left = pos + 1
        else:
            right = pos - 1

    return -1

# test case
test_list = [10, 13, 15, 17, 19, 20, 21, 23, 25, 27, 29, 30, 31, 50]
print(f"Original list: {test_list}")

key = int(input("Enter the key to search: "))
n = len(test_list)

result = interpolation_search(test_list, key)
if result == -1:
    print("Key not found")
else:
    print(f"Key found at index {result}")
