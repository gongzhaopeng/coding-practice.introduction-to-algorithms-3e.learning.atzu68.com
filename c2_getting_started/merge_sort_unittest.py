import unittest

from merge_sort import merge_sort


class MergeSortTests(unittest.TestCase):

    def test_single_elem_seq_sorting(self):
        single_elem_seq = [1]
        expected_sorted_seq = [1]

        merge_sort(single_elem_seq)
        self.assertListEqual(single_elem_seq, expected_sorted_seq)

    def test_odd_size_seq_sorting(self):
        odd_size_seq = [1, 3, 2]
        expected_sorted_seq = [1, 2, 3]

        merge_sort(odd_size_seq)
        self.assertListEqual(odd_size_seq, expected_sorted_seq)

    def test_even_size_seq_sorting(self):
        even_size_seq = [2, 1]
        expected_sorted_seq = [1, 2]

        merge_sort(even_size_seq)
        self.assertListEqual(even_size_seq, expected_sorted_seq)

    def test_asc_seq_sorting(self):
        asc_seq = [1, 2, 3, 4, 5]
        expected_sorted_seq = [1, 2, 3, 4, 5]

        merge_sort(asc_seq)
        self.assertListEqual(asc_seq, expected_sorted_seq)

    def test_desc_seq_sorting(self):
        desc_seq = [5, 4, 3, 2, 1]
        expected_sorted_seq = [1, 2, 3, 4, 5]

        merge_sort(desc_seq)
        self.assertListEqual(desc_seq, expected_sorted_seq)

    def test_shuffled_seq_sorting(self):
        shuffled_seq = [3, 1, 4, 5, 2]
        expected_seq = [1, 2, 3, 4, 5]

        merge_sort(shuffled_seq)
        self.assertListEqual(shuffled_seq, expected_seq)


if __name__ == '__main__':
    unittest.main()
