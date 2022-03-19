import unittest
from main import check_sum


class TestCheckSum(unittest.TestCase):
    
    def test_check_sum_true(self):
        actual = check_sum([10, 15, 3, 7], 17)
        expected = True
        self.assertEqual(actual, expected)

    def test_check_sum_false(self):
        actual = check_sum([10, 15, 3, 7], 21)
        expected = False
        self.assertEqual(actual, expected)

    def test_check_sum_single_number_times_two(self):
        actual = check_sum([10, 15, 3, 7], 20)
        expected = False
        self.assertEqual(actual, expected)