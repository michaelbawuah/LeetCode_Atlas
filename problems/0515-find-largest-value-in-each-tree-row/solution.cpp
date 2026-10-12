#include <algorithm>
#include <cstddef>
#include <deque>
#include <vector>

using std::vector;

// TreeNode is supplied by the judge or local adapter.
class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        std::deque<TreeNode*> pending;
        if (root != nullptr) { pending.push_back(root); }
        vector<int> result;
        while (!pending.empty()) {
            int greatest = pending.front()->val;
            const auto count = pending.size();
            for (std::size_t index = 0; index < count; ++index) {
                TreeNode* node = pending.front(); pending.pop_front();
                greatest = std::max(greatest, node->val);
                if (node->left != nullptr) { pending.push_back(node->left); }
                if (node->right != nullptr) { pending.push_back(node->right); }
            }
            result.push_back(greatest);
        }
        return result;
    }
};
