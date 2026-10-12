#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto arg0 = args.at(0).get<std::vector<int>>();
    Solution solution;
    return solution.findNumberOfLIS(arg0);
}
