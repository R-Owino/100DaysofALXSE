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
    """Returns a list containing the Fibonacci sequence up to n"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# Call the function
usage = int(input("Enter a number to get it's fibonacci sequence: "))
print(fib(usage))

# Example 2
def arrayChallenge(arr):
    """
     - for each element in the array, the counter is set to 0
     - the element is compared to each element on its left
     - if the element on the left is greater, the absolute difference is subtarcted from the counter
     - if the element on the left is less, the absolute difference is added to the counter
     - for each element in the array, determine the value of the counter
     - the values should be stored in an array and returned
    """
    n = len(arr)
    result = []
    
    for i in range(n):
        counter = 0
        for j in range(i):
            if arr[j] > arr[i]:
                counter -= abs(arr[j] - arr[i])
            else:
                counter += abs(arr[j] - arr[i])
        result.append(counter)
    
    return result

# Call the function
n = 3
arr = [1, 2, 3]
print(arrayChallenge(arr))
