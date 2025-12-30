class Stack:
    """
    A class representing a stack data structure using a fixed-size list.
    The stack follows the Last-In-First-Out (LIFO) principle.
    """

    def __init__(self, capacity=10):
        """
        Initializes a new empty stack.
        """
        self.capacity = capacity
        self.items = [None] * capacity
        self.num_items = 0

    def push(self, item):
        """
        Adds a new item to the top of the stack.
        Resizes if full.
        """
        if self.num_items == self.capacity:
            # Resize
            self.capacity *= 2
            new_items = [None] * self.capacity
            for i in range(self.num_items):
                new_items[i] = self.items[i]
            self.items = new_items
            
        self.items[self.num_items] = item
        self.num_items += 1

    def pop(self):
        """
        Removes and returns the item from the top of the stack.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        
        item = self.items[self.num_items - 1]
        self.items[self.num_items - 1] = None # Optional: clear reference
        self.num_items -= 1
        return item

    def peek(self):
        """
        Returns the item at the top of the stack without removing it.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[self.num_items - 1]

    def is_empty(self):
        """
        Checks whether the stack is empty.
        """
        return self.num_items == 0

    def size(self):
        """
        Returns the number of items in the stack.
        """
        return self.num_items
