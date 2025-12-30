class HashTable:
    """
    A class representing a Hash Table using chaining for collision resolution.
    """

    def __init__(self, size=10):
        """
        Initializes the Hash Table with a fixed number of buckets.
        """
        self.size = size
        self.table = []
        for i in range(size):
            self.table.append([])

    def hash_function(self, key):
        """
        Computes the index for the key.
        """
        # TODO: Implement hash function (hash(key) % size)
        pass

    def insert(self, key, value):
        """
        Inserts or updates a key-value pair.
        """
        # TODO: Implement insert logic
        pass

    def get(self, key):
        """
        Retrieves the value for a given key.
        Returns None if not found.
        """
        # TODO: Implement get logic
        pass

    def remove(self, key):
        """
        Removes a key-value pair.
        Returns True if removed, False otherwise.
        """
        # TODO: Implement remove logic
        pass

    def print_table(self):
        """
        Helper method to print the hash table contents for debugging.
        """
        print("\n" + "=" * 20)
        print("Hash Table Contents:")
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")
        print("=" * 20 + "\n")

if __name__ == "__main__":
    # Example Usage
    ht = HashTable(size=5)
    print("Inserted 'apple' -> 10")
    ht.insert("apple", 10)
    print("Inserted 'banana' -> 20")
    ht.insert("banana", 20)
    
    ht.print_table()
    
    print(f"Get 'apple': {ht.get('apple')}")   # 10
    
    print("Updating 'apple' -> 15")
    ht.insert("apple", 15)   # Update
    print(f"Get 'apple': {ht.get('apple')}")   # 15
    
    print(f"Remove 'banana': {ht.remove('banana')}") # True
    print(f"Get 'banana': {ht.get('banana')}")    # None
    
    ht.print_table()

