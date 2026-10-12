#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto nums = args.at(0).get<std::vector<int>>();
    Solution solution;
    return solution.rob(nums);
}
