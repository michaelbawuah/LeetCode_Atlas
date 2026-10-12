#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto n = args.at(0).get<int>();
    Solution solution;
    return solution.numSquares(n);
}
