#include <vector>

// TreeNode is supplied by the judge or local adapter.
class Solution {
public:
    void flatten(TreeNode* root) {
        if (root == nullptr) {
            return;
        }
        std::vector<TreeNode*> pending{root};
        TreeNode* previous = nullptr;
        while (!pending.empty()) {
            TreeNode* node = pending.back();
            pending.pop_back();
            if (previous != nullptr) {
                previous->left = nullptr;
                previous->right = node;
            }
            if (node->right != nullptr) {
                pending.push_back(node->right);
            }
            if (node->left != nullptr) {
                pending.push_back(node->left);
            }
            previous = node;
        }
        previous->left = nullptr;
        previous->right = nullptr;
    }
};
