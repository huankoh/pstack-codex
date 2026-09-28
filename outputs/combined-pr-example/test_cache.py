import unittest
from cache import save
class CacheTest(unittest.TestCase):
    def test_changed_value_persists(self):
        writes = []
        cache = {"doc": "old"}
        self.assertEqual(save(cache, "doc", "new", lambda *x: writes.append(x)), "written")
        self.assertEqual(writes, [("doc", "new")])
        self.assertEqual(cache["doc"], "new")
    def test_identical_value_skips_storage(self):
        writes = []
        cache = {"doc": "same"}
        self.assertEqual(save(cache, "doc", "same", lambda *x: writes.append(x)), "unchanged")
        self.assertEqual(writes, [])
    def test_missing_none_is_persisted(self):
        writes = []
        cache = {}
        self.assertEqual(save(cache, "doc", None, lambda *x: writes.append(x)), "written")
        self.assertEqual(writes, [("doc", None)])
