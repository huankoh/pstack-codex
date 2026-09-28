import unittest

from limits import allocate_units


class AllocationTests(unittest.TestCase):
    def test_returns_smaller_value(self):
        for requested, cap, expected in ((3, 5, 3), (7, 5, 5), (5, 5, 5)):
            with self.subTest(requested=requested, cap=cap):
                self.assertEqual(allocate_units(requested, cap), expected)

    def test_zero_is_valid(self):
        for requested, cap in ((0, 5), (1, 0), (0, 0)):
            with self.subTest(requested=requested, cap=cap):
                self.assertEqual(allocate_units(requested, cap), 0)

    def test_large_integers_remain_exact(self):
        cap = 10**100
        self.assertEqual(allocate_units(cap + 1, cap), cap)

    def test_negative_requested_is_rejected(self):
        with self.assertRaises(ValueError):
            allocate_units(-1, 5)

    def test_negative_cap_is_rejected(self):
        with self.assertRaises(ValueError):
            allocate_units(1, -1)

    def test_both_negative_values_are_rejected(self):
        with self.assertRaises(ValueError):
            allocate_units(-1, -1)


if __name__ == "__main__":
    unittest.main()
