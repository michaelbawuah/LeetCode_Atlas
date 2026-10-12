#include <vector>

// TreeNode is supplied by the judge or local adapter.
class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        std::vector<TreeNode*> pending{root};
        long long total = 0;
        while (!pending.empty()) {
            TreeNode* node = pending.back(); pending.pop_back();
            if (low <= node->val && node->val <= high) { total += node->val; }
            if (node->left != nullptr && node->val > low) { pending.push_back(node->left); }
            if (node->right != nullptr && node->val < high) { pending.push_back(node->right); }
        }
        return static_cast<int>(total);
    }
};
