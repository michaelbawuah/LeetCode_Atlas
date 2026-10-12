#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto amount = args.at(0).get<int>();
    auto coins = args.at(1).get<std::vector<int>>();
    Solution solution;
    return solution.change(amount, coins);
}
