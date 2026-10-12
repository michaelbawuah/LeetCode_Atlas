#include <algorithm>
#include <vector>

// TreeNode is supplied by the judge or local adapter.
class Solution {
    struct Frame {
        TreeNode* node;
        int stage = 0;
        int left_gain = 0;
        int right_gain = 0;
    };

public:
    int maxPathSum(TreeNode* root) {
        int best = root->val;
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
                const int left = std::max(0, frame.left_gain);
                const int right = std::max(0, frame.right_gain);
                best = std::max(best, frame.node->val + left + right);
                const int gain = frame.node->val + std::max(left, right);
                pending.pop_back();
                if (!pending.empty()) {
                    Frame& parent = pending.back();
                    if (parent.stage == 1) {
                        parent.left_gain = gain;
                    } else {
                        parent.right_gain = gain;
                    }
                }
            }
        }
        return best;
    }
};
