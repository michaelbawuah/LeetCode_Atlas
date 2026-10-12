#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json &args) {
    auto n = args.at(0).get<int>();
    auto connections = args.at(1).get<vector<vector<int>>>();
    Solution solution;
    return solution.makeConnected(n, connections);
}
