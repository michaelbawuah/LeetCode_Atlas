#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto nums = args.at(0).get<std::vector<int>>();
    const auto target = args.at(1).get<int>();
    Solution solution;
    return solution.search(nums, target);
}
