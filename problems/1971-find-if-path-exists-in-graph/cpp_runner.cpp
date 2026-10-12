#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json &args) {
    auto n = args.at(0).get<int>();
    auto edges = args.at(1).get<vector<vector<int>>>();
    auto source = args.at(2).get<int>();
    auto destination = args.at(3).get<int>();
    Solution solution;
    return solution.validPath(n, edges, source, destination);
}
