#!/usr/bin/python3
""" Radix sort algorithm """

import random

"""
Steps:
Assume the input array is [170, 45, 75, 90, 802, 24, 2, 66]:
1. Find the maximum number in the input array and iterate the number of times
   given the number of digits in the maximum number.
   In this case, max number = 802, so we will iterate 3 times
2. Use counting sort the elements based on the units place digits
   - Sorted array based on units place: [170, 90, 802, 2, 24, 45, 75, 66]
3. Use counting sort the elements based on the tens place digits
   - Sorted array based on tens place: [802, 2, 24, 45, 66, 170, 75, 90]
4. Use counting sort the elements based on the hundreds place digits
   - Sorted array based on hundreds place: [2, 24, 45, 66, 75, 90, 170, 802]
5. The array is now sorted in ascending order
"""

def countingSort(arr: list, exp: int) -> list:
    """ Counting sort implementation for radix sort """
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # sort elements based on the units place
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # sort elements based on the tens place
    for i in range(1, 10):
        count[i] += count[i - 1]

    # sort elements based on the hundreds place
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]

    return arr

def radix_sort(arr: list) -> list:
    """ Radix sort implementation """
    if len(arr) == 0:
        return "List is empty"
    if len(arr) < 2:
        return arr
    
    # Find the maximum element in the input list
    max_element = max(arr)
    exp = 1
    while max_element // exp > 0:
        countingSort(arr, exp)
        exp *= 10
    
    return arr

# test case
test_list = []
for _ in range(10):
    test_list.append(random.randint(0, 300))
print(f"Original list: {test_list}")

sorted = radix_sort(test_list)
print(f"Sorted list: {sorted}")
