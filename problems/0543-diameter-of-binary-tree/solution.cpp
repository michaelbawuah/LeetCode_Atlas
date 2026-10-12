#include <algorithm>
#include <unordered_map>
#include <utility>
#include <vector>

// TreeNode is supplied by the judge or local adapter.
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        std::unordered_map<TreeNode*, int> heights{{nullptr, 0}};
        std::vector<std::pair<TreeNode*, bool>> pending{{root, false}};
        int longest = 0;
        while (!pending.empty()) {
            const auto [node, ready] = pending.back();
            pending.pop_back();
            if (ready) {
                const int left = heights.at(node->left);
                const int right = heights.at(node->right);
                longest = std::max(longest, left + right);
                heights[node] = 1 + std::max(left, right);
            } else {
                pending.emplace_back(node, true);
                if (node->right != nullptr) {
                    pending.emplace_back(node->right, false);
                }
                if (node->left != nullptr) {
                    pending.emplace_back(node->left, false);
                }
            }
        }
        return longest;
    }
};
