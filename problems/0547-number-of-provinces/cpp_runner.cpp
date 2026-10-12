#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto connected = args.at(0).get<vector<vector<int>>>();
    Solution solution;
    return solution.findCircleNum(connected);
}
