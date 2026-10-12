#include <cstddef>
#include <deque>

// TreeNode is supplied by the judge or local adapter.
class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        std::deque<TreeNode*> pending{root};
        int answer = root->val;
        while (!pending.empty()) {
            answer = pending.front()->val;
            const auto count = pending.size();
            for (std::size_t index = 0; index < count; ++index) {
                TreeNode* node = pending.front(); pending.pop_front();
                if (node->left != nullptr) { pending.push_back(node->left); }
                if (node->right != nullptr) { pending.push_back(node->right); }
            }
        }
        return answer;
    }
};
