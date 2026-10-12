#include <algorithm>
#include <utility>
#include <vector>

// TreeNode is supplied by the judge or local adapter.
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        std::vector<std::pair<TreeNode*, int>> pending{{root, 1}};
        int deepest = 0;
        while (!pending.empty()) {
            const auto [node, depth] = pending.back();
            pending.pop_back();
            deepest = std::max(deepest, depth);
            if (node->left != nullptr) {
                pending.emplace_back(node->left, depth + 1);
            }
            if (node->right != nullptr) {
                pending.emplace_back(node->right, depth + 1);
            }
        }
        return deepest;
    }
};
