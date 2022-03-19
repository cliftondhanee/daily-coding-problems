import unittest
from main import get_product


class TestGetProduct(unittest.TestCase):

    def test_get_product(self):
        actual = get_product([1, 2, 3, 4, 5])
        expected = [120, 60, 40, 30, 24]
        self.assertEqual(actual, expected)

    def test_get_product_empty(self):
        actual = get_product([])
        expected = []
        self.assertEqual(actual, expected)

    def test_get_product_single_index(self):
        actual = get_product([3])
        expected = None
        self.assertEqual(actual, expected)

    def test_get_product_with_zero(self):
        actual = get_product([1, 2, 3, 0, 4, 5])
        expected = [0, 0, 0, 120, 0, 0]
        self.assertEqual(actual, expected)

