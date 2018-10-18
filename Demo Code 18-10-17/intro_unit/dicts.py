import unittest


# Testing class for dictionary
class TestDict(unittest.TestCase):

    def setUp(self):
        self.sample = {1: "Gardner", 2: "Judge", 3: "Stanton", 4: "Sanchez"}

    # Test listing all the keys
    def test_keys(self):
        result = [1, 2, 3, 4]
        self.assertEqual(result, list(self.sample.keys()))

    # Test listing all the keys
    def test_values(self):
        result = ['Gardner', 'Judge', 'Stanton', 'Sanchez']
        self.assertEqual(result, list(self.sample.values()))

    def test_clear(self):
        self.sample.clear()
        self.assertEqual(0, len(self.sample))

    def test_get(self):
        self.assertEqual('Gardner', self.sample[1])
        self.assertEqual('Gardner', self.sample.__getitem__(1))

    def test_add(self):
        self.sample[5] = "Torres"
        result = ['Gardner', 'Judge', 'Stanton', 'Sanchez', 'Torres']
        self.assertEqual(result, list(self.sample.values()))


if __name__ == '__main__':
    unittest.main()
