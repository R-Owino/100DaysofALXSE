#!/usr/bin/python3
""" Counting sort algorithm """

import random

"""
Steps:
1. Given an input list, create a count list to store the
   count of each unique element in the input list
   The steps for this would be:
     - Find the maximum element in the input list
     - Create a count list of size maximum element + 1
     - For each number in the input list, increment the corresponding index
       in the count list
     - example: 
        - input list = [2, 5, 2, 8, 5, 6, 8, 8]
        - count list = [0, 0, 2, 0, 0, 2, 1, 0, 3]
2. Create a sorted output list since we know how many times each value in the
   input list appears. This is done by iterating through the count list and adding the
   corresponding value to the output list that many times.
   - example: 
        - input list = [2, 5, 2, 8, 5, 6, 8, 8]
        - count list = [0, 0, 2, 0, 0, 2, 1, 0, 3]
        - output list = [2, 2, 5, 5, 6, 8, 8, 8]
"""

def countingSort(arr: list) -> list:
    """ Counting sort implementation """
    if len(arr) == 0:
        return "List is empty"
    if len(arr) < 2:
        return arr
    
    # Find the maximum element in the input list
    max_element = max(arr)

    # Create a count list to store the count of each unique element
    count_list = [0] * (max_element + 1)

    # For each number in the input list, increment the corresponding index
    # in the count list
    for num in arr:
        count_list[num] += 1

    # Create a sorted output list
    index = 0
    for i, count in enumerate(count_list):
        while count > 0:
            arr[index] = i
            index += 1
            count -= 1
    
    return arr

# test case
test_list = []
for _ in range(0):
    test_list.append(random.randint(0, 100))
print(f"Original list: {test_list}")

sorted = countingSort(test_list)
print(f"Sorted list: {sorted}")
