#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json &args) {
    auto start = args.at(0).get<string>();
    auto end = args.at(1).get<string>();
    auto bank = args.at(2).get<vector<string>>();
    Solution solution;
    return solution.minMutation(start, end, bank);
}
