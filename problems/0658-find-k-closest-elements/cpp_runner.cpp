#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    Solution solution;
    auto nums = args.at(0).get<std::vector<int>>();
    return solution.findClosestElements(nums, args.at(1).get<int>(), args.at(2).get<int>());
}
