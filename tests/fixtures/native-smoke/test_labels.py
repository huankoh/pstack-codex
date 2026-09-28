import unittest

from labels import normalize_label


class NormalizeLabelTests(unittest.TestCase):
    def test_strips_surrounding_whitespace(self):
        self.assertEqual(normalize_label(" \t\nalpha beta\r\n "), "alpha beta")

    def test_preserves_internal_spacing(self):
        self.assertEqual(
            normalize_label("  alpha  beta\tgamma\ndelta  "),
            "alpha  beta\tgamma\ndelta",
        )

    def test_preserves_label_without_outer_whitespace(self):
        self.assertEqual(normalize_label("alpha"), "alpha")

    def test_rejects_empty_or_whitespace_only_labels(self):
        for value in ("", " ", "\t\r\n", "\u2003"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    normalize_label(value)


if __name__ == "__main__":
    unittest.main()
