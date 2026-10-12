#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    Solution solution;
    auto first = args.at(0).get<std::vector<int>>();
    auto second = args.at(1).get<std::vector<int>>();
    return solution.findMedianSortedArrays(first, second);
}
