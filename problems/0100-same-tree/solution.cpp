#include <utility>
#include <vector>

// TreeNode is supplied by the judge or local adapter.
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        std::vector<std::pair<TreeNode*, TreeNode*>> pending{{p, q}};
        while (!pending.empty()) {
            const auto [first, second] = pending.back();
            pending.pop_back();
            if (first == nullptr || second == nullptr) {
                if (first != second) {
                    return false;
                }
                continue;
            }
            if (first->val != second->val) {
                return false;
            }
            pending.emplace_back(first->left, second->left);
            pending.emplace_back(first->right, second->right);
        }
        return true;
    }
};
