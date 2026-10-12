#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    TreeArena arena;
    TreeNode* root = arena.build(args.at(0));
    std::vector<std::pair<TreeNode*, int>> preorder;
    std::vector<TreeNode*> pending;
    if (root != nullptr) {
        pending.push_back(root);
    }
    while (!pending.empty()) {
        TreeNode* node = pending.back();
        pending.pop_back();
        preorder.emplace_back(node, node->val);
        if (node->right != nullptr) {
            pending.push_back(node->right);
        }
        if (node->left != nullptr) {
            pending.push_back(node->left);
        }
    }
    Solution solution;
    solution.flatten(root);
    TreeNode* current = root;
    for (const auto& [node, value] : preorder) {
        if (current != node || current->val != value || current->left != nullptr) {
            throw std::logic_error("flatten did not preserve original preorder node identities and values");
        }
        current = current->right;
    }
    if (current != nullptr) {
        throw std::logic_error("flatten produced extra nodes or a cycle");
    }
    return tree_to_json(root);
}
