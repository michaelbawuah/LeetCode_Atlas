#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto equations = args.at(0).get<std::vector<std::vector<std::string>>>();
    auto values = args.at(1).get<std::vector<double>>();
    auto queries = args.at(2).get<std::vector<std::vector<std::string>>>();
    Solution solution;
    return solution.calcEquation(equations, values, queries);
}
