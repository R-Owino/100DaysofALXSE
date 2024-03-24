<p>Yesterday, and parts of today, I covered stack data structures and saw the different ways stacks can be implemented using othe data structures I covered before. Today, I deepdive into queues 🚶🚶🚶🚶🚶</p>

## 4. Queues
<p>Like stacks, queues are a linear data structure in which elements are held in a sequence and access is restricted to one end. Elements are added (“enqueued”) at the rear end and removed (“dequeued”) from the front. This makes queues a First-In, First-Out (FIFO) data structure. Good examples include people standing in a line at the supermarket or waiting to be served by a teller at a bank. The first person in the line will be the one to pay or be served first and leave.</p>

<figure>
    <img src="../assets/queue.png" alt="queue" style="width:100%; height:50%">
    <figcaption align="center">Teller Line</figcaption>
</figure>

<p>The following terms are regularly used with stacks. These also double up as the operations done on a stack.</p>
<ol>
    <li>Enqueue - add a new element to the queue</li>
    <li>Dequeue - remove and return the first element from the queue</li>
    <li>Peek - retrieve the topmost element without removing it from the queue</li>
</ol>

<figure>
    <img src="../assets/queue_ops.png" alt="queue_ops" style="width:100%; height:50%">
    <figcaption align="center">Queue operations</figcaption>
</figure>


<p>The implementation for these will be done in the subsequent <i>.py</i> files.</p>

### Implementation of queues
1. Implement as an array
<p>Once again, arrays come in handy when implementing another data structure. The figure below shows how it looks like when a queue is implemented using an array.</p>

<figure>
    <img src="../assets/queue_array.png" alt="queue-implementation" style="width:100%">
    <figcaption align="center">Array implementation of queues</figcaption>
</figure>

<p>One of the biggest con of using arrays to implement queues is the shifting costs. Dequeue removes the first element and the other elements must be shifted to take up the free spaces before them. If the queue is long this can be extremely inefficient. </p>

2. Implement as an linked list
<p>Linked lists solve the problems of arrays. Since they're dynamic, queues can grow and shrink as needed, and the crown: no shifting is required - the other elements don't have to be shifted in memory after a dequeue operation. But then this comes at a cost of extra memory since each element has to contain the address of the next/previous elements.</p>

<figure>
    <img src="../assets/queue_linkedlist.png" alt="queue-implementation" style="width:100%">
    <figcaption align="center">Implementing queues using linked lists </figcaption>
</figure>

3. Implement as a collection
<p>Just like in stacks, we can use the deque collection to implement  a queue. The difference comes in the methods used, we'll see this in an example.</p>

### Applications of queues
1. Message sending
<p>Queues are used in messaging apps to maintain the heirarchy of text messages irrespective of whether a user is online or offline. When a user comes online, the messages in the queue gets delivered and the queue emptied</p>

2. Process scheduling in operating systems
<p>Queues are used to implement round robin scheduling algorithms in computer systems</p>

3. Switching and routing
<p>Both switches and routers maintain inbound and outbound queues to store packets</p>

4. Customer service systems
<p>Call center phone systems are developed using queue data structures. The first customer to call will be the first one to be served.</p>

#### References
1. [DSA - Queues](https://www.w3schools.com/dsa/dsa_data_queues.php)
2. [Implementing queue data structures](https://www.youtube.com/watch?v=rUUrmGKYwHw)
3. [A comprehensive look at queue in data strcture](https://www.simplilearn.com/tutorials/data-structure-tutorial/queue-in-data-structure)
