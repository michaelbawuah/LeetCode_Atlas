# 105 · Construct Binary Tree from Preorder and Inorder Traversal

[LeetCode problem](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

## Intuition
Preorder introduces nodes; inorder tells when each pending left region is complete.

## Baseline and approach
Recursive slicing repeatedly copies arrays and can become quadratic. The iterative construction keeps ancestors whose inorder visit is pending. A new preorder node becomes a left child until the stack top matches the next inorder value; completed ancestors are then popped and the node starts their right region.

## Why it works
The stack holds the path of introduced nodes that still await their inorder position. Before the next inorder value is reached, preorder must introduce a left descendant. Matching and popping an ancestor means its left region is complete; the next unintroduced node belongs to the last completed ancestor's right subtree. Unique values make these boundaries unambiguous.

## Complexity
**O(n) time; O(h) auxiliary; O(n) output space.** Here n is the number of nodes and h is the tree height where relevant. Adapter construction and serialization are separate from submission-method costs.

## Pitfalls
Both traversals describe the same nonempty tree and contain unique values. Avoid array slicing in the main traversal; an explicit stack avoids recursive failure on a skewed tree. Returned nodes are newly allocated.

## Follow-up
Can you construct an equivalent tree when values repeat, and what additional information would be necessary?

## Python and C++23
Both versions construct iteratively. Python uses an O(h) ancestor stack and allocates O(n) output nodes. C++ additionally stages every new node in unique_ptr storage, taking O(n) auxiliary space for exception-safe construction. On success it releases that storage; the judge owns the result, while the local runner immediately wraps it in TreeResultOwner. Returned nodes are freed once after serialization, including if serialization throws. Neither version modifies its traversal arrays.

C++23 submission-method complexity: **O(n) time; O(n) auxiliary ownership staging; O(n) output space**. Adapter ownership and JSON conversion costs are separate.
