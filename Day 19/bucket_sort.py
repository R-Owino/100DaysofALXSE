#!/usr/bin/python3
""" Bucket Sort algorithm """

import random

"""
Steps:
1. Create n empty buckets
2. Put the elements in the correct buckets
3. Sort the elements in the individual buckets
4. Concatenate all buckets into an output array
"""

def bucketSort(arr: list) -> list:
    """ Bucket sort implementation """
    if len(arr) == 0:
        return "List is empty"
    if len(arr) < 2:
        return arr
    
    n = len(arr)

    # create n empty buckets
    buckets = [[] for _ in range(n)]

    # put the elements in the correct buckets
    for i in range(n):
        index = int(n * arr[i])
        buckets[index].append(arr[i])

    # sort the elements in the individual buckets
    for i in range(n):
        buckets[i] = sorted(buckets[i])

    # concatenate all buckets into an output array
    k = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1

    return arr

# test case
test_list = []
for _ in range(10):
    test_list.append(random.uniform(0, 1))
print(f"Original list: {test_list}")

sorted = bucketSort(test_list)
print(f"Sorted list: {sorted}")
