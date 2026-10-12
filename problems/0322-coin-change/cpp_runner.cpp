#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto coins = args.at(0).get<std::vector<int>>();
    const auto amount = args.at(1).get<int>();
    Solution solution;
    return solution.coinChange(coins, amount);
}
