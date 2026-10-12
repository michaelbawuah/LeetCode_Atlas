#include <cstddef>
#include <memory>
#include <vector>

using std::vector;

// TreeNode is supplied by the judge or local adapter.
class Solution {
    struct Range {
        std::size_t low;
        std::size_t high;
        TreeNode** destination;
    };

public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        TreeNode* root = nullptr;
        vector<Range> pending{{0, nums.size(), &root}};
        // Independent ownership survives exceptions during allocation or traversal.
        vector<std::unique_ptr<TreeNode>> owned;
        owned.reserve(nums.size());
        while (!pending.empty()) {
            const Range current = pending.back();
            pending.pop_back();
            if (current.low == current.high) {
                continue;
            }
            const std::size_t middle = current.low + (current.high - current.low) / 2;
            owned.push_back(std::make_unique<TreeNode>(nums[middle]));
            TreeNode* node = owned.back().get();
            *current.destination = node;
            pending.push_back({middle + 1, current.high, &node->right});
            pending.push_back({current.low, middle, &node->left});
        }
        // The judge, or the adapter's TreeResultOwner, owns the completed output.
        for (auto& node : owned) {
            static_cast<void>(node.release());
        }
        return root;
    }
};
