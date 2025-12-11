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

class TestSeriesImplementation(unittest.TestCase):
    SeriesClass = None

    def setUp(self):
        if self.SeriesClass is None:
            self.fail("Series class not loaded.")

    def test_init_valid(self):
        s = self.SeriesClass(["a", "b"], [1, 2])
        self.assertEqual(s.get_length(), 2)
        self.assertEqual(s.get_data(), [1, 2])
        self.assertEqual(s.get_row_names(), ["a", "b"])

    def test_init_default_names(self):
        s = self.SeriesClass(None, [10, 20])
        self.assertEqual(s.get_row_names(), ["0", "1"])

    def test_init_errors(self):
        with self.assertRaisesRegex(ValueError, "data cannot be None"):
            self.SeriesClass(["a"], None)
        with self.assertRaisesRegex(ValueError, "Length of row_names and data must match"):
            self.SeriesClass(["a"], [1, 2])

    def test_append(self):
        s = self.SeriesClass(["a"], [1])
        s.append("b", 2)
        self.assertEqual(s.get_length(), 2)
        self.assertEqual(s.loc("b"), 2)

    def test_loc_single(self):
        s = self.SeriesClass(["x", "y"], [100, 200])
        self.assertEqual(s.loc("x"), 100)
        self.assertIsNone(s.loc("z"))

    def test_loc_multiple(self):
        s = self.SeriesClass(["x", "y", "z"], [10, 20, 30])
        res = s.loc(["x", "z", "w"])
        self.assertEqual(res, [10, 30, None])

    def test_iloc(self):
        s = self.SeriesClass(["x"], [99])
        self.assertEqual(s.iloc(0), 99)
        self.assertIsNone(s.iloc(5))

    def test_drop(self):
        s = self.SeriesClass(["a", "b"], [1, 2])
        self.assertTrue(s.drop("a"))
        self.assertEqual(s.get_length(), 1)
        self.assertEqual(s.loc("a"), None)
        self.assertFalse(s.drop("z"))

    def test_fill_null(self):
        s = self.SeriesClass(["a", "b"], [1, None])
        s.fill_null(0)
        self.assertEqual(s.loc("b"), 0)

    def test_fill_null_with_mean(self):
        s = self.SeriesClass(["a", "b", "c"], [10, 20, None])
        s.fill_null_with_mean()
        # Mean of 10 and 20 is 15.0 -> integer 15 (depending on implementation, let's assume int logic or float)
        # Java code implied int arithmetic but Tool.mean might differ. 
        # Python mean usually float. But let's check exact return.
        # If we assume int division: (10+20)/2 = 15.
        self.assertEqual(s.loc("c"), 15)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python Test.py <path_to_series_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        sys.exit(1)

    abs_path = os.path.abspath(file_path)
    try:
        mod = load_module_from_path(abs_path, "SeriesModule")
        if not hasattr(mod, 'Series'):
            print("Series class not found.")
            sys.exit(1)
        TestSeriesImplementation.SeriesClass = mod.Series
        sys.argv.pop(1)
        unittest.main(verbosity=2)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

