# Programming Assignment 3: Series Implementation

### Objective
The objective of this assignment is to implement a data structure called `Series` (inspired by pandas Series). A Series represents a one-dimensional labeled array capable of holding integer data (including nulls/Nones).

### Requirements & Details of Implementation

You are required to implement a Python class named `Series` in a file named `Series.py`.

#### Class Attributes
*   `row_names`: A list of strings acting as labels for the data.
*   `data`: A list of integers (or `None`) representing the values.

#### Class Methods

1.  **`__init__(self, row_names, data)`**
    *   Initializes the Series.
    *   **Parameters**:
        *   `row_names`: A list of strings. If `None`, defaults to string representation of indices (0 to length-1).
        *   `data`: A list of integers. Cannot be `None`.
    *   **Error Handling**:
        *   If `data` is `None`, raise `ValueError` ("data cannot be None").
        *   If `row_names` is provided but length doesn't match `data`, raise `ValueError` ("Length of row_names and data must match").
        *   Validate `row_names` contains valid non-empty strings.

2.  **`__str__(self)`**
    *   Returns a string representation of the Series.
    *   Format: `row_name \t value \n` for each row.

3.  **`get_length(self)`**
    *   Returns the number of elements in the Series.

4.  **`get_row_names(self)`**
    *   Returns a copy of the row names list.

5.  **`get_data(self)`**
    *   Returns a copy of the data list.

6.  **`append(self, rn, d)`**
    *   Adds a new element.
    *   **Parameters**: `rn` (row name), `d` (data).
    *   If `rn` is `None` or empty, use the current length as the row name.

7.  **`loc(self, rn)`**
    *   Retrieves data by row name.
    *   **Parameters**: `rn` (string) or `rn` (list of strings).
    *   **Returns**:
        *   If `rn` is a single string: The integer value or `None`.
        *   If `rn` is a list: A list of values corresponding to the row names.
    *   **Error Handling**: Raises `ValueError` for invalid inputs (None or empty).

8.  **`iloc(self, ind)`**
    *   Retrieves data by integer index.
    *   **Returns**: The value at index `ind`, or `None` if index is out of bounds.

9.  **`drop(self, rn)`**
    *   Removes an entry by row name.
    *   **Returns**: `True` if removed, `False` if not found.
    *   **Error Handling**: Validate `rn`.

10. **`fill_null(self, value)`**
    *   Replaces all `None` values in `data` with `value`.
    *   **Error Handling**: `value` cannot be `None`.

11. **`fill_null_with_mean(self)`**
    *   Replaces all `None` values with the mean of the existing non-None values.
    *   **Error Handling**: Raise `ValueError` if mean calculation fails (e.g., all values are None).

### Example Usage

```python
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
```

### Answer Key

Run tests:
```bash
python Test.py Series.py
```

