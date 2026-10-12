#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto times = args.at(0).get<vector<vector<int>>>();
    auto n = args.at(1).get<int>();
    auto k = args.at(2).get<int>();
    Solution solution;
    return solution.networkDelayTime(times, n, k);
}
