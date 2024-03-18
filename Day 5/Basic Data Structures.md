<p>This is a continuation of the basic data structures. Yesterday, I covered arrays. Today I will look into linked lists.</p>

## 2. Linked Lists

<p>Linked lists are a linear data structure, like arrays, in which elements are not stored in contigous memory location, unlike arrays. They form a series of connected nodes, where each node contains a data field and the address(reference) of the next node</p>

<figure>
    <img src="../assets/Singlelinkedlist.png" alt="linked_list" style="width:100%">
    <figcaption align="center">linked list</figcaption>
</figure>

<p>The following terms are regularly used with linked lists:</p>
<ol>
    <li>Node - holds the data field and the pointer to the next node</li>
    <li>Data - holds the actual value associated with a node</li>
    <li>Next Pointer - stores the memory address of the next node in the sequence</li>
    <li>Head - first node in the list, this is where the linked list is accessed through</li>
    <li>Tail - last node in the list which points to a null</li>
</ol>

### Types of linked lists

<p>There are 3 major types of linked lists:</p>
<ol>
    <li>
        <p>Singly linked list</p>
        <p>This is the simplest type in which every node contains some data and a pointer to the next node of the same data type. Traversal is only one way, forward direction.</p>
        <figure>
                    <img src="../assets/Singlelinkedlist.png" alt="singly linked list" style="width:100%">
                    <figcaption align="center">Singly linked list</figcaption>
        </figure>
    </li>
    <li>
        <p>Doubly linked list</p>
        <p>This is like a singly linked list, but instead of having a pointer to the next node only, it has an additional pointer to the previous node as well. Traversal can be in both forward and backward directions.</p>
        <figure>
                    <img src="../assets/doublylinkedlist.png" alt="Image description" style="width:100%">
                    <figcaption align="center">Doubly linked list</figcaption>
        </figure>
    </li>
    <li>
        <p>Circular linked list</p>
        <p>This is a list in which the last node contains the pointer to the first node of the list. It has no beginning or end because it allows traversal in any direction until we get to the same node we started from.</p>
        <figure>
                    <img src="../assets/circularlinkedlist.png" alt="Image description" style="width:100%">
                    <figcaption align="center">Circular linked list</figcaption>
        </figure>
    </li>
</ol>

### Linked lists vs Arrays
