#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto count = args.at(0).get<int>();
    auto edges = args.at(1).get<std::vector<std::vector<int>>>();
    auto queries = args.at(2).get<std::vector<std::vector<int>>>();
    Solution solution;
    return solution.checkIfPrerequisite(count, edges, queries);
}
