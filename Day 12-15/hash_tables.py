#!/usr/bin/python3
"""
Hash maps data structure
"""

"""
Implementation of hash maps:
  - Insertion: The key-value pair is hashed, and the resulting index is used to store the value in the corresponding slot.
    If a collision occurs, the collision resolution strategy is applied.
  - Deletion: The key is hashed to find the index, and the item at that index is removed.
    Collision resolution may be necessary.
  - Lookup: The key is hashed to find the index, and the value at that index is returned.
    Collision resolution may be applied if needed.

To implement the hash map, these methods will be used:

  - set_val(key, value): Inserts a key-value pair into the hash map.
                         If the value already exists in the hash map, update the value.
  - get_val(key): Returns the value to which the specified key is mapped,
                  or “No record found” if this map contains no mapping for the key.
  - delete_val(key): Removes the mapping for the specific key if the hash map contains the mapping for the key.

"""

class HashTable:
    """ Hash map implementation """
    def __init__(self, size):
        """ Initialize the hash map object """
        self.size = size
        self.hash_table = self.create_bucket()

    def create_bucket(self):
        """ Holders for information in the hash map """
        return [[] for _ in range(self.size)]
    
    def set_val(self, key, val):
        """ Insert a key-value pair into the hash map """
    
        # get index from key using hash function
        hash_key = hash(key) % self.size

        # get bucket for the key
        bucket = self.hash_table[hash_key]

        key_found = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if key is already in the bucket
            if record_key == key:
                key_found = True
                break

        # if key is present, update the value
        # else append new key-pair to the bucket
        if key_found:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))


    def get_val(self, key):
        """ Returns the value to which the specified key is mapped """

        # get index from key using hash function
        hash_key = hash(key) % self.size

        # get bucket for the key
        bucket = self.hash_table[hash_key]

        key_found = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if key is already in the bucket
            if record_key == key:
                key_found = True
                break

        # if key is present, return the value
        # else return “No record found”
        if key_found:
            return record_val
        return "No record found"
    
    def delete_val(self, key):
        """ Removes the mapping for the specific key if the hash map contains the mapping for the key """

        # get index from key using hash function
        hash_key = hash(key) % self.size

        # get bucket for the key
        bucket = self.hash_table[hash_key]

        key_found = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if key is already in the bucket
            if record_key == key:
                key_found = True
                break

        # if key is present, remove the key-pair from the bucket
        if key_found:
            bucket.pop(index)
        return "No record found"
    
    def __str__(self):
        """ String representation of the hash map """
        return "".join(str(record) for record in self.hash_table)

hash_map = HashTable(5)

# set/insert values
hash_map.set_val("apple", "red")
hash_map.set_val("banana", "yellow")
hash_map.set_val("orange", "orange")
print(hash_map)
print("-"*20)

# get values
print(hash_map.get_val("apple"))
print(hash_map.get_val("banana"))
print("-"*20)

# delete values
print(hash_map.delete_val("apple"))
