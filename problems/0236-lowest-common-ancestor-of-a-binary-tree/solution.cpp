#include <algorithm>
#include <cstddef>
#include <utility>
#include <vector>

// TreeNode is supplied by the judge or local adapter.
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        std::vector<TreeNode*> path;
        std::vector<TreeNode*> p_path;
        std::vector<TreeNode*> q_path;
        std::vector<std::pair<TreeNode*, bool>> pending{{root, false}};
        while (!pending.empty()) {
            const auto [node, leaving] = pending.back();
            pending.pop_back();
            if (leaving) {
                path.pop_back();
                continue;
            }
            path.push_back(node);
            if (node == p) {
                p_path = path;
            }
            if (node == q) {
                q_path = path;
            }
            if (!p_path.empty() && !q_path.empty()) {
                break;
            }
            pending.emplace_back(node, true);
            if (node->right != nullptr) {
                pending.emplace_back(node->right, false);
            }
            if (node->left != nullptr) {
                pending.emplace_back(node->left, false);
            }
        }
        TreeNode* ancestor = nullptr;
        const std::size_t common_length = std::min(p_path.size(), q_path.size());
        for (std::size_t index = 0; index < common_length && p_path[index] == q_path[index]; ++index) {
            ancestor = p_path[index];
        }
        return ancestor;
    }
};
