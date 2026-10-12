#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    TreeArena arena;
    TreeNode* root = arena.build(args.at(0));
    const int target = args.at(1).get<int>();
    Solution solution;
    return solution.hasPathSum(root, target);
}
