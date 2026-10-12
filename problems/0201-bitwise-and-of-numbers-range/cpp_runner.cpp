#include "atlas_adapter.hpp"
#include "solution.cpp"

json run_case(const json& args) {
    auto left = args.at(0).get<int>();
    auto right = args.at(1).get<int>();
    Solution solution;
    return solution.rangeBitwiseAnd(left, right);
}
