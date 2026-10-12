# Practice routes

[All problems](problems.md) · [Pattern atlas](patterns.md) · [Worked traces](traces.md) · [Roadmap](roadmap.md)

Use Python for the primary coding practice track and C++23 for the selected counterparts. Start with a problem's interface and examples, try it before opening the solution, then compare the state and invariant behind your approach.

## Choose one route

Read each row from left to right. Move on when you can explain the safe transition, construct a counterexample to a tempting wrong approach, and implement the solution without consulting the code.

| Route | Sequence | Question to explain |
|---|---|---|
| Lookup and windows | [Two Sum](../problems/0001-two-sum/README.md) → [Group Anagrams](../problems/0049-group-anagrams/README.md) → [Permutation in String](../problems/0567-permutation-in-string/README.md) → [Minimum Window](../problems/0076-minimum-window-substring/README.md) → [Sliding Window Maximum](../problems/0239-sliding-window-maximum/README.md) | Which retained values are sufficient, and which can be discarded? |
| Links and trees | [Reverse List](../problems/0206-reverse-linked-list/README.md) → [Swap Pairs](../problems/0024-swap-nodes-in-pairs/README.md) → [Merge K Lists](../problems/0023-merge-k-sorted-lists/README.md) → [Reconstruct Tree](../problems/0105-construct-binary-tree-from-preorder-and-inorder-traversal/README.md) → [LCA](../problems/0236-lowest-common-ancestor-of-a-binary-tree/README.md) | What preserves existing node identity and connectivity? |
| Graphs | [Islands](../problems/0200-number-of-islands/README.md) → [Course Schedule](../problems/0207-course-schedule/README.md) → [Network Delay](../problems/0743-network-delay-time/README.md) → [Minimum Effort Path](../problems/1631-path-with-minimum-effort/README.md) → [Critical Connections](../problems/1192-critical-connections-in-a-network/README.md) | How do the frontier and meaning of visited state change? |
| Dynamic programming | [House Robber](../problems/0198-house-robber/README.md) → [Coin Change II](../problems/0518-coin-change-ii/README.md) → [Edit Distance](../problems/0072-edit-distance/README.md) → [Longest Palindromic Subsequence](../problems/0516-longest-palindromic-subsequence/README.md) → [Burst Balloons](../problems/0312-burst-balloons/README.md) | What does one state mean, and which subproblems must already be known? |
| Stateful interfaces | [Min Stack](../problems/0155-min-stack/README.md) → [LRU Cache](../problems/0146-lru-cache/README.md) → [Stock Span](../problems/0901-online-stock-span/README.md) → [TimeMap](../problems/0981-time-based-key-value-store/README.md) → [Mutable Range Sums](../problems/0307-range-sum-query-mutable/README.md) | Which invariant must hold after every operation? |
| C++ arithmetic and ownership | [Reverse Integer](../problems/0007-reverse-integer/README.md) → [Single Number II](../problems/0137-single-number-ii/README.md) → [Unique Paths II](../problems/0063-unique-paths-ii/README.md) → [Add Two Numbers](../problems/0002-add-two-numbers/README.md) → [Merge K Lists](../problems/0023-merge-k-sorted-lists/README.md) | Which intermediate values can overflow, and who owns each node? |

## Make three passes

1. **Understand:** derive the baseline, identify repeated work, and state the invariant before reading the optimized code. Walk one example and one edge case by hand.
2. **Recall:** implement from the interface under a self-chosen time limit. Explain why each update is safe and include hidden costs such as slices, sorting, string copies, and output construction.
3. **Transfer:** return later without looking at the implementation. Change an assumption using the follow-up, or compare Python and C++ where both exist.

Keep an attempt record separate from the implementation catalog. A useful record has the problem ID, date, language, elapsed time, whether you used hints, the mistake or insight, and the next follow-up to try. The repository's implementation count does not infer these practice activities.

## Check one problem

```bash
python -m atlas run 28
python -m atlas run 236 --args '[[3,5,1,6,2,0,8,null,null,7,4],7,4]'
python -m pytest problems/0063-unique-paths-ii
python -m atlas list --pattern interval-dp
```

For LCA, the final two JSON values resolve to the existing nodes in the first argument's tree. They are not separate trees. For a design problem, `python -m atlas run 901` executes its first named operation history.

The [verification guide](verification.md) explains how to run the complete Python and C++ checks. Turn an informative failure into a named regression after understanding its cause.
