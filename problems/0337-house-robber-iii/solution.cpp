#include <algorithm>
#include <vector>

// TreeNode is supplied by the judge or local adapter.
class Solution {
    struct Frame {
        TreeNode* node;
        int stage = 0;
        int left_take = 0;
        int left_skip = 0;
        int right_take = 0;
        int right_skip = 0;
    };

public:
    int rob(TreeNode* root) {
        if (root == nullptr) {
            return 0;
        }
        std::vector<Frame> pending{{root}};
        while (true) {
            Frame& frame = pending.back();
            if (frame.stage == 0) {
                frame.stage = 1;
                if (frame.node->left != nullptr) {
                    pending.push_back({frame.node->left});
                }
            } else if (frame.stage == 1) {
                frame.stage = 2;
                if (frame.node->right != nullptr) {
                    pending.push_back({frame.node->right});
                }
            } else {
                const int take = frame.node->val + frame.left_skip + frame.right_skip;
                const int skip = std::max(frame.left_take, frame.left_skip)
                    + std::max(frame.right_take, frame.right_skip);
                pending.pop_back();
                if (pending.empty()) {
                    return std::max(take, skip);
                }
                Frame& parent = pending.back();
                if (parent.stage == 1) {
                    parent.left_take = take;
                    parent.left_skip = skip;
                } else {
                    parent.right_take = take;
                    parent.right_skip = skip;
                }
            }
        }
    }
};
