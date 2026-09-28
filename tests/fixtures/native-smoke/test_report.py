import unittest
from report import render_usage


class IntegrationTests(unittest.TestCase):
    def test_normalizes_label_and_applies_cap(self):
        self.assertEqual(render_usage("  team alpha  ", 7, 5), "team alpha: 5")

    def test_preserves_internal_spacing(self):
        self.assertEqual(render_usage("team  alpha", 3, 5), "team  alpha: 3")

    def test_zero_is_valid(self):
        self.assertEqual(render_usage("team", 1, 0), "team: 0")

    def test_blank_label_is_rejected(self):
        with self.assertRaises(ValueError):
            render_usage(" \t ", 3, 5)

    def test_negative_units_are_rejected(self):
        with self.assertRaises(ValueError):
            render_usage("team", -1, 5)

    def test_negative_cap_is_rejected(self):
        with self.assertRaises(ValueError):
            render_usage("team", 1, -1)


if __name__ == "__main__":
    unittest.main()
