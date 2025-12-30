class Stack:
    """
    A class representing a stack data structure using a fixed-size list (array).
    The stack follows the Last-In-First-Out (LIFO) principle.
    The underlying data structure is a fixed-size Python list.
    """

    def __init__(self, capacity=10):
        """
        Initializes a new empty stack with a fixed capacity.
        
        Parameters:
        capacity: The initial size of the underlying list (default 10).
        """
        # TODO: Initialize self.capacity, self.num_items, and self.items (list of Nones)
        pass

    def push(self, item):
        """
        Adds a new item to the top of the stack.
        If the stack is full, double the capacity and resize.
        
        Parameters:
        item: The item to be added.
        """
        # TODO: Check capacity, resize if needed, then add item
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
        # TODO: Return num_items
        pass

# Example Usage
if __name__ == "__main__":
    s = Stack(capacity=2)
    s.push(1)
    s.push(2)
    # Stack is full (size 2, capacity 2)
    s.push(3) 
    # Resize triggers: Capacity becomes 4
    print(s.size()) # 3
    print(s.pop())  # 3
