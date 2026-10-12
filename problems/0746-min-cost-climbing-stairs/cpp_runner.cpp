#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto cost = args.at(0).get<std::vector<int>>();
    Solution solution;
    return solution.minCostClimbingStairs(cost);
}
