#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto count = args.at(0).get<int>();
    auto edges = args.at(1).get<std::vector<std::vector<int>>>();
    auto durations = args.at(2).get<std::vector<int>>();
    Solution solution;
    return solution.minimumTime(count, edges, durations);
}
