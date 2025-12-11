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
        self.head = None

    def append(self, data):
        """
        Adds a new node containing data to the end of the list.
        """
        new_node = LLNode(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """
        Adds a new node containing data to the beginning of the list.
        """
        new_node = LLNode(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """
        Removes the first occurrence of a node containing data.
        """
        if not self.head:
            raise ValueError("Data not found")

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        
        raise ValueError("Data not found")

    def find(self, data):
        """
        Searches for a node containing data.
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def is_empty(self):
        """
        Checks if the list is empty.
        """
        return self.head is None

    def size(self):
        """
        Returns the number of nodes in the list.
        """
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def print_list(self):
        """
        Returns a string representation of the list in the format: val1 -> val2 -> val3 -> None.
        """
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        result.append("None")
        return " -> ".join(result)

