<p>This is the last of basic data structures. Over the next few days, I will be learning more about hash tables, also called hash maps</p>

## 5. Hash maps/tables
<p>Hash tables are specialized data structures that allow fast access to data based on a key - data is stored in an associative manner. Essentially, a hash table works by taking a key input, and then computes an index into an array in which the desired value can be found. It uses a hash function to calculate this index. The process of mapping the keys to appropriate locations (or indices) in a hash table is called <i>hashing</i>.</p>

<p>Hash tables are particularly efficient when the maximum number of entries can be predicted in advance.</p>

<figure>
    <img src="../assets/hash-table.png" alt="hash table" style="width:100%; height:50%">
    <figcaption align="center">Hash table</figcaption>
</figure>

### How a hash map works

<figure>
    <img src="../assets/hashmap_work.png" alt="hash table" style="width:100%; height:50%">
    <figcaption align="center">How a hash map works</figcaption>
</figure>

<p>A hash map is a concrete implementation of an associative array. At the fundamental level, it maps keys to values. Here's how hash maps work:</p>

1. Key-pair storage - a hash map stores key-value pairs and associayes the supplied key with the value so later on the value can be retrieved using the key.

2. Hash function - a hash function is used to compute an index into an array of buckets or slots from a key. The hash function is an algorithm that produces an index of where a value can be found or stored in the hash table.

3. Bucket array - the hash map internally maintains an array, also known as a "bucket array". Each index position in the array is a bucket that can hold multiple Node objects using a LinkedList.

4. Handling collisions - a collision occurs when 2 different keys hash to the same bucket. There are solutions on how to handle these collisions, which will be handled in the collisions section.

5. Key retrieval - to retrieve a value, the hash map uses the key to compute the hash, which indicates the bucket. The bucket is then searched to find the matching key and return its corresponding value.

### Advantages of hashing
1. Speed - the access time of an element is on average 0(1) (complexities will be covered after this). This makes the lookup action very fast.

### Hash functions
<p>A Hash function is a mathematical function that converts a given numeric or alphanumeric key to a small practical integer value. The mapped integer value is used as an index in the hash table. In simple terms, a hash function maps a significant number or string to a small integer that can be used as the index in the hash table.</p>

### Collisions

#### References