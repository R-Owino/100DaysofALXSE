#!/usr/bin/python3
""" Binary Search algorithm """

import random 

"""
Steps:
1. Divide the array into two halves by calculating the mid element
2. Compare the target element with the mid element. If the target is less than the mid element,
   move to the left, and if it is greater than the mid, move to the right of the search space
3. Repeat step 1 and 2 until the target is found
4. If the key matches the value of the mid element, stop the search and
   return the index where the value is

Binary search can be done iteratively and recursively. Let's see both below
First, we'll sort the list using quick sort, then we'll perform binary search
Ideally, quicksort should be imported from "Day 19" directory, but the space is giving
a hard time, so we'll paste the quick sort code here
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

def binary_search_iterative(arr: list, key: int, left: int, right: int) -> int:
    """
    Perform an iterative binary search on a sorted array

    Args:
        arr (list): The sorted array to search
        key (int): The value to search for
        left (int): The leftmost index of the array segment to search
        right (int): The rightmost index of the array segment to search

    Returns:
        int: The index of the key in the array, or -1 if the key is not found
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

def binary_search_recursive(arr: list, key: int, left: int, right: int) -> int:
    """ 
    Perform an recursive binary search on a sorted array

    Args:
        arr (list): The sorted array to search
        key (int): The value to search for
        left (int): The leftmost index of the array segment to search
        right (int): The rightmost index of the array segment to search

    Returns:
        int: The index of the key in the array, or -1 if the key is not found
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
        return binary_search_recursive(arr, key, mid + 1, right)

    # else the element can only be present in the right subarray
    else:
        return binary_search_recursive(arr, key, left, mid - 1)

# test case
test_list = [2, 3, 4, 10, 40]
for _ in range(10):
    test_list.append(random.randint(0, 100))
print(f"Original list: {test_list}")

sorted = quicksort(test_list)
print(f"Sorted list: {sorted}")

key = int(input("Enter the key to search: "))
x = len(test_list)

# iterative search
result = binary_search_iterative(test_list, key, 0, x-1)
if result == -1:
    print("Key not found")
else:
    print(f"Key found at index {result} iteratively")

# recursive search
result = binary_search_recursive(test_list, key, 0, x-1)
if result == -1:
    print("Key not found")
else:
    print(f"Key found at index {result} recursively")
