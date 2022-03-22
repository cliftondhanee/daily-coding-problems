import unittest
from main import get_lowest_positive_int


class TestGetLowestPositiveInt(unittest.TestCase):

    def test_get_lowest_positive_int(self):
        actual = get_lowest_positive_int([1, 2, 0])
        expected = 3
        self.assertEqual(actual, expected)

    def test_get_lowest_positive_int_negative_value(self):
        actual = get_lowest_positive_int([3, 4, -1, 1])
        expected = 2
        self.assertEqual(actual, expected)

    def test_get_lowest_positive_int_duplicate_value(self):
        actual = get_lowest_positive_int([1, 4, 1, -4, 0, 2])
        expected = 3