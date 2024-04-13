#!/usr/bin/python3
""" Linear Search algorithm """

import random

"""
Method 1:
1. Initialize the search index variable i to 0
2. Set the last element of the list as the search key
3. While the search key is not equal to the current element, increment the search index
4. If i is less than the size of the array or arr[i] is equal to the search key,
   return the value of i - index of the search key
5. Otherwise return -1 because the search key was not found
"""

def sentinelSearch(arr: list, key: int, x: int) -> int:
    """ 
    Sentinel search implementation 
    
    Args:
        arr: list of elements
        key: element to search
        x: length of the array
    """
    # find the last ement of the array
    last = arr[x-1]

    # set the last element as the search key
    arr[x-1] = key
    i = 0

    while (arr[i] != key):
        i += 1
    
    # set back the last element
    arr[x-1] = last

    if i < x or arr[i] == key:
        return i
    return -1

# test case
test_list = []
for _ in range(10):
    test_list.append(random.randint(0, 100))
print(f"Original list: {test_list}")

key = int(input("Enter the key to search: "))
x = len(test_list)
result = sentinelSearch(test_list, key, x)
if result == -1:
    print("Key not found")
else:
    print(f"Key found at index {result}")
