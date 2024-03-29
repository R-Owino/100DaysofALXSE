#!/usr/bin/python3
"""
Hash maps data structure
"""

"""
Handling collisions in hash maps using linear probing:
  - Linear probing looks for the next available slot in the array when a
  collision occurs
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
    
    def get_hash(self, key):
        """ Get the hash key for the given key """
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.size
    
    def set_val(self, key, val):
        """ Insert a key-value pair into the hash map """
        hash_key = self.get_hash(key)
        if self.hash_table[hash_key]:
            for index, element in enumerate(self.hash_table[hash_key]):
                if element[0] == key:
                    self.hash_table[hash_key][index] = (key, val)
                    return
                # linear probing
                for new_key in range(hash_key+1, self.size):
                    if not self.hash_table[new_key]:
                        self.hash_table[new_key] = [(key, val)]
                        return
                for new_key in range(0, hash_key):
                    if not self.hash_table[new_key]:
                        self.hash_table[new_key] = [(key, val)]
                        return
        self.hash_table[hash_key] = [(key, val)]

    def get_val(self, key):
        """ Returns the value to which the specified key is mapped """
        hash_key = self.get_hash(key)
        if self.hash_table[hash_key]:
            for index, element in enumerate(self.hash_table[hash_key]):
                if element[0] == key:
                    return element[1]
        return "No record found"

    def delete_val(self, key):
        """ Removes the mapping for the specific key if the hash map contains the mapping for the key """
        hash_key = self.get_hash(key)
        if self.hash_table[hash_key]:
            for index, element in enumerate(self.hash_table[hash_key]):
                if element[0] == key:
                    self.hash_table[hash_key].pop(index)
                    return
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
