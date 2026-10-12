#include <algorithm>
#include <cstdlib>
#include <vector>

// TreeNode is supplied by the judge or local adapter.
class Solution {
    struct Frame {
        TreeNode* node;
        int stage = 0;
        int left_height = 0;
        int right_height = 0;
    };

public:
    bool isBalanced(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }
        std::vector<Frame> pending{{root}};
        while (!pending.empty()) {
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
                if (std::abs(frame.left_height - frame.right_height) > 1) {
                    return false;
                }
                const int height = 1 + std::max(frame.left_height, frame.right_height);
                pending.pop_back();
                if (!pending.empty()) {
                    Frame& parent = pending.back();
                    if (parent.stage == 1) {
                        parent.left_height = height;
                    } else {
                        parent.right_height = height;
                    }
                }
            }
        }
        return true;
    }
};
