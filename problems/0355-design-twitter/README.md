# 355. Design Twitter

[Problem on LeetCode](https://leetcode.com/problems/design-twitter/) · Medium

## Approach, invariant, and complexity

Each user's posts form a chronological stream. Merge only the newest available post from each visible stream with a heap and stop after ten results.

A baseline filters all visible posts and sorts them, O(T log T) time. The heap contains the newest unreturned post from each source. Popping its newest entry produces the next globally newest visible post; replacing it with the preceding post from that source preserves this invariant.

For F visible users, feed construction takes O(F + 10 log(F + 1)) time and O(F) auxiliary space. Other operations take O(1) amortized expected time. Stored space is O(T + R + U) for T posts, R following relations, and U retained user-map entries.

Always include the user's own posts, even without a follow relation. Repeated follows use set semantics; unfollowing an absent relation is harmless. Timestamp order, rather than tweet ID magnitude, determines recency.

Follow-up: keep only a bounded recent history per user. Explain when older posts could still be necessary.

## Verification

Named fixtures and an independent generated-input reference cover behavior. Judge results are recorded separately in metadata.
