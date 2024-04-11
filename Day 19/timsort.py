#!/usr/bin/python3
""" Timsort algorithm """

import random

"""
Steps:
1. Divide the array into runs
2. Sort each run using an insertion sort
3. Merge the sorted runs
4. Adjust the run size - double it until it exceed the array size
5. Repeat the merging until the array is sorted
"""

MIN_MERGE = 32

def calc_min_run(n):
    """Calculate the minimum length of a run from an array of size n."""
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    min_run = n + r
    return max(min_run, 1)

def insertion_sort(arr, left, right):
    """Sort small pieces of the array using insertion sort."""
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

def merge(arr, l, m, r):
    """Merge two sorted segments of the array."""
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(len1):
        left.append(arr[l + i])
    for i in range(len2):
        right.append(arr[m + 1 + i])

    i = j = 0
    k = l
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = right[j]
        j += 1
        k += 1

def timsort(arr):
    """Perform the Timsort algorithm on the array."""
    if len(arr) < 2:
        return arr
    
    n = len(arr)
    min_run = calc_min_run(n)

    # Sort individual subarrays of size MIN_MERGE
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)

    # Start merging from size MIN_MERGE. It will double after every iteration.
    size = min_run
    while size < n:
        # Determine the arrays to be merged
        for left in range(0, n, size * 2):
            mid = min(n - 1, left + size - 1)
            right = min((left + size * 2 - 1), (n - 1))

            # Merge the subarrays
            if mid < right:
                merge(arr, left, mid, right)

        # Double the size for next iteration
        size *= 2
    return arr

# test case
test_list = []
for _ in range(1):
    test_list.append(random.randint(0, 100))
print(f"Original list: {test_list}")

sorted = timsort(test_list)
print(f"Sorted list: {sorted}")
