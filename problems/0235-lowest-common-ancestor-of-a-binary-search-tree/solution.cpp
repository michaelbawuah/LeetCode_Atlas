#include <algorithm>

// TreeNode is supplied by the judge or local adapter.
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        const int low = std::min(p->val, q->val);
        const int high = std::max(p->val, q->val);
        while (root != nullptr) {
            if (root->val < low) {
                root = root->right;
            } else if (root->val > high) {
                root = root->left;
            } else {
                return root;
            }
        }
        return nullptr;
    }
};
