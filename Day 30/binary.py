#!/usr/bin/python3
""" Binary Search algorithm """

import random

"""
Steps:
1. Divide the array into two halves by calculating the mid element
2. Compare the target element with the mid element. If the target is less than the mid element,
   move to the left, and if it is greater than the mid, move to the right of the search space
3. Repeat step 1 and 2 until the target is found
4. If the key matches the value of the mid element, stop the search and return the index where the value is

Binary search can be done iteratively and recursively. Let's see both below
"""

def bin_search(arr: list, key: int, left: int, right: int) -> int:
    """
    Implementing binary search iteratively

    Args:
        arr: list of elements
        key: element to search
        left: left search space
        right: right search space
    """
    while left <= right:
        mid = left + (right - left) // 2

        # if the element is present at the middle itself
        if arr[mid] == key:
            return mid

        # if the element is smaller than mid, then it can only
        # be present in the left subarray
        elif arr[mid] < key:
            left = mid + 1

        # else the element can only be present in the right subarray
        else:
            right = mid - 1

    # element not found
    return -1

def binary_search(arr: list, key: int, left: int, right: int) -> int:
    """ 
    Implementing binary search recursively

    Args:
        arr: list of elements
        key: element to search
        left: left search space
        right: right search space
    """

    # base case
    if left > right:
        return -1

    mid = left + (right - left) // 2

    # if the element is present at the middle itself
    if arr[mid] == key:
        return mid

    # if the element is smaller than mid, then it can only
    # be present in the left subarray
    elif arr[mid] < key:
        return binary_search(arr, key, mid + 1, right)

    # else the element can only be present in the right subarray
    else:
        return binary_search(arr, key, left, mid - 1)
    

# test case
test_list = []
for _ in range(10):
    test_list.append(random.randint(0, 100))
print(f"Original list: {test_list}")

key = int(input("Enter the key to search: "))
x = len(test_list)

result = bin_search(test_list, key, 0, x-1)

