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
    expense[3] += 200
    print(f"Expense after refund: {expense}")

expense_tracker()

print("###################### Example 2 ######################")