#include <utility>
#include <vector>

// TreeNode is supplied by the judge or local adapter.
class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        if (root == nullptr) {
            return false;
        }
        std::vector<std::pair<TreeNode*, long long>> pending{{root, root->val}};
        while (!pending.empty()) {
            const auto [node, total] = pending.back();
            pending.pop_back();
            if (node->left == nullptr && node->right == nullptr && total == targetSum) {
                return true;
            }
            if (node->right != nullptr) {
                pending.emplace_back(node->right, total + node->right->val);
            }
            if (node->left != nullptr) {
                pending.emplace_back(node->left, total + node->left->val);
            }
        }
        return false;
    }
};
