import unittest
import platform


# Method to add two items, without defaults. Notice that Python does not
# insist on specifying the type of the arguments (unlike Java and C++).
#
def DoSum(Value1, Value2):
    return Value1 + Value2


# Method to add two items, with defaults
def DoSumDefault(Value1=8, Value2=22):
    return Value1 + Value2


# Testing class for function calls
class TestFunc(unittest.TestCase):

    # Confirm that summing two numbers works
    def test_function_with_numbers(self):
        a = DoSum(5, 10)
        self.assertEqual(a, 15)

    # Confirm that summing two strings works
    def test_function_with_strings(self):
        a = DoSum('quantum', 'computing')
        self.assertEqual(a, 'quantumcomputing')

    # Confirm that we can't add mismatched items
    def test_function_with_mismatched_arguments(self):
        result = "cannot concatenate 'str' and 'int' objects"
        with self.assertRaises(Exception) as context:
            a = DoSum('quantum', 2)
        self.assertTrue(result, str(context.exception))

    # Test to call the function with only one argument
    # Python 2: can't call it
    # Python 3: complains about missing a positional argument
    def test_function_calling(self):
        result = 'takes exactly 2 arguments'
        if platform.python_version().startswith('3'):
            result = 'missing 1 required positional argument'
        with self.assertRaises(Exception) as context:
            a = DoSum(7)
        self.assertTrue(result, str(context.exception))

    # Test to use named arguments
    def test_positional(self):
        a = DoSum(Value1=5, Value2=10)
        self.assertEqual(a, 15)

    # Test to use named arguments, but use a nonexistent name
    def test_positional_bad(self):
        with self.assertRaises(Exception) as context:
            a = DoSum(Value=5, Value2=10)
        self.assertTrue('got an unexpected keyword' in str(context.exception))

    # Test using the defaults
    def test_default(self):
        a = DoSumDefault()
        self.assertEqual(a, 30)

    # Test using only the second default
    def test_default_2(self):
        # it assumes the first argument is Value1
        a = DoSumDefault(7)
        self.assertEqual(a, 29)


if __name__ == '__main__':
    unittest.main()
