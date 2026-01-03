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
    *   **Logic**:
        *   Calculate the hash index using `hash_function`.
        *   Access the bucket (list) at that index.
        *   Iterate through the bucket to check if the `key` already exists.
        *   If the key exists, update its `value`.
        *   If the key does not exist, append the `(key, value)` tuple/list to the bucket.
    *   **Parameters**: `key`, `value`.
    *   **Returns**: None.

4.  **`get(self, key)`**
    *   Retrieves the value associated with the key.
    *   **Logic**:
        *   Calculate the hash index.
        *   Search the bucket at that index for the `key`.
        *   Return the corresponding `value` if found.
    *   **Parameters**: `key`.
    *   **Returns**: The value if found, otherwise `None`.

5.  **`remove(self, key)`**
    *   Removes the key-value pair from the hash table.
    *   **Logic**:
        *   Calculate the hash index.
        *   Search the bucket for the `key`.
        *   If found, remove the pair from the list and return `True`.
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

