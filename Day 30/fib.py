#!/usr/bin/python3
""" Fibonacci Search Algorithm """

from typing import Optional

"""
Steps:
1. Find F(k) - the kth fibonacci number, which is greater than or equal to the length of the array, n
2. If F(k) = 0, then return -1
3. Using an initial offset of -1, find the index in the array where the target element could be
   - offset = -1
   - arr[i] = min(offset + F(k-2), n-1)
4. If key is equal to arr[i], return i and stop the search
5. Else, if key is greater than arr[i]:
   - k = k-1, offset = i
   - repeat step 3,4
6. Else:
   - k = k-2
   - repeat step 3,4
"""

def fibonacci_search(arr: list, key: int) -> Optional[int]:
    """
    Implementation of fibonacci search algorithm

    Args:
        arr - a list of integers
        key - target element

    Returns:
        index of the target element, else -1
    """
    # initialize the fib numbers
    fibk2 = 0 # F(k-2)'th fib number
    fibk1 = 1 # F(k-1)'th fib number
    fibk = fibk1 + fibk2 # F(k)'th fib number

    # find fibk where fibk >= len(arr)
    while fibk < len(arr):
        fibk2 = fibk1
        fibk1 = fibk
        fibk = fibk1 + fibk2
    
    # initialize the offset
    offset = -1

    while fibk > 1:
        # check if fibk2 is a valid index
        i = min(offset + fibk2, len(arr) - 1)

        # if key is less than the value at i
        # subset the array from offset to i
        if arr[i] < key:
            fibk = fibk1
            fibk1 = fibk2
            fibk2 = fibk - fibk1
            offset = i

        # if key is greater than the value at i
        # subset the array after i+1
        elif arr[i] > key:
            fibk = fibk2
            fibk1 = fibk1 - fibk2
            fibk2 = fibk - fibk1

        # if key is equal to the value at i
        else:
            # check for duplicates, if they're allowed
            indices = [i]

            # duplicates on the left
            j = i-1
            while j >= 0 and arr[j] == key:
                indices.append(j)
                j -= 1
            # duplicates in the right
            j = i+1
            while j < len(arr) and arr[j] == key:
                indices.append(j)
                j += 1
            return indices
        
    # compare the last element with key
    if fibk1 and arr[offset + 1] == key:
        return [offset + 1]
        
    # element not found
    return -1

# test case
test_list = [10, 13, 15, 15, 19, 20, 21, 23, 25, 27, 29, 30, 31, 50]
print(f"Original list: {test_list}")

key = int(input("Enter the key to search: "))

result = fibonacci_search(test_list, key)
if result == -1:
    print("Key not found")
print(f"{key} found at index {result}")
