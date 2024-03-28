#!/usr/bin/python3
"""
Two sum problem:
  - Given an array of integers `nums` and an integer `target`,
  return indices of the two numbers such that they add up to `target`

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
"""

"""
Soln: 
This is a classic hash table problem. We can traverse the array and for
each element, we can calculate the difference between the target and the current
element and check if the difference exists in the hash table. If the difference
is in the table, we return the indices of the two elements. If the difference is
not in the table, we add the current element to the table.

Steps:
- Create an empty hash table on initialization to store the elements and their indices
- Traverse the array of nums
- Calculate the difference (target - current element) for each element
- Check if the difference is in the hash table
- If yes, return the current index and the index of the difference in the hash table
- If no, add the current element and its index to the hash table
- If no pair is found, return an empty list to imply no solution
"""

class TwoSum:
    """ Two sum problem """
    def twoSum(self, nums, target):
        """
        method to solve the two sum problem

        args:
            nums: list of integers
            target: integer
        """
        hash_table = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in hash_table:
                return [hash_table[diff], index]
            hash_table[num] = index
        return []

two_sum = TwoSum()
nums = [2, 7, 11, 5, 15, 30]
target = 12

result = two_sum.twoSum(nums, target)
print(f"Indices of the two numbers: {result}")
