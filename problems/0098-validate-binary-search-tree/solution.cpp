#include <vector>

// TreeNode is supplied by LeetCode or the local adapter.
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        std::vector<TreeNode*> ancestors;
        TreeNode* current = root;
        bool have_previous = false;
        int previous = 0;
        while (current != nullptr || !ancestors.empty()) {
            while (current != nullptr) {
                ancestors.push_back(current);
                current = current->left;
            }
            current = ancestors.back();
            ancestors.pop_back();
            if (have_previous && current->val <= previous) {
                return false;
            }
            previous = current->val;
            have_previous = true;
            current = current->right;
        }
        return true;
    }
};
