import unittest

from maximum_subarray import find_maximum_subarray


class MaximumSubarrayTests(unittest.TestCase):
    def test_simple_basic_case(self):
        simple_basic_array = [13, -3, -25, 20, -3, -16, -23, 18,
                              20, -7, 12, -5, -22, 15, -4, 7]
        expected_maximum_subarray = 7, 11, 43  # (subarray_low_inclusive, subarray_high_exclusive, subarray_sum)

        found_maximum_subarray = find_maximum_subarray(simple_basic_array)
        self.assertEqual(expected_maximum_subarray, found_maximum_subarray)
