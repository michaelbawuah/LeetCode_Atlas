#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    Solution solution;
    auto first = args.at(0).get<std::vector<int>>();
    auto second = args.at(2).get<std::vector<int>>();
    solution.merge(first, args.at(1).get<int>(), second, args.at(3).get<int>());
    return first;
}
