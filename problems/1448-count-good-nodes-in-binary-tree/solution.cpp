#include <algorithm>
#include <utility>
#include <vector>

// TreeNode is supplied by the judge or local adapter.
class Solution {
public:
    int goodNodes(TreeNode* root) {
        std::vector<std::pair<TreeNode*, int>> pending{{root, root->val}};
        int answer = 0;
        while (!pending.empty()) {
            const auto [node, previous_maximum] = pending.back(); pending.pop_back();
            if (node->val >= previous_maximum) { ++answer; }
            const int greatest = std::max(previous_maximum, node->val);
            if (node->right != nullptr) { pending.emplace_back(node->right, greatest); }
            if (node->left != nullptr) { pending.emplace_back(node->left, greatest); }
        }
        return answer;
    }
};
