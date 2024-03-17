#!/usr/bin/python3
"""Arrays data structure"""

# one dimensional array
arr1 = [1, 2, 3, "hello", "foo", "bar"]

# multi-dimensional array
arr2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

print("###################### Example 1 ######################")
"""
- These are the expenses for Ali for every month:
 - January: 2200
 - February: 2350
 - March: 2600
 - April: 2130
 - May: 2190
- Create a list to store the expenses and find out the following:
 - How much more was spent in Feb compared to Jan
 - Total expenses in the first quater
 - Which month was the expense exactly 2000
 - Add monthly expense for June, the amount is 1980
 - Ali returned an item that he bought in April and a got a refund of 200.
   Make the necessary adjustment in the list to reflect this
"""

def expense_tracker():
    # create the list of expenses
    expense = [2200, 2350, 2600, 2130, 2190]

    # How much more was spent in Feb compared to Jan
    diff = expense[1] - expense[0]
    print(f"Feb compared to Jan: {diff}")

    # Total expenses in the first quater
    q1_total = sum(expense[:3])
    print(f"Total expenses in the first quater: {q1_total}")

    # Which month was the expense exactly 2000
    if 2000 in expense:
        month = expense.index(2000) + 1
        print(f"Month the expense was exactly 2000: {month}")
    else:
        print("No month had an expense of exactly 2000")
    
    # Add monthly expense for June, the amount is 1980
    expense.append(1980)
    print(f"Expense after adding June: {expense}")

    # Ali returned an item that he bought in April and a got a refund of 200.
    expense[3] -= 200
    print(f"Expense after refund: {expense}")

expense_tracker()

print("###################### Example 2 ######################")
"""
Given this list of marvel characters, find out:
    characters = ['spider man','thor','hulk','iron man','captain america']
- The length of the list
- Add "black panther" at the end of this list
- Remove "black panther" from the list and add it after "hulk"
- Using one line of code, remove "hulk" and "thor" and replace them with "doctor strange"
- Sort the list in aplhabetical order
"""

def marvel():
    characters = ['spider man','thor','hulk','iron man','captain america']
    print(f"Length of list: {len(characters)}")

    # Add "black panther" at the end of this list
    characters.append("black panther")
    print(f"List after adding 'black panther': {characters}")

    # Remove "black panther" from the list and add it after "hulk"
    characters.remove("black panther")
    characters.insert(3, "black panther")
    print(f"List after removing 'black panther' and adding it after 'hulk': {characters}")

    # Using one line of code, remove "hulk" and "thor" and replace them with "doctor strange"
    characters[1:3] = ["doctor strange"]
    print(f"List after removing 'hulk' and 'thor' and adding 'doctor strange': {characters}")

    # Sort the list in aplhabetical order
    characters.sort()
    print(f"List after sorting in aplhabetical order: {characters}")

marvel()

print("###################### Example 3 ######################")
"""
Create a list of odd numbers between 1 and a max number
Take max_number as input from the user
"""

def odd_numbers():
    max_number = int(input("Enter max number: "))
    odd = [x for x in range(1, max_number + 1) if x % 2 == 1]
    print(f"Odd numbers between 1 and {max_number}: {odd}")

odd_numbers()
