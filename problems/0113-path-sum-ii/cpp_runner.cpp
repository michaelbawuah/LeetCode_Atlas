#include <tuple>

#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    TreeArena arena;
    TreeNode* root = arena.build(args.at(0));
    std::vector<std::tuple<TreeNode*, int, TreeNode*, TreeNode*>> original;
    std::vector<TreeNode*> snapshot_pending;
    if (root != nullptr) {
        snapshot_pending.push_back(root);
    }
    while (!snapshot_pending.empty()) {
        TreeNode* node = snapshot_pending.back();
        snapshot_pending.pop_back();
        original.emplace_back(node, node->val, node->left, node->right);
        if (node->left != nullptr) {
            snapshot_pending.push_back(node->left);
        }
        if (node->right != nullptr) {
            snapshot_pending.push_back(node->right);
        }
    }
    Solution solution;
    auto result = solution.pathSum(root, args.at(1).get<int>());
    for (const auto& [node, value, left, right] : original) {
        if (node->val != value || node->left != left || node->right != right) {
            throw std::logic_error("read-only tree method changed original node links or values");
        }
    }
    return result;
}
