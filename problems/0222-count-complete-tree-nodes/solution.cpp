#include <vector>

// TreeNode is supplied by the judge or local adapter.
class Solution {
public:
    int countNodes(TreeNode* root) {
        std::vector<TreeNode*> pending;
        if (root != nullptr) { pending.push_back(root); }
        int total = 0;
        while (!pending.empty()) {
            TreeNode* node = pending.back(); pending.pop_back();
            int left_height = 0, right_height = 0;
            for (TreeNode* left = node; left != nullptr; left = left->left) { ++left_height; }
            for (TreeNode* right = node; right != nullptr; right = right->right) { ++right_height; }
            if (left_height == right_height) {
                total += static_cast<int>((1LL << left_height) - 1);
            } else {
                ++total;
                if (node->right != nullptr) { pending.push_back(node->right); }
                if (node->left != nullptr) { pending.push_back(node->left); }
            }
        }
        return total;
    }
};
