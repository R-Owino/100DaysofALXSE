## Search Algorithms

### What are search algorithms?
<p>
In Computer Science, a search algorithm is a technique for finding a specific item or group of items among a collection of data. Basically, they are developed to solve search problems.
Search algorithms work to retrieve information stored within a particular data structure, or calculated in the search space of a problem domain, with either discrete or continuous values.
Search algorithms operate by checking each element in the dataset in order to locate the target selection. 
</p>

### Terminologies used with search algorthims
1. Target element
<p>
Specific element or group of elements that is being looked for within the data collection. The target could be a value, a record, a key or something else.
</p>

2. Search space
<p>
The entire collection of data where the target element is being looked for. It varies in size and organization depending on the data structure used.
</p>

3. Complexity
<p>
Measured in terms of time and space requirements, searching has different levels of complexity depending on the data structure and algorithm used.
</p>

3. Deterministic vs non-deterministic
<p>
Binary search algorthms are deterministic i.e they follow a clear systematic approach.
Linear search algorithms are non-deterministic i.e they need to examine the entire search space in the worst case.
</p>

### Types of search algorithms

1. Linear Search
<p>
Also called sequential search, it starts from one end and goes through the entire list until the target element is found, else it goes through to the end of the list.

It works on both sorted and unsorted lists, and does not need any preconditioned list for the operation. However, its efficiency is lesser as compared to other search algorithms since it checks all elements one by one.

Time complexity for linear search is O(n) on the worst and average cases and O(1) on the best case.
</p>

2. Sentinel Linear Search
<p>
Just like linear search, sentinel search is an algorithm for a list of items stored in a sequential manner.

<details>
  <summary><strong>Recap 🔄</strong></summary>

  - Linear search works by going through each item of the list in a linear fashion, comparing it to the target. This results to either finding the required item or not.

  - It does this by making two comparisons in every iteration
        - First iteration: check if the we're at the end of the list
        - Second iteration: check if current item matches the target or not
</details>

Linear search does comparisons twice. What if there was a way to make the search faster? This is where sentinel search comes in.

Sentinel search works by first inserting the target element at the end of the list, then comparisons are done with each item of the list until the required item is found. In this case, either the required item is in the list, in which case it will be found before we reach the end of the list. Or the list didn’t have the target, so the algorithm will reach the end of the list and find the target item that we have inserted.

This way, we only need to check if the item matches the target, not if the list is empty. This is because one way or another, we'll find the target and break out of the loop.

Lastly, we check if the item found was already there or manually added. This check will happen only once and the entire runtime of the algorithm will be cut down significantly because we have one less comparison to do in every iteration of the loop.

The time complexity of sentinel search is O(n) in the worst case and O(1) in the best case, when the key is found in the first iteration.
</p>

3. Binary Search

4. Depth-first search
<p>
Used more intricately in data structures like trees and graphs. It explores the depth of a branch before breadth.
</p>

5. Breadth-first search
<p>
Also used in tree and graph data structures. It explores all the neighboring nodes before proceeding to the nodes at the next level depth.
</p>

#### References
1. [Search algorithms](https://en.wikipedia.org/wiki/Search_algorithm)
2. [Search Algorithms – Linear Search and Binary Search Code Implementation and Complexity Analysis](https://www.freecodecamp.org/news/search-algorithms-linear-and-binary-search-explained/)
3. [Searching algorithms](https://www.geeksforgeeks.org/searching-algorithms/)
4. [Linear search](https://www.geeksforgeeks.org/linear-search/)
