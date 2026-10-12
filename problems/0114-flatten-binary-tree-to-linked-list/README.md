# 114 · Flatten Binary Tree to Linked List

[LeetCode problem](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/)

## Intuition
Preorder already defines the required chain order; the task is to replace each consecutive pair with a right link.

## Baseline and approach
Recording all nodes in preorder and then relinking them uses O(n) temporary storage. A DFS stack produces that order incrementally, connecting the previous node to the next and clearing its left child.

## Why it works
Before each visit, the completed chain contains exactly the previously visited preorder nodes. Pushing right before left preserves preorder. Connecting the previous tail to the current node extends that chain, while pending original child references remain on the stack. Clearing the final tail completes a right-only acyclic chain.

## Complexity
**O(n) time; O(h) space.** Here n is the number of nodes and h is the tree height where relevant. Adapter construction and serialization are separate from submission-method costs.

## Pitfalls
Save child references by pushing them before later rewiring can erase them. The method returns `None`; `result_from_arg: 0` makes the local runner serialize the changed root. All existing nodes must be reused.

## Follow-up
Thread the original tree through predecessor links to flatten it with O(1) auxiliary storage.

## C++23 implementation

C++23 has the standard `void flatten(TreeNode*)` interface. Its adapter serializes the changed argument zero and checks the exact original preorder node identities, unchanged values, null left links, and an acyclic right-only tail. The method creates or deletes no nodes.

C++23 submission cost: **O(n) time; O(h) space**. Here n is node count, h is tree height, w is maximum level width, and L is the number of returned path elements when applicable. Adapter construction, snapshots, and serialization are measured separately.
