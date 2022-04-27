import unittest

from insertion_sort import insertion_sort


class InsertionSortTests(unittest.TestCase):

    def test_single_elem_seq_sorting(self):
        single_elem_seq = [1]
        expected_sorted_seq = [1]

        insertion_sort(single_elem_seq)
        self.assertListEqual(single_elem_seq, expected_sorted_seq)

    def test_asc_seq_sorting(self):
        asc_seq = [1, 2, 3, 4, 5]
        expected_sorted_seq = [1, 2, 3, 4, 5]

        insertion_sort(asc_seq)
        self.assertListEqual(asc_seq, expected_sorted_seq)

    def test_desc_seq_sorting(self):
        desc_seq = [5, 4, 3, 2, 1]
        expected_sorted_seq = [1, 2, 3, 4, 5]

        insertion_sort(desc_seq)
        self.assertListEqual(desc_seq, expected_sorted_seq)

    def test_shuffled_seq_sorting(self):
        shuffled_seq = [3, 1, 4, 5, 2]
        expected_seq = [1, 2, 3, 4, 5]

        insertion_sort(shuffled_seq)
        self.assertListEqual(shuffled_seq, expected_seq)


if __name__ == '__main__':
    unittest.main()
