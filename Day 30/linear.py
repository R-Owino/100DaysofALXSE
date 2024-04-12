#!/usr/bin/python3
""" Linear Search algorithm """

import random

"""
Steps:
1. Start from the beginning of the array, index 0
2. Compare the target element, key, with each element in the array, arr[i]
3. If the element is found, return its index
4. If the element is not found, return -1
"""

def linear_search(arr: list, key: int, x: int) -> int:
    """ 
    Linear search implementation 
    
    Args:
        arr: list of elements
        key: element to search
        x: length of the array
    """
    for i in range(0, x):
        if arr[i] == key:
            return i
    return -1

# test case
test_list = []
for _ in range(10):
    test_list.append(random.randint(0, 100))
print(f"Original list: {test_list}")

key = int(input("Enter the key to search: "))
x = len(test_list)

result = linear_search(test_list, key, x)
if result == -1:
    print("Key not found")
else:
    print(f"Key found at index {result}")
