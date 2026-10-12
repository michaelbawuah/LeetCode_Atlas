#include <algorithm>
#include <cstddef>
#include <deque>
#include <utility>
#include <vector>

using std::vector;

// TreeNode is supplied by the judge or local adapter.
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        std::deque<TreeNode*> pending;
        if (root != nullptr) { pending.push_back(root); }
        vector<vector<int>> result;
        bool reverse = false;
        while (!pending.empty()) {
            vector<int> row;
            const auto count = pending.size();
            for (std::size_t index = 0; index < count; ++index) {
                TreeNode* node = pending.front(); pending.pop_front();
                row.push_back(node->val);
                if (node->left != nullptr) { pending.push_back(node->left); }
                if (node->right != nullptr) { pending.push_back(node->right); }
            }
            if (reverse) { std::reverse(row.begin(), row.end()); }
            result.push_back(std::move(row));
            reverse = !reverse;
        }
        return result;
    }
};
