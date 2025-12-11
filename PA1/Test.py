import sys
import importlib.util
import os
import unittest

# Helper to load module dynamically
def load_module_from_path(path, module_name):
    """Dynamically loads a module from a file path."""
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None:
        raise ImportError(f"Could not load module from path: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

class TestLinkedListImplementation(unittest.TestCase):
    """
    Unit tests for the LinkedList implementation.
    The LinkedList class is dynamically loaded from the provided file path.
    """
    
    LinkedListClass = None

    def setUp(self):
        """Creates a new linked list instance before each test."""
        if self.LinkedListClass is None:
            self.fail("LinkedList class not loaded properly.")
        self.ll = self.LinkedListClass()

    def test_initialization(self):
        """Test that a new linked list is empty."""
        try:
            self.assertTrue(self.ll.is_empty(), "New list should be empty")
            self.assertEqual(self.ll.size(), 0, "New list size should be 0")
            self.assertEqual(self.ll.print_list(), "None", "Empty list string representation should be 'None'")
        except Exception as e:
            self.fail(f"Initialization test failed: {str(e)}")

    def test_append(self):
        """Test appending items to the list."""
        try:
            self.ll.append(10)
            self.assertFalse(self.ll.is_empty(), "List should not be empty after append")
            self.assertEqual(self.ll.size(), 1, "Size should be 1 after one append")
            self.assertEqual(self.ll.print_list(), "10 -> None")
            
            self.ll.append(20)
            self.assertEqual(self.ll.size(), 2)
            self.assertEqual(self.ll.print_list(), "10 -> 20 -> None")
        except Exception as e:
            self.fail(f"Append test failed: {str(e)}")

    def test_prepend(self):
        """Test prepending items to the list."""
        try:
            self.ll.prepend(10)
            self.assertEqual(self.ll.print_list(), "10 -> None")
            
            self.ll.prepend(5)
            self.assertEqual(self.ll.print_list(), "5 -> 10 -> None")
            self.assertEqual(self.ll.size(), 2)
        except Exception as e:
            self.fail(f"Prepend test failed: {str(e)}")

    def test_find(self):
        """Test finding items in the list."""
        try:
            self.ll.append(10)
            self.ll.append(20)
            self.ll.append(30)
            
            self.assertTrue(self.ll.find(10), "Should find 10")
            self.assertTrue(self.ll.find(20), "Should find 20")
            self.assertTrue(self.ll.find(30), "Should find 30")
            self.assertFalse(self.ll.find(99), "Should not find 99")
        except Exception as e:
            self.fail(f"Find test failed: {str(e)}")

    def test_delete(self):
        """Test deleting items from the list."""
        try:
            self.ll.append(10)
            self.ll.append(20)
            self.ll.append(30)
            
            # Delete from middle
            self.ll.delete(20)
            self.assertEqual(self.ll.print_list(), "10 -> 30 -> None")
            self.assertEqual(self.ll.size(), 2)
            
            # Delete from head
            self.ll.delete(10)
            self.assertEqual(self.ll.print_list(), "30 -> None")
            self.assertEqual(self.ll.size(), 1)
            
            # Delete last element
            self.ll.delete(30)
            self.assertTrue(self.ll.is_empty())
            self.assertEqual(self.ll.print_list(), "None")
        except Exception as e:
            self.fail(f"Delete test failed: {str(e)}")

    def test_delete_not_found(self):
        """Test that deleting a non-existent item raises ValueError."""
        try:
            self.ll.append(10)
            with self.assertRaises(ValueError, msg="Delete non-existent item should raise ValueError") as cm:
                self.ll.delete(99)
            self.assertEqual(str(cm.exception), "Data not found")
            
            # Test on empty list
            empty_ll = self.LinkedListClass()
            with self.assertRaises(ValueError, msg="Delete on empty list should raise ValueError") as cm:
                empty_ll.delete(10)
            self.assertEqual(str(cm.exception), "Data not found")
        except Exception as e:
            if isinstance(e, self.failureException):
                raise e
            self.fail(f"Delete not found test failed with unexpected error: {str(e)}")

    def test_mixed_operations(self):
        """Test a sequence of mixed operations."""
        try:
            self.ll.append(1)
            self.ll.prepend(0)
            self.ll.append(2)
            # List: 0 -> 1 -> 2 -> None
            self.assertEqual(self.ll.print_list(), "0 -> 1 -> 2 -> None")
            self.assertEqual(self.ll.size(), 3)
            
            self.ll.delete(1)
            # List: 0 -> 2 -> None
            self.assertEqual(self.ll.print_list(), "0 -> 2 -> None")
            self.assertTrue(self.ll.find(2))
            
            self.ll.delete(0)
            self.ll.delete(2)
            self.assertTrue(self.ll.is_empty())
        except Exception as e:
            self.fail(f"Mixed operations test failed: {str(e)}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python Test.py <path_to_ll_file>")
        print("Example: python Test.py LL.py")
        sys.exit(1)

    file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    abs_file_path = os.path.abspath(file_path)
    
    try:
        # Load the module containing the LinkedList class
        ll_module = load_module_from_path(abs_file_path, "LLModule")
        
        if not hasattr(ll_module, 'LinkedList'):
            print(f"Error: Class 'LinkedList' not found in {file_path}")
            sys.exit(1)
            
        TestLinkedListImplementation.LinkedListClass = ll_module.LinkedList
        
        sys.argv.pop(1)
        unittest.main(verbosity=2)
        
    except Exception as e:
        print(f"An error occurred while loading or testing the file: {e}")
        sys.exit(1)

