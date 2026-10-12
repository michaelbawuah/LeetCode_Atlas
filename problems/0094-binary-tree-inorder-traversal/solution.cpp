#include <vector>

using std::vector;

// TreeNode is supplied by the judge or local adapter.
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<TreeNode*> ancestors;
        vector<int> values;
        TreeNode* current = root;
        while (current != nullptr || !ancestors.empty()) {
            while (current != nullptr) {
                ancestors.push_back(current);
                current = current->left;
            }
            current = ancestors.back();
            ancestors.pop_back();
            values.push_back(current->val);
            current = current->right;
        }
        return values;
    }
};
