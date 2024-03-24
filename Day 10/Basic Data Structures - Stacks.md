<p>Over the past few days I have comprehensively covered linked lists data structures. Today, I will look into stacks 📚</p>

## 3. Stacks
<p>In Day 4 I went over arrays and linked lists over the past few days. One of the main benefits of arrays and linked lists are their ability to be used to define other data structures.</p>

<p>Stacks are linear data structures that follow a Last In First Out (LIFO) or First In Last Out (FILO) principle and allows insertion and deletion operations from the top. Implementation of the stack can be done by contiguous memory which is an array, and non-contiguous memory which is a linked list. Examples of stacks include a pile of books, a stack of plates, a deck of cards etc</p>

<figure>
    <img src="../assets/stack-of-book.avif" alt="stack" style="width:100%; height:50%">
    <figcaption align="center">Stack of books</figcaption>
</figure>

<p>The following terms are regularly used with stacks. These also double up as the operations done on a stack.</p>
<ol>
    <li>Top - the last element to be inserted to the stack</li>
    <li>Push - inserting a new elemnet in the stack</li>
    <li>Pop - removing or deleting elements from the stack</li>
    <li>Peek - retrieve the topmost element without removing it from the collection</li>
</ol>

<p>The implementation for these will be don in the subsequent <i>.py</i> files.</p>

### Implementation of stacks
1. Implement as an array
<p>Stacks can be formed using arrays and all the operations are performed using arrays. Of course, the arrays are dynamic. We'll see an example of this.</p>

<figure>
    <img src="../assets/array-implemnetation-of-stack.avif" alt="stack-implementation" style="width:100%">
    <figcaption align="center">Array implementation of stacks</figcaption>
</figure>

2. Implement as a linked list
<p>When implementing a stack as an array, every new element is inserted as the top element (insert from beginning) and removing an element happens from the top (remove from beginning)</p>

<figure>
    <img src="../assets/stack-implemntation-using-linked-list.avif" alt="stack-implementation" style="width:100%">
    <figcaption align="center">Implementing stacks using linked lists</figcaption>
</figure>

3. Implement as a collection
<p>Lists are great for stack implementation. Problem is, they're dynamic, so every time a new element has to be added and there's no more space, the whole list is copied over to a new memory location and the new memory space doubles in size. This is costly.</p>

<p>This is where collection.deque class comes to the rescue. We don't have to worry about the dynamic nature of arrays since new locations are allocated as needed. This we got to see practically.</p>

### Applications of stack data structures
1. Function call
<p>When a function is called from another function, the function references are stored in a stack in the order in which the functions are called. When the function call is terminated, the program control moves back to the function call using the references stored in the stack.</p>

2. Memory management
<p>Stacks are essential in helping operating systems manage memory. References to operations are stored in stacks so whenever they're needed the OS can reference to the stack.</p>

3. Backtracking
<p>Backtracking is a recursive algorithm mechanism that is used to solve optimization problems. To solve the optimization problem with backtracking, there're multiple solutions; it does not matter if it is correct. While finding all the possible solutions in backtracking, the previously calculated problems are stored in a stack and that solution is used to resolve the following issues.</p>

#### References
1. [Implementing Stacks in Data Structures](https://www.simplilearn.com/tutorials/data-structure-tutorial/stacks-in-data-structures)
2. [DSA - Stacks](https://www.youtube.com/watch?v=zwb3GmNAtFk)
3. [Collections - deque objects](https://docs.python.org/3/library/collections.html#deque-objects)
