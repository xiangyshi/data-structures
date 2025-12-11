class Stack:
    """
    A class representing a stack data structure.
    The stack follows the Last-In-First-Out (LIFO) principle.
    The underlying data structure is a Python list.
    """

    def __init__(self):
        """
        Initializes a new empty stack.
        """
        # TODO: Initialize the underlying list here
        pass

    def push(self, item):
        """
        Adds a new item to the top of the stack.
        
        Parameters:
        item: The item to be added.
        """
        # TODO: Implement push operation
        pass

    def pop(self):
        """
        Removes and returns the item from the top of the stack.
        
        Returns:
        The item that was removed.
        
        Raises:
        IndexError: If the stack is empty, with message "pop from empty stack".
        """
        # TODO: Implement pop operation
        pass

    def peek(self):
        """
        Returns the item at the top of the stack without removing it.
        
        Returns:
        The top item.
        
        Raises:
        IndexError: If the stack is empty, with message "peek from empty stack".
        """
        # TODO: Implement peek operation
        pass

    def is_empty(self):
        """
        Checks whether the stack is empty.
        
        Returns:
        True if the stack is empty, False otherwise.
        """
        # TODO: Implement is_empty check
        pass

    def size(self):
        """
        Returns the number of items in the stack.
        
        Returns:
        An integer representing the size of the stack.
        """
        # TODO: Implement size calculation
        pass

# Example Usage
if __name__ == "__main__":
    s = Stack()
    print(s.is_empty()) # True
    s.push(4)
    s.push('dog')
    print(s.peek()) # dog
    s.push(True)
    print(s.size()) # 3
    print(s.is_empty()) # False
    s.push(8.4)
    print(s.pop()) # 8.4
    print(s.pop())

    # Expected Output:
    # True
    # dog
    # 3
    # False
    # 8.4
    # True