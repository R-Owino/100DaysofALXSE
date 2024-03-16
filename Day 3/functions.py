#!/usr/bin/python3
"""
In this script, I will explore functions
"""

"""
 - A function is defined using the `def` keyword
 - After the first statement which also contains the function name,
   all other lines below must be idented
 - To use the function, the function name must be called
"""

# Example 1
def fib(n):
    """Print a Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# Call the function
usage1 = fib(2000)
usage1

