#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto gas = args.at(0).get<vector<int>>();
    auto cost = args.at(1).get<vector<int>>();
    Solution solution;
    return solution.canCompleteCircuit(gas, cost);
}
