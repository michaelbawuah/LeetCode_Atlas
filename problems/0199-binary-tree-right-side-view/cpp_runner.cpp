#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    TreeArena arena;
    TreeNode* root = arena.build(args.at(0));
    Solution solution;
    return solution.rightSideView(root);
}
