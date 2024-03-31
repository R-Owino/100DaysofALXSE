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

