#include <stdexcept>
#include <vector>

// TreeNode is supplied by the judge or local adapter.
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        std::vector<TreeNode*> ancestors;
        TreeNode* current = root;
        while (current != nullptr || !ancestors.empty()) {
            while (current != nullptr) {
                ancestors.push_back(current);
                current = current->left;
            }
            current = ancestors.back();
            ancestors.pop_back();
            if (--k == 0) {
                return current->val;
            }
            current = current->right;
        }
        throw std::out_of_range("k must identify an existing BST node");
    }
};
