## Sorting Algorithms
<p>
In computer science, a sorting algorithm is an algorithm that puts elements of a list into an order. The most frequently used orders are numerical order and lexicographical order, and either ascending or descending. Efficient sorting is important for optimizing the efficiency of other algorithms (such as search and merge algorithms) that require input data to be in sorted lists. Sorting is also often useful for canonicalizing data and for producing human-readable output.
</p>

### Sorting algorithms trade-offs
<p>
In order to choose the best sorting algorithm for a particular problem, ask the following question:

1. How big is the collection being sorted?
2. How much memory is needed?
3. Will the collection grow?

While choosing the algorithm, determine what the requirements are and consider the limitations of the system the algorithm will run on before deciding which sorting algorithm to use.
</p>

### Classifying sorting algorithms
<p>
Sorting algorithms can be classified by:

1. Computational complexity
<p>
This refers to the computatonal time and space taken by an algorithm to run as a function of the size of the input to the program. For example, bubble sort has a time complexity of O(n2) and  space complexity of O(1) while merge sort has a time complexity of O(nlog⁡n) and a space complexity of O(n).
</p>

2. Stability
<p>
A sorting algorithm is said to be stable if two objects with equal keys appear in the same order in sorted output as they appear in the input array to be sorted. Bubble Sort, Insertion Sort, and Merge Sort are examples of stable sorting algorithms.
</p>

3. Internal or external
<p>
Internal sorting is applied when the entire collection of data to be sorted is small enough that the sorting process can take place within main memory. An external sorting algorithm is used when the data being sorted do not fit into the main memory of a computing device and instead they must reside in the slower external memory (usually a hard drive).
</p>

4. Comparison-based or Non-comparison based
<p>
Comparison based algorithms compare elements of an array and decide their order while non-comparison based algorithms do not compare elements. Quick Sort is an example of a comparison-based sort, while Counting Sort is an example of a non-comparison based sort.
</p>

5. Recursive or non-recursive
<p>
Some sorting algorithms use recursion to sort lists, like Quick Sort and Merge Sort, while others, like Bubble Sort and Insertion Sort, are non-recursive.
</p>

6. Online or Offline
<p>
Online sorting algorithms can handle the case when all the data may not be available at the time of running the algorithm. Insertion sort is an example of an online algorithm. Offline algorithms require the entire list up front, like Quick Sort.
</p>

</p>

### Some common sorting algorithms
1. Selection sort
<p>
Selection sort works by dividing an array into 2 parts- sorted and unsorted. At first, all the elements are in the unsorted part and the sorted part is empty. The algorithm repeatedly goes through the elements, finds the smallest (or largest, depending on the sort order) one and moves it to the sorted part until all the elements are sorted.


This is not very effective on large arrays as the time complexity is O(n²) but really good when memory is a priority because it does no more than n swaps - no copies need to be made.


Properties of selection sort algorithm:
- Space Complexity:  O(n)
- Time Complexity:  O(n²)
- Sorting in Place:  Yes
- Stable:  No
</p>

2. Bubble sort
<p>
From its name, and picturing how the biggest bubbles "bubble" to the top, the largest element bubbles to the its intended location. The algorithm repeatedly swaps adjacent elements until the entire list is sorted in ascending order.


Like selection sort, it has a worst-case performance of O(n²) so it is rarely used to sort large unordered data sets.


Bubble sort can also be used efficiently on a list of any length that is nearly sorted (that is, the elements are not significantly out of place). 

For example, if any number of elements are out of place by only one position (e.g. 0123546789 and 1032547698), bubble sort's exchange will get them in order on the first pass, the second pass will find all elements in order, so the sort will take only 2n time.


Properties of bubble sort algorithm:
- Space complexity: O(1)
- Best case performance: O(n)
- Average case performance: O(n²)
- Worst case performance: O(n²)
- Stable: Yes
</p>

3. Insertion sort
<p>
From its name, insertion sort works by taking elements from the list one by one and inserting them in their correct position into a new sorted list, similar to how a player would sort playing cards in their hand. It is a simple algorithm that is much less efficient on large lists compared to more advanced algorithms.


It provides advantages such as being an easy to understand algorithm, performs well with small lists or lists that are partially sorted and can sort the list as it receives it.


The main disadvantage is it's expensive as it requires shifting the following elements over by one.


Properties of insertion sort:
- Space Complexity: O(1)
- Time Complexity: O(n), O(n²), O(n²) for Best, Average, Worst cases respectively.
- Best Case: array is already sorted
- Average Case: array is randomly sorted
- Worst Case: array is reversely sorted.
- Sorting In Place: Yes
- Stable: Yes
</p>

4. Merge sort
5. Quick sort
6. Heap sort
7. Counting sort
8. Radix sort
9. Bucket sort

#### References
1. [Sorting algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm)
2. [Sorting Algorithms Explained with Examples in JavaScript, Python, Java, and C++](https://www.freecodecamp.org/news/sorting-algorithms-explained-with-examples-in-python-java-and-c/)
3. [Sorting Algorithm Animations](https://www.toptal.com/developers/sorting-algorithms)
4. [Selection Sort with Gypsy folk dance](https://www.youtube.com/watch?v=Ns4TPTC8whw)
5. [Bubble sort with Hungarian folk dance](https://www.youtube.com/watch?v=Iv3vgjM8Pv4)
6. [Insertion sort with Romanian folk dance](https://www.youtube.com/watch?v=EdIKIf9mHk0)
