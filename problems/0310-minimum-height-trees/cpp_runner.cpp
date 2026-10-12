#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json &args) {
    auto n = args.at(0).get<int>();
    auto edges = args.at(1).get<vector<vector<int>>>();
    Solution solution;
    return solution.findMinHeightTrees(n, edges);
}
