class HashTable:
    """
    A class representing a Hash Table using chaining for collision resolution.
    """

    def __init__(self, size=10):
        """
        Initializes the Hash Table with a fixed number of buckets.
        """
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        """
        Computes the index for the key.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Inserts or updates a key-value pair.
        """
        index = self.hash_function(key)
        bucket = self.table[index]
        
        # Check if key exists and update
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Key not found, append
        bucket.append((key, value))

    def get(self, key):
        """
        Retrieves the value for a given key.
        Returns None if not found.
        """
        index = self.hash_function(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        """
        Removes a key-value pair.
        Returns True if removed, False otherwise.
        """
        index = self.hash_function(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return True
        return False

