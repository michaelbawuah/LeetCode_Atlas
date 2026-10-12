#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto m = args.at(0).get<int>();
    auto n = args.at(1).get<int>();
    Solution solution;
    return solution.uniquePaths(m, n);
}
