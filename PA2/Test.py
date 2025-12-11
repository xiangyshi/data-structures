import sys
import importlib.util
import os
import unittest

def load_module_from_path(path, module_name):
    """Dynamically loads a module from a file path."""
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None:
        raise ImportError(f"Could not load module from path: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

class TestStackImplementation(unittest.TestCase):
    """
    Unit tests for the Stack implementation.
    The Stack class is dynamically loaded from the provided file path.
    """
    
    StackClass = None  # Class reference to be set before running tests

    def setUp(self):
        """Creates a new stack instance before each test."""
        if self.StackClass is None:
            self.fail("Stack class not loaded properly.")
        self.stack = self.StackClass()

    def test_initialization(self):
        """Test that a new stack is empty."""
        try:
            self.assertTrue(self.stack.is_empty(), "New stack should be empty")
            self.assertEqual(self.stack.size(), 0, "New stack size should be 0")
        except Exception as e:
            self.fail(f"Initialization test failed: {str(e)}")

    def test_push_and_peek(self):
        """Test pushing items and peeking at the top."""
        try:
            self.stack.push(10)
            self.assertFalse(self.stack.is_empty(), "Stack should not be empty after push")
            self.assertEqual(self.stack.peek(), 10, "Peek should return the last pushed item (10)")
            
            self.stack.push("hello")
            self.assertEqual(self.stack.peek(), "hello", "Peek should return the last pushed item ('hello')")
            self.assertEqual(self.stack.size(), 2, "Stack size should be 2 after two pushes")
        except Exception as e:
            self.fail(f"Push/Peek test failed: {str(e)}")

    def test_pop(self):
        """Test popping items from the stack."""
        try:
            self.stack.push(1)
            self.stack.push(2)
            
            popped_item = self.stack.pop()
            self.assertEqual(popped_item, 2, "Pop should return the last pushed item (2)")
            self.assertEqual(self.stack.size(), 1, "Stack size should decrease after pop")
            
            popped_item = self.stack.pop()
            self.assertEqual(popped_item, 1, "Pop should return the remaining item (1)")
            self.assertTrue(self.stack.is_empty(), "Stack should be empty after popping all items")
        except Exception as e:
            self.fail(f"Pop test failed: {str(e)}")

    def test_pop_empty_stack(self):
        """Test that popping from an empty stack raises IndexError."""
        try:
            with self.assertRaises(IndexError, msg="Pop on empty stack should raise IndexError") as cm:
                self.stack.pop()
            self.assertEqual(str(cm.exception), "pop from empty stack", 
                             "Error message should be 'pop from empty stack'")
        except Exception as e:
            # If assertRaises fails (no exception raised), unittest handles it, 
            # but we catch other unexpected errors here.
            if isinstance(e, self.failureException):
                raise e
            self.fail(f"Pop empty stack test failed with unexpected error: {str(e)}")

    def test_peek_empty_stack(self):
        """Test that peeking at an empty stack raises IndexError."""
        try:
            with self.assertRaises(IndexError, msg="Peek on empty stack should raise IndexError") as cm:
                self.stack.peek()
            self.assertEqual(str(cm.exception), "peek from empty stack", 
                             "Error message should be 'peek from empty stack'")
        except Exception as e:
            if isinstance(e, self.failureException):
                raise e
            self.fail(f"Peek empty stack test failed with unexpected error: {str(e)}")

    def test_mixed_operations(self):
        """Test a sequence of mixed operations."""
        try:
            self.stack.push(5)
            self.stack.push(10)
            self.assertEqual(self.stack.pop(), 10)
            self.stack.push(15)
            self.assertEqual(self.stack.size(), 2)
            self.assertEqual(self.stack.peek(), 15)
            self.assertEqual(self.stack.pop(), 15)
            self.assertEqual(self.stack.pop(), 5)
            self.assertTrue(self.stack.is_empty())
        except Exception as e:
            self.fail(f"Mixed operations test failed: {str(e)}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python Test.py <path_to_stack_file>")
        print("Example: python Test.py ../PA1 - Stack/Stack.py")
        sys.exit(1)

    file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    # Convert relative path to absolute path to avoid import issues
    abs_file_path = os.path.abspath(file_path)
    
    try:
        # Load the module containing the Stack class
        stack_module = load_module_from_path(abs_file_path, "StackModule")
        
        # Check if Stack class exists in the loaded module
        if not hasattr(stack_module, 'Stack'):
            print(f"Error: Class 'Stack' not found in {file_path}")
            sys.exit(1)
            
        # Inject the loaded Stack class into the Test Case
        TestStackImplementation.StackClass = stack_module.Stack
        
        # Remove the file path argument so unittest.main doesn't try to parse it
        sys.argv.pop(1)
        
        # Run the tests
        unittest.main(verbosity=2)
        
    except Exception as e:
        print(f"An error occurred while loading or testing the file: {e}")
        sys.exit(1)

