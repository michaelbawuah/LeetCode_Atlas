#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    Solution solution;
    auto nums = args.at(1).get<std::vector<int>>();
    return solution.minSubArrayLen(args.at(0).get<int>(), nums);
}
