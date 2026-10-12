#include <utility>
#include <vector>

// TreeNode is supplied by the judge or local adapter.
class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        std::vector<std::pair<TreeNode*, bool>> pending{{root, false}};
        int total = 0;
        while (!pending.empty()) {
            const auto [node, is_left] = pending.back(); pending.pop_back();
            if (is_left && node->left == nullptr && node->right == nullptr) { total += node->val; }
            if (node->right != nullptr) { pending.emplace_back(node->right, false); }
            if (node->left != nullptr) { pending.emplace_back(node->left, true); }
        }
        return total;
    }
};
