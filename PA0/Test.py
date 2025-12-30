import sys
import importlib.util
import os
import unittest

def load_module_from_path(path, module_name):
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None:
        raise ImportError(f"Could not load module from path: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

class TestHashTableImplementation(unittest.TestCase):
    HashTableClass = None

    def setUp(self):
        if self.HashTableClass is None:
            self.fail("HashTable class not loaded.")
        self.ht = self.HashTableClass(size=5)

    def test_initialization(self):
        # Basic check if it runs
        self.assertIsNotNone(self.ht)

    def test_insert_and_get(self):
        self.ht.insert("a", 1)
        self.assertEqual(self.ht.get("a"), 1)
        self.ht.insert("b", 2)
        self.assertEqual(self.ht.get("b"), 2)

    def test_update(self):
        self.ht.insert("a", 1)
        self.ht.insert("a", 100)
        self.assertEqual(self.ht.get("a"), 100)

    def test_get_not_found(self):
        self.assertIsNone(self.ht.get("z"))

    def test_remove(self):
        self.ht.insert("a", 1)
        self.assertTrue(self.ht.remove("a"))
        self.assertIsNone(self.ht.get("a"))
        self.assertFalse(self.ht.remove("a"))

    def test_collision_handling(self):
        # Force collision if possible, but hard to guarantee with built-in hash.
        # Just insert many items into small table.
        small_ht = self.HashTableClass(size=2)
        small_ht.insert("a", 1)
        small_ht.insert("b", 2)
        small_ht.insert("c", 3)
        self.assertEqual(small_ht.get("a"), 1)
        self.assertEqual(small_ht.get("b"), 2)
        self.assertEqual(small_ht.get("c"), 3)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python Test.py <path_to_hashtable_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        sys.exit(1)

    abs_path = os.path.abspath(file_path)
    try:
        mod = load_module_from_path(abs_path, "HashTableModule")
        if not hasattr(mod, 'HashTable'):
            print("HashTable class not found.")
            sys.exit(1)
        TestHashTableImplementation.HashTableClass = mod.HashTable
        sys.argv.pop(1)
        unittest.main(verbosity=2)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

