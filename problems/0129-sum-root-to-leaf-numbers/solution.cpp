#include <cstdint>
#include <utility>
#include <vector>

// TreeNode is supplied by the judge or local adapter.
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        std::int64_t total = 0;
        std::vector<std::pair<TreeNode*, std::int64_t>> pending{{root, 0}};
        while (!pending.empty()) {
            const auto [node, prefix] = pending.back();
            pending.pop_back();
            const std::int64_t number = prefix * 10 + node->val;
            if (node->left == nullptr && node->right == nullptr) {
                total += number;
            }
            if (node->right != nullptr) {
                pending.emplace_back(node->right, number);
            }
            if (node->left != nullptr) {
                pending.emplace_back(node->left, number);
            }
        }
        // The official sum fits a signed 32-bit integer.
        return static_cast<int>(total);
    }
};
