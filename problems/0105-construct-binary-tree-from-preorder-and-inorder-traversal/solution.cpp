#include <cstddef>
#include <memory>
#include <vector>

using std::vector;

// TreeNode is supplied by the judge or local adapter.
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.empty()) {
            return nullptr;
        }
        // Stage independent ownership so a construction exception cannot leak nodes.
        vector<std::unique_ptr<TreeNode>> owned;
        owned.reserve(preorder.size());
        owned.push_back(std::make_unique<TreeNode>(preorder.front()));
        TreeNode* root = owned.front().get();
        vector<TreeNode*> pending{root};
        std::size_t inorder_index = 0;
        for (std::size_t index = 1; index < preorder.size(); ++index) {
            owned.push_back(std::make_unique<TreeNode>(preorder[index]));
            TreeNode* child = owned.back().get();
            if (pending.back()->val != inorder.at(inorder_index)) {
                pending.back()->left = child;
            } else {
                TreeNode* parent = pending.back();
                pending.pop_back();
                ++inorder_index;
                while (!pending.empty() && pending.back()->val == inorder.at(inorder_index)) {
                    parent = pending.back();
                    pending.pop_back();
                    ++inorder_index;
                }
                parent->right = child;
            }
            pending.push_back(child);
        }
        // The returned tree transfers to the judge, or TreeResultOwner in local tests.
        for (auto& node : owned) {
            static_cast<void>(node.release());
        }
        return root;
    }
};
