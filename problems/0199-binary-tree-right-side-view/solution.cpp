#include <cstddef>
#include <utility>
#include <vector>

using std::vector;

// TreeNode is supplied by the judge or local adapter.
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        if (root == nullptr) {
            return {};
        }
        vector<int> view;
        vector<std::pair<TreeNode*, std::size_t>> pending{{root, 0}};
        while (!pending.empty()) {
            const auto [node, depth] = pending.back();
            pending.pop_back();
            if (depth == view.size()) {
                view.push_back(node->val);
            }
            if (node->left != nullptr) {
                pending.emplace_back(node->left, depth + 1);
            }
            if (node->right != nullptr) {
                pending.emplace_back(node->right, depth + 1);
            }
        }
        return view;
    }
};
