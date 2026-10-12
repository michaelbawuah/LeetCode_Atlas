#include <cstddef>
#include <queue>
#include <utility>
#include <vector>

using std::vector;

// TreeNode is supplied by the judge or local adapter.
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        if (root == nullptr) {
            return result;
        }
        std::queue<TreeNode*> pending;
        pending.push(root);
        while (!pending.empty()) {
            const std::size_t width = pending.size();
            vector<int> level;
            level.reserve(width);
            for (std::size_t index = 0; index < width; ++index) {
                TreeNode* node = pending.front();
                pending.pop();
                level.push_back(node->val);
                if (node->left != nullptr) {
                    pending.push(node->left);
                }
                if (node->right != nullptr) {
                    pending.push(node->right);
                }
            }
            result.push_back(std::move(level));
        }
        return result;
    }
};
