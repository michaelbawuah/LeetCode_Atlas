#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto arg0 = args.at(0).get<int>();
    auto arg1 = args.at(1).get<std::vector<int>>();
    Solution solution;
    return solution.maxProfit(arg0, arg1);
}
