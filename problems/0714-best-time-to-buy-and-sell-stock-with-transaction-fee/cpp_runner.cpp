#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto prices = args.at(0).get<std::vector<int>>();
    auto fee = args.at(1).get<int>();
    Solution solution;
    return solution.maxProfit(prices, fee);
}
