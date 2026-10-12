#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto first = args.at(0).get<std::string>();
    auto second = args.at(1).get<std::string>();
    Solution solution;
    return solution.minimumDeleteSum(first, second);
}
