## Why
Avoid a storage write when a cached value is unchanged. Callers rely on the return value; the new `"unchanged"` result needs review.

## Scope
Read [cache.py](cache.py) first. The head adds one guard before persistence:
```diff
 def save(cache, key, value, persist):
+    if key in cache and cache[key] == value:
+        return "unchanged"
     persist(key, value)
```
Existing keys with equal values return `"unchanged"` without calling `persist`. Missing keys, including a new `None` value, still persist and return `"written"`.

The patch changes only `cache.py`; the three regression tests already exist at the base revision.

## Blast Radius
The return contract changes for unchanged values. Existing callers should be checked for assumptions that every call returns `"written"`.

Human review note: “Callers rely on the return value. The new unchanged result needs review.”

## Verification
The supplied fixture receipts show `python3 -B -m unittest -v`: base failed the unchanged-value case (three tests, one failure); head passed all three tests. Live application proof and independent trail review are unavailable.

[Review appendix: decisions, evidence and gaps](review-appendix.md).
