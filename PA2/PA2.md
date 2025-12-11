# Programming Assignment 2: Stack Implementation

### Objective
The objective of this assignment is to get familiar with Python class syntax and object oriented programming by implementing a simple data structure. The underlying data structure utilized by the Stack class is simply a list. Operations supported by the stack class are listed as below.

Note that the list data structure implemented in python is already equipped with various operations that can greatly faciliate the implementation of this assignment. Feel free to checkout the documentation.

### Requirements & Details of Implementation 

You are required to implement a Python class named `Stack` in a file named `stack.py`. The stack should follow the Last-In-First-Out (LIFO) principle.


### Error Throwing
The syntax to throw an error is:
```python
raise IndexError("message")
```
This means that when this line of code is executed, an error would be thrown at this position, usually causing the program to terminate immediately unless handled. Error throwing and handling is essential to programming as it helps programmers understand where and how our code failed.

There are many types of error, these are errors that comes with python:

*   **`IndexError`**: Raised when a sequence subscript is out of range. (e.g., trying to access an index that doesn't exist in a list). This is the Error we will be using in this assignment.
*   **`TypeError`**: Raised when an operation or function is applied to an object of inappropriate type.
*   **`ValueError`**: Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.
*   **`KeyError`**: Raised when a dictionary key is not found.
*   **`AttributeError`**: Raised when an attribute reference or assignment fails.
*   **`ZeroDivisionError`**: Raised when the second argument of a division or modulo operation is zero.


This is an exmaple how you would throw errors in a real function:
```python
def set_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}")
    if age < 0:
        raise ValueError("Age cannot be negative.")
    # proceed with logic if valid
    print(f"Age set to {age}")
```

In future assignments, you will learn how to create custom exceptions, for now, just pay attention to the errors that comes natively with python.

### Class Methods
In `Stack.py` you will find these function signatures defined for you. You are expected to implement the specific logic behind these operations. If you have any questions, please ask Leo (assuming you are Coco).

1.  **`__init__(self)`**
    *   Initializes a new empty stack.
    *   The underlying data structure should be a Python list.

2.  **`push(self, item)`**
    *   Adds a new item to the top of the stack.
    *   **Parameters**: `item` - The item to be added.
    *   **Returns**: None.
    *   The expected time complexity for this operation is O(1).

3.  **`pop(self)`**
    *   Removes and returns the item from the top of the stack.
    *   **Returns**: The item that was removed.
    *   **Error Handling**: If the stack is empty, raise an `IndexError` with the message "pop from empty stack".
    *   The expected time complexity for this operation is O(1).

4.  **`peek(self)`**
    *   Returns the item at the top of the stack without removing it.
    *   **Returns**: The top item.
    *   **Error Handling**: If the stack is empty, raise an `IndexError` with the message "peek from empty stack".
    *   The expected time complexity for this operation is O(1).

5.  **`is_empty(self)`**
    *   Checks whether the stack is empty.
    *   **Returns**: `True` if the stack is empty, `False` otherwise.
    *   The expected time complexity for this operation is O(1).

6.  **`size(self)`**
    *   Returns the number of items in the stack.
    *   **Returns**: An integer representing the size of the stack.
    *   The expected time complexity for this operation is O(1).

### Example Usage

```python
s = Stack()
print(s.is_empty())  # True
s.push(4)
s.push('dog')
print(s.peek())      # 'dog'
s.push(True)
print(s.size())      # 3
print(s.is_empty())  # False
s.push(8.4)
print(s.pop())       # 8.4
print(s.pop())       # True
print(s.size())      # 2
```

### Answer Key

Once you are confident in your implementation or would like to test, you may use the provided `Test.py` file to check your work. Run the following command in your terminal:

```
python3 Test.py Stack.py
```
or
```
python Test.py Stack.py
```

If all tests passed you should see something like this:
```
test_initialization (__main__.TestStackImplementation.test_initialization)
Test that a new stack is empty. ... ok
test_mixed_operations (__main__.TestStackImplementation.test_mixed_operations)
Test a sequence of mixed operations. ... ok
test_peek_empty_stack (__main__.TestStackImplementation.test_peek_empty_stack)
Test that peeking at an empty stack raises IndexError. ... ok
test_pop (__main__.TestStackImplementation.test_pop)
Test popping items from the stack. ... ok
test_pop_empty_stack (__main__.TestStackImplementation.test_pop_empty_stack)
Test that popping from an empty stack raises IndexError. ... ok
test_push_and_peek (__main__.TestStackImplementation.test_push_and_peek)
Test pushing items and peeking at the top. ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```
A reference answer file is provided under `ReferenceAnswers/StackAnswer.py`. Please only look at the file when you have passed all tests to check your understanding.