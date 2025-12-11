# Programming Assignment 1: Linked List Implementation

### Objective
The objective of this assignment is to understand the fundamental mechanics of a Singly Linked List by implementing one from scratch. Unlike Python lists (which are dynamic arrays), a Linked List consists of nodes where each node points to the next one. This structure allows for efficient insertions and deletions but requires O(n) time to access elements by index.

### Requirements & Details of Implementation

You are required to implement a Python class named `LinkedList` in a file named `LL.py`. This class will manage a sequence of `LLNode` objects.

### The `LLNode` Class
A helper class `LLNode` is provided to you in `LL.py`. You should not modify this class. It represents a single node in the linked list.

```python
class LLNode:
    def __init__(self, data):
        self.data = data  # The value stored in the node
        self.next = None  # Reference to the next node in the list
```
*   **`data`**: Holds the actual value of the element.
*   **`next`**: A pointer (reference) to the next node in the sequence. If it is `None`, that means this node is the last one in the list.

### Class Methods for `LinkedList`

In `LL.py`, you will find function signatures defined for you. You are expected to implement the logic for a Singly Linked List.

1.  **`__init__(self)`**
    *   Initializes a new empty linked list.
    *   Should maintain a `head` attribute pointing to the first node (initially `None`).

2.  **`append(self, data)`**
    *   Adds a new node containing `data` to the **end** of the list.
    *   **Parameters**: `data` - The item to be added.
    *   **Returns**: None.
    *   **Complexity**: O(n) (unless you maintain a tail pointer, but O(n) is acceptable for this basic implementation).

3.  **`prepend(self, data)`**
    *   Adds a new node containing `data` to the **beginning** of the list.
    *   **Parameters**: `data` - The item to be added.
    *   **Returns**: None.
    *   **Complexity**: O(1).

4.  **`delete(self, data)`**
    *   Removes the **first occurrence** of a node containing `data`.
    *   **Parameters**: `data` - The item to be removed.
    *   **Returns**: None.
    *   **Error Handling**: If the data is not found in the list, raise a `ValueError` with the message "Data not found".
    *   **Complexity**: O(n).

5.  **`find(self, data)`**
    *   Searches for a node containing `data`.
    *   **Parameters**: `data` - The item to search for.
    *   **Returns**: `True` if found, `False` otherwise.
    *   **Complexity**: O(n).

6.  **`is_empty(self)`**
    *   Checks if the list is empty.
    *   **Returns**: `True` if the list is empty, `False` otherwise.
    *   **Complexity**: O(1).

7.  **`size(self)`**
    *   Returns the number of nodes in the list.
    *   **Returns**: An integer representing the size.
    *   **Complexity**: O(n) (traversing to count) or O(1) (if you maintain a size counter).

8.  **`print_list(self)`**
    *   Returns a string representation of the list in the format: `val1 -> val2 -> val3 -> None`.
    *   **Returns**: A string representing the list.

### Example Usage

```python
ll = LinkedList()
print(ll.is_empty())   # True
ll.append(10)
ll.append(20)
ll.prepend(5)
print(ll.print_list()) # 5 -> 10 -> 20 -> None
print(ll.size())       # 3
ll.delete(10)
print(ll.print_list()) # 5 -> 20 -> None
print(ll.find(20))     # True
print(ll.find(99))     # False
```

### Answer Key

Once you are confident in your implementation, run the tests:

```
python Test.py LL.py
```

If all tests passed you should see an "OK" message.

