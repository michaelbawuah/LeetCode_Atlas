#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    Solution solution;
    auto values0 = args.at(0).get<std::vector<int>>();
    auto values1 = args.at(1).get<std::vector<int>>();
    auto values2 = args.at(2).get<std::vector<int>>();
    auto values3 = args.at(3).get<std::vector<int>>();
    return solution.fourSumCount(values0, values1, values2, values3);
}
