#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    TreeArena arena;
    auto* root = arena.build(args.at(0));
    const int low = args.at(1).get<int>(), high = args.at(2).get<int>();
    Solution solution;
    return solution.rangeSumBST(root, low, high);
}
