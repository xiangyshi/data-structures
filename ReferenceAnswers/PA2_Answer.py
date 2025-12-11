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
        self.items = []

    def push(self, item):
        """
        Adds a new item to the top of the stack.
        
        Parameters:
        item: The item to be added.
        """
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the item from the top of the stack.
        
        Returns:
        The item that was removed.
        
        Raises:
        IndexError: If the stack is empty, with message "pop from empty stack".
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """
        Returns the item at the top of the stack without removing it.
        
        Returns:
        The top item.
        
        Raises:
        IndexError: If the stack is empty, with message "peek from empty stack".
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """
        Checks whether the stack is empty.
        
        Returns:
        True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self):
        """
        Returns the number of items in the stack.
        
        Returns:
        An integer representing the size of the stack.
        """
        return len(self.items)
