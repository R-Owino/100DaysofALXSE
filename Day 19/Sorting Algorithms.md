## Sorting Algorithms

### What is a sorting algorithms?
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

- Space Complexity: O(n)
- Time Complexity: O(n²)
- Sorting in Place: Yes
- Stable: No
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
<p>
Merge sort algorithm is a divide and conquer algorithm that takes the advantage of the ease of merging already sorted lists into a new sorted lists. It works by dividing the input array into two halves, calls itself for the two halves then merges the two sorted halves.

Of the algorithms discussed so far, this is the first that works efficiently with large lists because it's worst case running time is O(n log n). The downside is it requires an additional O(n) space complexity compared to bubble, selection and insertion sorts and involves large number of copies in simple implementations.

Properties of merge sort:

- Space Complexity: O(n)
- Time Complexity: O(n log n)
- Sorting In Place: No in a typical implementation
- Stable: Yes
- Parallelizable :yes
</p>

5. Quicksort
<p>
Quicksort is an in-place divide and conquer algorithm that uses a partition technique to sort elements. The partition operation uses a randomly chosen pivot element. Smaller elements are moved to the left of the pivot elememt and larger elements are moved to the right. The sublists are then sorted recursively resulting in an avarage time of O(n log n) with a low overhead making it a popular algorithm.

The only caveat with quicksort is that its worst case performance is O(n²). This is rare, but in naive implementations, where the smallest or largest elemenets are chosen as the pivot, this occurs for sorted data.

The issue in quicksort is choosing a good pivot element as consistently poor choices of pivots can result in drastically slower O(n²) performance, but good choice of pivots yields O(n log n) performance, which is asymptotically optimal.

Properties of quicksort:

- Space complxity: O(n)
- Best case time complexity: O(n log n)
- Worst case time complexity: O(n²)
- Stable: No
</p>

6. Heapsort
<p>
Heapsort is a much more efficient version of selection sort. It is a comparison based algorithm that works by utilizing a data structure called  called a heap, a special type of binary tree. Using the heap, it works by dividing its input into a sorted and an unsorted region, and iteratively shrinking the unsorted region by extracting the largest element and moving that to the sorted region.

It involves building a Max-Heap, which is a specialized tree-based data structure, and then swapping the root node (maximum element) with the last node, reducing the size of heap by one and heapifying the root node. The maximum element is now at the end of the list and this step is repeated until all nodes are sorted.

Using the heap, finding the next largest element takes O(log n) time, instead of O(n) for a linear scan as in simple selection sort. This allows heapsort to run in O(n log n) time, and this is also the worst case complexity.

Properties of heapsort:

- Space complexity: O(n)
- Best case time complexity: O(n log n)
- Worst case time complexity: O(n log n)
- Stable: No
- Sorting inplace: Yes
</p>

7. Counting sort
<p>
Counting sort is a sorting technique based on keys between a specific range. It works by first creating a list of the count of occurences of each unique value in the list. Then it creates a final sorted list based on the list of counts. 

It is applicable when each input is known to belong to a particular set, S, of possibilities. The algorithm runs in O(|k| + n) time and O(|k|) memory where n is the length of the input.  This sorting algorithm often cannot be used because k needs to be reasonably small for the algorithm to be efficient, but it is extremely fast and demonstrates great asymptotic behavior as n increases.

Properties of counting sort:
- Space complexity: O(k)
- Best case performance: O(n+k)
- Average case performance: O(n+k)
- Worst case performance: O(n+k)
- Stable: Yes (k is the range of the elements in the array)
</p>

8. Radix sort
<p>
Yesterday, I looked into counting sort (above), it's a prerequisite for radix sort. While quicksort, merge sort and heapsort are comparison-based, countsort is not. It has a complexity of O(n+k). So, if k is O(n), CountSort becomes linear sorting, which is better than comparison based sorting algorithms that have O(nlogn) time complexity. The idea is to extend the countsort algorithm to get a better time complexity when k goes O(n2). Thus, Radix Sort.

The key idea behind Radix Sort is to exploit the concept of place value. It assumes that sorting numbers digit by digit will eventually result in a fully sorted list. Radix Sort can be performed using different variations, such as Least Significant Digit (LSD) Radix Sort or Most Significant Digit (MSD) Radix Sort.

<p>How the radix sort algorithm works?</p>

