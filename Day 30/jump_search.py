#!/usr/bin/python3
""" Jump search algorithm """

import math
from typing import List, Optional

"""
Steps:
1. Calculate the length of the array
2. Calculate the squareroot of that length to get the block size
3. Skip the array elements the number of times determined
   by the block size starting from the first element
4. Repeat step 3 until the last element in a block is 
   greater than the target element
5. Perform linear search on the block with the target element
5. Return the index of the target element else -1 if not found
"""

def jump_search(arr: List[int], key: int) -> Optional[int]:
    """
    Implementation of jump search algorithm

    Args:
        arrr - a list of integers
        key - target element

    Returns:
        index of the target element, else -1
    """
    # calculate the block size to be jumped
    n = len(arr)
    block_size = int(math.sqrt(n))

    # find the block where the target element can be found
    prev = 0
    while arr[min(block_size, n) - 1] < key:
        prev = block_size
        block_size += int(math.sqrt(n))
        if prev >= n:
            return -1

    # perform linear search on the block
    i = prev
    while arr[i] < key:
        i += 1

        # element not found if we reached the end of the block
        if i == min(block_size, n):
            return -1

    # element found
    if arr[i] == key:
        return i
    
    return -1 

# test case
test_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
print(f"Original list: {test_list}")

key = int(input("Enter the key to search: "))

result = jump_search(test_list, key)
if result == -1:
    print("Key not found")
print(f"{key} found at index {result}")
