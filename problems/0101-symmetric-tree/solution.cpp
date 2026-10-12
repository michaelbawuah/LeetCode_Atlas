#include <utility>
#include <vector>

// TreeNode is supplied by the judge or local adapter.
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (root == nullptr) { return true; }
        std::vector<std::pair<TreeNode*, TreeNode*>> pending{{root->left, root->right}};
        while (!pending.empty()) {
            const auto [left, right] = pending.back();
            pending.pop_back();
            if (left == nullptr || right == nullptr) {
                if (left != right) { return false; }
                continue;
            }
            if (left->val != right->val) { return false; }
            pending.emplace_back(left->left, right->right);
            pending.emplace_back(left->right, right->left);
        }
        return true;
    }
};
