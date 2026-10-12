#include <utility>
#include <vector>

using std::vector;

// TreeNode is supplied by the judge or local adapter.
class Solution {
    struct Frame {
        TreeNode* node;
        int total;
        bool leaving;
    };

public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> result;
        if (root == nullptr) {
            return result;
        }
        vector<int> path;
        vector<Frame> pending{{root, 0, false}};
        while (!pending.empty()) {
            const Frame current = pending.back();
            pending.pop_back();
            if (current.leaving) {
                path.pop_back();
                continue;
            }
            const int total = current.total + current.node->val;
            path.push_back(current.node->val);
            if (current.node->left == nullptr && current.node->right == nullptr && total == targetSum) {
                result.push_back(path);
            }
            pending.push_back({current.node, total, true});
            if (current.node->right != nullptr) {
                pending.push_back({current.node->right, total, false});
            }
            if (current.node->left != nullptr) {
                pending.push_back({current.node->left, total, false});
            }
        }
        return result;
    }
};
