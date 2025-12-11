import copy

class Series:
    """
    A class representing a one-dimensional labeled array.
    """

    def __init__(self, row_names, data):
        """
        Constructs a new Series object.
        """
        if data is None:
            raise ValueError("Series(row_names, data): data cannot be None. Terminating.")
        
        if row_names is None:
            row_names = [str(i) for i in range(len(data))]
        elif len(row_names) != len(data):
            raise ValueError("Series(row_names, data): Length of row_names and data must match")
        
        # Validate row_names content
        for name in row_names:
            if not isinstance(name, str) or not name:
                raise ValueError("Series: row_names contains invalid entries")

        self.row_names = list(row_names)
        self.data = list(data)

    def __str__(self):
        """
        Returns a string representation of the Series object.
        """
        result = "Printing Series...\n\n"
        for i in range(len(self.row_names)):
            result += f"{self.row_names[i]}\t{self.data[i]}\n"
        return result

    def get_length(self):
        """
        Returns the length of the series object.
        """
        return len(self.data)

    def get_row_names(self):
        """
        Returns a copy of the row names.
        """
        return list(self.row_names)

    def get_data(self):
        """
        Returns a copy of the data.
        """
        return list(self.data)

    def append(self, rn, d):
        """
        Adds a new pair of rowName and data at the end of the Series.
        """
        if not rn:
            rn = str(len(self.row_names))
        
        self.row_names.append(rn)
        self.data.append(d)

    def loc(self, rn):
        """
        Retrieves data value(s) given a row name or list of row names.
        """
        if rn is None:
            raise ValueError("loc: rn cannot be None")

        if isinstance(rn, str):
            if not rn:
                raise ValueError("loc: rn cannot be empty string")
            # Find first match
            try:
                idx = self.row_names.index(rn)
                return self.data[idx]
            except ValueError:
                return None
        
        elif isinstance(rn, list):
            if not rn:
                raise ValueError("loc: rn list cannot be empty")
            result = []
            for name in rn:
                try:
                    # Recursive call for single item logic (simplifies, but handles finding index)
                    # Note: Java implementation does linear scan. Here list.index is linear.
                    if name in self.row_names:
                        idx = self.row_names.index(name)
                        result.append(self.data[idx])
                    else:
                        result.append(None)
                except ValueError: # Should not hit if check is correct
                    result.append(None)
            return result
        else:
            raise ValueError("loc: rn must be string or list of strings")

    def iloc(self, ind):
        """
        Retrieves a data value based on its integer index.
        """
        try:
            return self.data[ind]
        except IndexError:
            return None

    def drop(self, rn):
        """
        Removes a pair of rowname-data from the Series, given a row name.
        """
        if not rn:
            raise ValueError("drop: rn invalid")
            
        try:
            idx = self.row_names.index(rn)
            self.row_names.pop(idx)
            self.data.pop(idx)
            return True
        except ValueError:
            return False

    def fill_null(self, value):
        """
        Replace any data value that is None with value.
        """
        if value is None:
            raise ValueError("fill_null: value cannot be None")
            
        for i in range(len(self.data)):
            if self.data[i] is None:
                self.data[i] = value

    def fill_null_with_mean(self):
        """
        Replace any data value that is None with the mean of the Series.
        """
        valid_data = [x for x in self.data if x is not None]
        if not valid_data:
            raise ValueError("Cannot calculate mean: all values are None or empty")
            
        mean_val = sum(valid_data) / len(valid_data)
        # Assuming integer series, we might round or keep float. 
        # The Java code used Integer[] implying integer arithmetic or casting.
        # Let's cast to int to match typical Integer array behavior, or keep float if data supports it.
        # Since requirements say "Integer array", we cast to int.
        self.fill_null(int(mean_val))

