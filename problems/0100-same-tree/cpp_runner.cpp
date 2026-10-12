#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    TreeArena arena;
    TreeNode* first = arena.build(args.at(0));
    TreeNode* second = arena.build(args.at(1));
    Solution solution;
    return solution.isSameTree(first, second);
}
