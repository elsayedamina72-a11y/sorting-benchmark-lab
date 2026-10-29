"""Unit tests. Run with:  python -m unittest -v"""
import random
import unittest

from sorts import insertion_sort, insertion_sort_counts, merge_sort, python_sorted

ALGORITHMS = [insertion_sort, merge_sort, python_sorted]


class TestSorts(unittest.TestCase):
    def check_all(self, data):
        expected = sorted(data)
        for algo in ALGORITHMS:
            self.assertEqual(algo(data), expected, msg=algo.__name__)

    def test_empty(self):
        self.check_all([])

    def test_single(self):
        self.check_all([7])

    def test_two_elements(self):
        self.check_all([2, 1])
        self.check_all([1, 2])

    def test_already_sorted(self):
        self.check_all(list(range(100)))

    def test_reverse_sorted(self):
        self.check_all(list(range(100, 0, -1)))

    def test_duplicates(self):
        self.check_all([3, 1, 3, 1, 2, 2, 3, 1])

    def test_all_equal(self):
        self.check_all([5] * 50)

    def test_negative_numbers(self):
        self.check_all([-5, 3, 0, -1, 8, -10, 2])

    def test_random_inputs(self):
        rng = random.Random(0)
        for _ in range(50):
            n = rng.randint(0, 200)
            self.check_all([rng.randint(-1000, 1000) for _ in range(n)])

    def test_input_not_modified(self):
        data = [5, 2, 9, 1]
        copy = data[:]
        for algo in ALGORITHMS:
            algo(data)
            self.assertEqual(data, copy, msg=algo.__name__)

    def test_stability_of_merge_sort(self):
        # Sort pairs by key only: equal keys must keep original order.
        class Item:
            def __init__(self, key, tag):
                self.key, self.tag = key, tag

            def __le__(self, other):
                return self.key <= other.key

            def __gt__(self, other):
                return self.key > other.key

        items = [Item(1, "a"), Item(0, "b"), Item(1, "c"), Item(0, "d")]
        result = merge_sort(items)
        self.assertEqual([i.tag for i in result], ["b", "d", "a", "c"])


class TestCounters(unittest.TestCase):
    def test_reverse_input_worst_case(self):
        _, c, s = insertion_sort_counts([4, 3, 2, 1])
        self.assertEqual((c, s), (6, 6))  # n(n-1)/2 with n = 4

    def test_sorted_input_best_case(self):
        _, c, s = insertion_sort_counts([1, 2, 3, 4])
        self.assertEqual((c, s), (3, 0))  # n-1 comparisons, no shifts

    def test_counts_match_formula_for_reverse(self):
        n = 50
        _, c, s = insertion_sort_counts(list(range(n, 0, -1)))
        self.assertEqual(c, n * (n - 1) // 2)
        self.assertEqual(s, n * (n - 1) // 2)


if __name__ == "__main__":
    unittest.main()
