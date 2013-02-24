from sum import sum
#import sum
import unittest

class TestSum(unittest.TestCase):

    # Initialise test suite.
    def setUp(self):
        pass

    # Clean up test suite.
    def tearDown(self):
        pass

    # Test sum(1, 0).
    def test_sum10(self):
        self.assertTrue(1 == sum(1, 0))

    # Test sum(0, 1).
    def test_sum01(self):
        self.assertEqual(1, sum(0, 1))

if __name__ == '__main__':
    unittest.main()
