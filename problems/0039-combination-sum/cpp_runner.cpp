#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto candidates = args.at(0).get<vector<int>>();
    auto target = args.at(1).get<int>();
    Solution solution;
    return solution.combinationSum(candidates, target);
}
