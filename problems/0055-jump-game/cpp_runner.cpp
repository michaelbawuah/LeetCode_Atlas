#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto nums = args.at(0).get<vector<int>>();
    Solution solution;
    return solution.canJump(nums);
}
