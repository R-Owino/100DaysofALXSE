<details>
  <summary><strong>Recap 🔄</strong></summary>
  
  - Data structures provide a specific way to orgainize and store data so that it can be accessed and used efficiently.
  - The different types of data structures include:
    - Arrays
    - Linked lists
    - Stacks
    - Hash tables
    - Trees
    - Graphs
  - Each of these data structures has its unique characteristics and usecases, and is optimal for certain kinds of operations.
  - Correctly choosing a data structure can significantly enhance the performance of a program.
</details>


<p>In Day 1, I went over what data structures are and why they are needed. Today, I will go over the first basic data structure, arrays</p>

### 1. Arrays

<p>An array is a linear data structure akin to a list i.e it can hold elements of the multiple types. This is unlike in other languages like Java and C++ where an array can hold only elements of the same type.</p>

<p>These arrays in Python are dynamic, again unlike in Java or C++ where the arrays are both static and dynamic.</p>

<p>Dynamic arrays allow us to add elements as the list grows. An initial capacity in the memory is allocated to accomodate the dynamic nature of these arrays</p>

<p>Arrays use contigous memory space to store elements. An item can be accessed directly based on its index making arrays an efficient data structure</p>

<p>Arrays have 2 types:</p>

- One diemnsional array has the data stored in a linear form

```
# Type 1: One-dimentional arrays
arr1 = [1, 2, 3, "hello", "foo", "bar"]
```

- Multi-dimesional array has the data stored in a matrix form or in a 3-D format

```
# Type 2: Multi-dimensional arrays
arr2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
```

<p>To practice arrays, I have a file <i>arrays.py</i> that constitutes exercise from the first link in the References section below. The following snippet shows the output of <i>arrays.py</i></p>

```
$ ./arrays.py 
###################### Example 1 ######################
Feb compared to Jan: 150
Total expenses in the first quater: 7150
No month had an expense of exactly 2000
Expense after adding June: [2200, 2350, 2600, 2130, 2190, 1980]
Expense after refund: [2200, 2350, 2600, 1930, 2190, 1980]
###################### Example 2 ######################
Length of list: 5
List after adding 'black panther': ['spider man', 'thor', 'hulk', 'iron man', 'captain america', 'black panther']
List after removing 'black panther' and adding it after 'hulk': ['spider man', 'thor', 'hulk', 'black panther', 'iron man', 'captain america']
List after removing 'hulk' and 'thor' and adding 'doctor strange': ['spider man', 'doctor strange', 'black panther', 'iron man', 'captain america']
List after sorting in aplhabetical order: ['black panther', 'captain america', 'doctor strange', 'iron man', 'spider man']
###################### Example 3 ######################
Enter max number: 10
Odd numbers between 1 and 10: [1, 3, 5, 7, 9]
```



#### References
1. [DSA - Arrays](https://www.youtube.com/watch?v=gDqQf4Ekr2A)
2. [Arrays](https://www.w3schools.com/dsa/dsa_data_arrays.php)
