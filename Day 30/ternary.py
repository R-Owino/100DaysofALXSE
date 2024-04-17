#!/usr/bin/python3
""" Ternary search algorithm """

import random

"""
Steps:
1. Divide the array into three parts by calculating 2 mid points i.e
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3
2. Compare the target element with both mid elements
3. If the key does not compare to either mid point elements, check if it exists
   in the left subarray or mid subarray or right subarray
     key < arr[mid1]
     key > arr[mid2]
4. If the key is less than mid1, concentrate the search in the left subarray,
   if it is greater than mid2, concentrate the search in the right subarray
   else, concentrate the search in the mid subarray
5. Repeat steps 1-3 for whatever subarray where the key could possibly be
   until the key is found
6. If the key is not found, return -1

Ternary search can be done iteratively and recursively. Let's see both below
First, we'll sort the list using quick sort, then we'll perform ternary search
"""

def quicksort(arr: list) -> list:
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

def select_pivot(arr: list) -> int:
    """ select the pivot element using the median of medians algorithm """
    if len(arr) <= 5:
        return sorted(arr)[len(arr) // 2]
    sublists = [sorted(arr[i:i+5]) for i in range(0, len(arr), 5)]
    medians = [sl[len(sl) // 2] for sl in sublists]
    return select_pivot(medians)

def ternarySearch_iterative(arr: list, key: int, left: int, right: int) -> int:
    """
    Implementing the ternary search iteratively
    """
    while left <= right:
        # calculate the mid1, mid2
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        # check if key is at any mid point
        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2
        
        # if key is not at any mid point, check which subarray
        # possibly contains the key
        # repeat the search in that subarray
        if key < arr[mid1]:
            right = mid1 - 1
        elif key > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
        
    # key not found
    return -1

def ternarySearch_recursive(arr: list, key: int, left: int, right: int) -> int:
    """
    Implementing the ternary search recursively
    """
    if left > right:
        return -1
    # calculate the mid1, mid2
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3

    # check if key is at any mid point
    if arr[mid1] == key:
        return mid1
    if arr[mid2] == key:
        return mid2
    
    # if key is not at any mid point, check which subarray
    # possibly contains the key
    if key < arr[mid1]:
        return ternarySearch_recursive(arr, key, left, mid1 - 1)
    elif key > arr[mid2]:
        return ternarySearch_recursive(arr, key, mid2 + 1, right)
    else:
        return ternarySearch_recursive(arr, key, mid1 + 1, mid2 - 1)
    
    
# test cases
test_list = []
for _ in range(10):
    test_list.append(random.randint(0, 100))
print(f"Original list: {test_list}")

sorted = quicksort(test_list)
print(f"Sorted list: {sorted}")

key = int(input("Enter the key to search: "))
x = len(test_list)

# iterative search
result = ternarySearch_iterative(sorted, key, 0, x-1)
# if result == -1:
#     print("Key not found")
print(f"{key} found at index {result} iteratively")

# recursive search
result = ternarySearch_recursive(sorted, key, 0, x-1)
# if result == -1:
#     print("Key not found")
print(f"{key} found at index {result} recursively")
