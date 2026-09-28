# Native worktree exercise

This fixture tests the coding workflow, not the plugin's helper unit tests. The current tree contains the integrated solution. Commit `8292ba92bd9bb628210404b781f1d10fbbe3e1a4` preserves the incomplete starting point (five failing integration cases and one passing case).

For a fresh exercise, start disposable worktrees from that commit. Two independent writers implement the contracts below in separate worktrees; the coordinator integrates their commits and a fresh reviewer verifies the combination. Prefer managed worktrees. The recorded run used the documented manual Git fallback because the app's managed tool did not recognize this chat's newly initialized repository.

- `normalize_label(value)`: for string inputs, strip surrounding whitespace, preserve internal spacing, and reject empty/whitespace-only labels with `ValueError`.
- `allocate_units(requested, cap)`: for nonnegative integer inputs, return the smaller value. Reject negative requested units or a negative cap with `ValueError`.
- `render_usage` combines both and must satisfy `test_report.py` after integration.

Worker A owns `labels.py` and an optional `test_labels.py`. Worker B owns `limits.py` and an optional `test_limits.py`. Neither may edit the integration test or the other's module. Use explicit absolute paths; the worktree tool does not change a child's default working directory. Stop children before integrating or archiving.

Run `python3 -m unittest discover -v` from this fixture directory to exercise the integrated behavior. All 16 tests pass in the integrated tree. The ordinary package test command does not discover this nested fixture. See the root `VALIDATION.md` for the observed results and scope.
