# Programming Assignment 0: Hash Table Implementation

### Objective
The objective of this assignment is to understand the basics of a Hash Table data structure using Chaining for collision resolution. This assignment is smaller in scope compared to others.

### Requirements & Details of Implementation 

You are required to implement a Python class named `HashTable` in a file named `HashTable.py`.

#### Class Methods

1.  **`__init__(self, size=10)`**
    *   Initializes a new Hash Table.
    *   **Parameters**: `size` - The number of buckets (lists) in the table. Default is 10.
    *   Initialize `self.table` as a list of empty lists, with length equal to `size`.

2.  **`hash_function(self, key)`**
    *   Computes the hash index for a given key.
    *   **Parameters**: `key` - The key to hash (string or int).
    *   **Returns**: An integer index (0 to size-1).
    *   **Logic**: Use Python's built-in `hash(key)` modulo `size`.

3.  **`insert(self, key, value)`**
    *   Inserts a key-value pair into the hash table.
    *   If the key already exists, update its value.
    *   **Parameters**: `key`, `value`.
    *   **Returns**: None.

4.  **`get(self, key)`**
    *   Retrieves the value associated with the key.
    *   **Parameters**: `key`.
    *   **Returns**: The value if found, otherwise `None`.

5.  **`remove(self, key)`**
    *   Removes the key-value pair from the hash table.
    *   **Parameters**: `key`.
    *   **Returns**: `True` if removed, `False` if key not found.

### Example Usage

```python
ht = HashTable(size=5)
ht.insert("apple", 10)
ht.insert("banana", 20)
print(ht.get("apple"))   # 10
ht.insert("apple", 15)   # Update
print(ht.get("apple"))   # 15
print(ht.remove("banana")) # True
print(ht.get("banana"))    # None
```

