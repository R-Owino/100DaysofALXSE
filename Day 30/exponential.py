#!/usr/bin/python3
""" Exponential search algorithm """

from typing import List, Optional

"""
Steps:
1. Find the range where the key could possibly be exponentially
   - for an array, arr, start at the second element arr[1] and exponenetially
     increase the index (1, 2, 4, 8, 16, ...) until we find an interval [i/2, i]
     where the target could be
   - This is done by checking if the element at index i is greater than the target. 
     If it is, then we know the target must be within the interval [i/2, i]
2. Perform binary search on the interval [i/2, i]
"""

def exponential_search(arr: List[int], key: int) -> Optional[int]:
    """
    Implementation of exponential search algorithm

    Args:
        arrr - a list of integers
        key - target element

    Returns:
        index of the target element, else -1
    """
    # check if target is at the 0th index
    if arr[0] == key:
        return 0

    # find the range where the key could possibly be
    i = 1
    while i < len(arr) and arr[i] <= key:
        i *= 2

    # perform binary search on the interval [i/2, i]
    return binary_search(arr, key,  i // 2, min(i, len(arr)))

def binary_search(arr: List[int], key: int, left: int, right: int) -> Optional[int]:
    """
    Implementation of binary search algorithm

    Args:
        arr - a list of integers
        key - target element
        left - left index
        right - right index

    Returns:
        index of the target element, else -1
    """
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return binary_search(arr, key, mid + 1, right)
        return binary_search(arr, key, left, mid - 1)

# test case
test_list = [2, 3, 4, 10, 40]
print(f"Original list: {test_list}")

key = int(input("Enter the key to search: "))

result = exponential_search(test_list, key)
if result != -1:
    print(f"{key} found at index {result}")
