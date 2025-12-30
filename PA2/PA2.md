# Programming Assignment 2: Stack Implementation

### Objective
The objective of this assignment is to get familiar with Python class syntax and object oriented programming by implementing a Stack data structure using a **fixed-size list** (array) approach. The underlying data structure utilized by the Stack class is a list with a managed capacity. Operations supported by the stack class are listed below.

### Requirements & Details of Implementation 

You are required to implement a Python class named `Stack` in a file named `stack.py`. The stack should follow the Last-In-First-Out (LIFO) principle.

**Key Difference**: Unlike a standard Python list which resizes automatically, you must manage the "capacity" of your underlying list manually.

#### Class Attributes
*   `capacity`: The current maximum number of items the stack can hold before resizing. Default is 10.
*   `items`: A list initialized with `None` values, with a length equal to `capacity`.
*   `num_items`: The current number of actual items in the stack.

#### Class Methods

1.  **`__init__(self, capacity=10)`**
    *   Initializes a new empty stack.
    *   **Parameters**: `capacity` (int) - The initial size of the underlying list. Default is 10.
    *   Initializes `self.items` to a list of `None`s of size `capacity`.
    *   Initializes `self.num_items` to 0.

2.  **`push(self, item)`**
    *   Adds a new item to the top of the stack.
    *   **Parameters**: `item` - The item to be added.
    *   **Logic**:
        *   If `num_items` equals `capacity`:
            *   Double the `capacity`.
            *   Create a new list of the new capacity.
            *   Copy existing items to the new list.
            *   Replace `self.items` with the new list.
        *   Add the item at the next available index (`num_items`).
        *   Increment `num_items`.
    *   **Returns**: None.

3.  **`pop(self)`**
    *   Removes and returns the item from the top of the stack.
    *   **Returns**: The item that was removed.
    *   **Error Handling**: If the stack is empty, raise an `IndexError` with the message "pop from empty stack".
    *   **Logic**:
        *   Retrieve the item at `num_items - 1`.
        *   Set that position to `None` (optional but good practice).
        *   Decrement `num_items`.
        *   Return the item.

4.  **`peek(self)`**
    *   Returns the item at the top of the stack without removing it.
    *   **Returns**: The top item.
    *   **Error Handling**: If the stack is empty, raise an `IndexError` with the message "peek from empty stack".

5.  **`is_empty(self)`**
    *   Checks whether the stack is empty.
    *   **Returns**: `True` if the stack is empty, `False` otherwise.

6.  **`size(self)`**
    *   Returns the number of items in the stack.
    *   **Returns**: An integer representing the size of the stack (`num_items`).

### Example Usage

```python
s = Stack(capacity=2)
s.push(1)
s.push(2)
# Stack is full (size 2, capacity 2)
s.push(3) 
# Resize triggers: Capacity becomes 4
print(s.size()) # 3
print(s.pop())  # 3
```
