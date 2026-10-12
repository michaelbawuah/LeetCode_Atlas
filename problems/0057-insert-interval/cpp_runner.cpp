#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto intervals = args.at(0).get<std::vector<std::vector<int>>>();
    auto new_interval = args.at(1).get<std::vector<int>>();
    Solution solution;
    return solution.insert(intervals, new_interval);
}
