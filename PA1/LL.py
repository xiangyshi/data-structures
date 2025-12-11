class LLNode:
    """
    A class representing a node in a singly linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    A class representing a singly linked list.
    """

    def __init__(self):
        """
        Initializes a new empty linked list.
        """
        # TODO: Initialize head
        pass

    def append(self, data):
        """
        Adds a new node containing data to the end of the list.
        
        Parameters:
        data: The item to be added.
        """
        # TODO: Implement append
        pass

    def prepend(self, data):
        """
        Adds a new node containing data to the beginning of the list.
        
        Parameters:
        data: The item to be added.
        """
        # TODO: Implement prepend
        pass

    def delete(self, data):
        """
        Removes the first occurrence of a node containing data.
        
        Parameters:
        data: The item to be removed.
        
        Raises:
        ValueError: If the data is not found, with message "Data not found".
        """
        # TODO: Implement delete
        pass

    def find(self, data):
        """
        Searches for a node containing data.
        
        Parameters:
        data: The item to search for.
        
        Returns:
        True if found, False otherwise.
        """
        # TODO: Implement find
        pass

    def is_empty(self):
        """
        Checks if the list is empty.
        
        Returns:
        True if the list is empty, False otherwise.
        """
        # TODO: Implement is_empty
        pass

    def size(self):
        """
        Returns the number of nodes in the list.
        
        Returns:
        An integer representing the size.
        """
        # TODO: Implement size
        pass

    def print_list(self):
        """
        Returns a string representation of the list in the format: val1 -> val2 -> val3 -> None.
        
        Returns:
        A string representing the list.
        """
        # TODO: Implement print_list
        pass