For each digit i where i varies from the least significant digit to the most significant digit of a number (ones, tens, hundreds ...), sort input array using countsort algorithm according to i<i>th</i> digit. We used count sort because it is a stable sort.

Properties of radix sort:
- Space complexity: O(n)
- Worst case performance: O(nk) where k is the number of digits
- Average case performance: O(nk)
- Best case performance: Ω(n+k)
- Stable: yes - both Least Significant Digit and Most Significant Digit radix sort

</p>

9. Bucket sort
<p>
Bucket sort is a divide-and-conquer sorting algorithm that generalizes counting sort by partitioning an array into a finite number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sorting algorithm.

A bucket sort works best when the elements of the data set are evenly distributed across all buckets. For example, when the input array is a large array of floating point integers distributed uniformly between an upper and lower bound.

Other sorting algorithms like merge sort, heap sort, or quick sort could be used. However, those algorithms guarantee a best case time complexity of O(nlogn). Using bucket sort, sorting the same array can be completed in O(n) time.

</p>

10. Timsort
<p>
Timsort algorithm is a hybrid, stable sorting algorithm, derived from merge sort and insertion sort that finds subsequences of the data that are already ordered (runs) and uses them to sort the remainder more efficiently. This is done by merging runs until certain criteria are fulfilled.

It works by taking advantage of runs of consecutive ordered elements that already exist in most real-world data, natural runs. It iterates over the data collecting elements into runs and simultaneously putting those runs in a stack. Whenever the runs on the top of the stack match a merge criterion, they are merged. This goes on until all data is traversed; then, all runs are merged two at a time and only one sorted run remains.

The main advantage of merging ordered runs instead of merging fixed size sub-lists (as done by traditional mergesort) is that it decreases the total number of comparisons needed to sort the entire list.

Properties of timsort:
- Space Complexity: O(n)
- Best case complexity: O(n)
- Average case complexity: O(nlogn)
- Worst case complexity: O(nlogn)
- Stable: Yes
- Inplace sorting: no, it requires extra space
</p>

#### References

1. [Sorting algorithm](https://en.wikipedia.org/wiki/Sorting_algorithm)
2. [Sorting Algorithms Explained with Examples in JavaScript, Python, Java, and C++](https://www.freecodecamp.org/news/sorting-algorithms-explained-with-examples-in-python-java-and-c/)
3. [Sorting Algorithm Animations](https://www.toptal.com/developers/sorting-algorithms)
4. [Selection Sort with Gypsy folk dance](https://www.youtube.com/watch?v=Ns4TPTC8whw)
5. [Bubble sort with Hungarian folk dance](https://www.youtube.com/watch?v=Iv3vgjM8Pv4)
6. [Insertion sort with Romanian folk dance](https://www.youtube.com/watch?v=EdIKIf9mHk0)
7. [Merge sort with Transylvanian saxon](https://www.youtube.com/watch?v=dENca26N6V4&list=PLOmdoKois7_FK-ySGwHBkltzB11snW7KQ&index=3)
8. [Quick sort with Hungarian folk dance](https://www.youtube.com/watch?v=3San3uKKHgg)
9. [Median of medians algorithm to get the pivot value in quicksort](https://www.linkedin.com/advice/0/what-advantages-disadvantages-median-of-medians-algorithm)
10. [Heap Sort in a Nutshell](https://www.youtube.com/watch?v=MtQL_ll5KhQ)
11. [Investigating Heap Sort - Why Is Heap Sort Θ(nlogn)?](https://www.youtube.com/watch?v=k72DtCnY4MU)
12. [Counting sort](https://www.youtube.com/watch?v=7zuGmKfUt7s)
13. [Radix Sort](https://www.geeksforgeeks.org/radix-sort/)
14. [Radix sort - visual](https://www.youtube.com/watch?v=GUHGMtNo6RQ)
15. [Bucket sort](https://www.youtube.com/watch?v=VuXbEb5ywrU)
16. [TimSort](https://www.youtube.com/watch?v=_dlzWEJoU7I)
17. [Timsort algorithm](https://en.wikipedia.org/wiki/Timsort)
18. [TimSort Algorithm](https://www.awesomealgorithms.com/home/tim-sort)
19. [TimSort implementation in Python](https://www.pythonpool.com/python-timsort/)
