import copy

class Series:
    """
    A class representing a one-dimensional labeled array.
    """

    def __init__(self, row_names, data):
        """
        Constructs a new Series object.
        
        Parameters:
        row_names: List of strings (can be None)
        data: List of integers (cannot be None)
        """
        # TODO: Implement initialization with validation
        pass

    def __str__(self):
        """
        Returns a string representation of the Series object.
        """
        # TODO: Implement string representation
        pass

    def get_length(self):
        """
        Returns the length of the series object.
        """
        # TODO: Return length
        pass

    def get_row_names(self):
        """
        Returns a copy of the row names.
        """
        # TODO: Return copy of row names
        pass

    def get_data(self):
        """
        Returns a copy of the data.
        """
        # TODO: Return copy of data
        pass

    def append(self, rn, d):
        """
        Adds a new pair of rowName and data at the end of the Series.
        """
        # TODO: Implement append logic
        pass

    def loc(self, rn):
        """
        Retrieves data value(s) given a row name or list of row names.
        """
        # TODO: Implement loc logic for single string and list of strings
        pass

    def iloc(self, ind):
        """
        Retrieves a data value based on its integer index.
        """
        # TODO: Implement iloc logic
        pass

    def drop(self, rn):
        """
        Removes a pair of rowname-data from the Series, given a row name.
        """
        # TODO: Implement drop logic
        pass

    def fill_null(self, value):
        """
        Replace any data value that is None with value.
        """
        # TODO: Implement fill_null
        pass

    def fill_null_with_mean(self):
        """
        Replace any data value that is None with the mean of the Series.
        """
        # TODO: Implement fill_null_with_mean
        pass

if __name__ == "__main__":
    # 1. Initialization and printing
    data = [10, 20, None]
    names = ["a", "b", "c"]
    s = Series(names, data)
    print(s)
    # Output:
    # Printing Series...
    #
    # a    10
    # b    20
    # c    None

    # 2. Accessing data by row name (loc)
    print(s.loc("a"))      # 10
    print(s.loc(["a", "c"])) # [10, None]

    # 3. Accessing data by integer index (iloc)
    print(s.iloc(1))       # 20
    print(s.iloc(0))       # 10

    # 4. Handling Null values
    s.fill_null(0)
    print(s.loc("c"))      # 0

    # 5. Modifying the Series (append and drop)
    s.append("d", 30)
    print(s.get_length())  # 4
    print(s.loc("d"))      # 30

    s.drop("b")
    print(s.get_length())  # 3
    print(s.loc("b"))      # None (assuming not found returns None)