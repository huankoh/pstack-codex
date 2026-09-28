import { test, expect } from "bun:test";
import { readSnapshot, classifyPr } from "../src/pstack-codex/skills/poteto-mode/scripts/watch-pr/policy.ts";
import { fakeReader } from "../src/pstack-codex/skills/poteto-mode/scripts/watch-pr/fakes.test-helper.ts";
import { parsePrNumber } from "../src/pstack-codex/skills/poteto-mode/scripts/watch-pr/types.ts";

for (const [reviewDecision, reason] of [["REVIEW_REQUIRED", "review-required"], ["APPROVED", "merge-blocked"]] as const) {
  test(`blocked PR with ${reviewDecision} never becomes ready`, async () => {
    const snapshot = await readSnapshot({
      reader: fakeReader({ facts: { reviewDecision, mergeStateStatus: "BLOCKED" } }),
      context: { owner: "owner", repo: "repo", number: parsePrNumber(23) },
      pendingHistory: "omit", allowDraft: false,
    });
    const decision = classifyPr(snapshot);
    expect(decision.kind).toBe("blocker");
    if (decision.kind !== "blocker") throw new Error("missing blocker");
    expect(decision.blocker.reason).toBe(reason);
  });
}
