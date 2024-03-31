#!/usr/bin/python3
""" Time complexity demonstration using simple examples """


# Example 1 -  linear complexity
def square_numbers(nums):
    """
    Squares numbers by taking an input list
    """
    squared_nums = []
    for num in nums:
        squared_nums.append(num**2)
    return squared_nums

numbers = [1, 2, 3, 4, 5]
print(square_numbers(numbers))

# Example 2 -  constant complexity
def find_first_pe(prices, eps, index):
    """
    Getting the pe of the first stock in the list
    """
    pe = prices[index] / eps[index]
    return pe

prices = [100, 200, 300, 400, 500]
eps = [10, 20, 30, 40, 50]
index = 0
print(find_first_pe(prices, eps, index))

# Example 3 -  quadratic complexity
def find_duplicates(nums):
    """
    finds duplacates in a list of numbers
    """
    duplicates = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                duplicates.append(nums[i])
    return duplicates

numbers = [3, 4, 6, 4, 7, 9, 3]
res = find_duplicates(numbers)
print(f"{res} is a duplicate in the list")

# Example 4 -  exponential complexity
def fib(n):
    """
    Returns a list containing the Fibonacci sequence up to n
    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

n = 10
print(fib(n))

# Example 5 -  logarithmic complexity
def binary_search(nums, target):
    """
    Binary search algorithm
    """
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 8
print(binary_search(nums, target))
